"""Search index (web/data/search.json) and the buildings along each street (web/data/search/streets-<k>.json).

London has no open register that ties a house number to a footprint: Overture's buildings carry no address, and the
OS address products are not open. What the index holds instead:

names: named buildings, each pointing at its footprint (gid, the building's row in data/buildings.parquet, as in the
  tiles): Wikidata labels (on every footprint the item was placed on), the names of the curated stories, the names of listed buildings (Historic England's
  list, by the Colouring London link or the entry's point inside a footprint) and OpenStreetMap building names.
  A label that is only an address ('5, Mulberry Walk SW3') is left out, unless it is a Wikidata item with a Wikipedia
  article ('30 St Mary Axe').
addresses: the addresses in the names of listed buildings ('42 AND 44, HILL STREET W1'), one per house number. They
  cover listed buildings only, so the viewer offers no 'nearest number' for an address it does not know.
streets: every named street (Overture roads, OpenStreetMap), split where one name is used in places far apart, with
  the borough it lies in and the footprints within NEAR metres of its line. The footprints are written to a few
  shards, fetched when a street is chosen, so the index the viewer loads stays small.
The OpenStreetMap names, the most numerous, go to web/data/search/named.json, which the viewer fetches after the index.
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely

from .city import BOROUGHS, CRS
from .s01e_ages import LISTED_THINGS

NEAR = 15.0       # metres from a footprint to a street's centre line: its frontage, not the block behind it
APART = 150.0     # metres; parts of one street name farther apart than this are separate streets
SHARDS = 16
SAME_PLACE = 250.0  # metres; one label on footprints this close is one place ('Palace of Westminster')
OUT = Path("web/data")
NOT_BUILDINGS = re.compile(r"\b(tomb|tombs|mausoleum|headstone|grave|obelisk|sundial|urn|vase|cattle trough)\b", re.I)
SMALL = {"of", "the", "and", "at", "in", "on", "to", "for", "with", "by", "from", "a", "an", "de", "la", "le"}
POSTCODE = re.compile(r"\s+(EC|WC|SW|SE|NW|N|E|W)\d+[A-Z]?$")


def title(s):
    """Historic England writes most names in capitals: 'CHURCH OF ST MARY' -> 'Church of St Mary'."""
    if s != s.upper():
        return s
    words = s.lower().split(" ")
    return " ".join(w if (i and w in SMALL) else w[:1].upper() + w[1:] for i, w in enumerate(words))


def numbers(part):
    """'42 AND 44' -> 42, 44; '31-41' -> 31, 33 … 41; '5 AND 5A' -> 5, 5A. None when the part is not plain numbers."""
    out = []
    for tok in re.split(r"\s*(?:,|\bAND\b|&)\s*", part.upper().removeprefix("NUMBERS ").removeprefix("NUMBER ")):
        tok = tok.strip()
        if not tok:
            continue
        m = re.fullmatch(r"(\d+)\s*-\s*(\d+)", tok)
        if m:
            a, b = int(m[1]), int(m[2])
            if not a < b <= a + 60:
                return None
            out += [str(n) for n in range(a, b + 1, 2 if a % 2 == b % 2 else 1)]
        elif re.fullmatch(r"\d+[A-Z]?", tok):
            out.append(tok)
        else:
            return None
    return out or None


def address(name):
    """('42 AND 44, HILL STREET W1') -> (['42', '44'], 'Hill Street'), or None when the name is not an address."""
    m = re.fullmatch(r"(.+?),\s*([A-Z][A-Za-z' .-]+?)", POSTCODE.sub("", name.strip()))
    if not m:
        return None
    nums = numbers(m[1])
    street = title(m[2].strip())
    if not nums or len(street) < 4 or LISTED_THINGS.search(street):
        return None
    return nums, street


def main():
    b = gpd.read_parquet("data/buildings.parquet", columns=["identificatie", "name", "planning_list_id", "geometry"])
    gid = {k: i for i, k in enumerate(b.identificatie)}
    geom = b.geometry.values
    cent = shapely.centroid(geom)

    boroughs = gpd.read_file("data/raw/boundary.json").set_crs(CRS, allow_override=True)
    boroughs = boroughs[boroughs.LAD24NM.isin(BOROUGHS)].reset_index(drop=True)
    area_names = list(boroughs.LAD24NM)
    btree = shapely.STRtree(boroughs.geometry.values)

    def borough_of(pts):
        idx = np.full(len(pts), -1)
        p, a = btree.query(pts, predicate="within")
        idx[p] = a
        return idx

    area = borough_of(cent)

    # ---- names: (label, footprint, kind) in order of trust; one label on nearby footprints becomes one result
    raw = []

    def add(label, g, kind):
        if label and g is not None and g >= 0:
            label = re.sub(r"\s+", " ", str(label)).strip()
            if len(label) >= 3:
                raw.append((label, int(g), kind))

    # Wikidata items with every footprint they were placed on (s06_wiki); a label that is an address names a
    # building only when the item has an article ('30 St Mary Axe')
    wd = {r["i"]: r["labelEn"] for r in csv.DictReader(open("data/raw/wd_buildings.csv"))}
    for i, place in json.load(open("data/wd_places.json")).items():
        label = wd.get(i)
        if label and (not re.search(r"\d", label) or place.get("en")):
            for bg in place["bags"]:
                add(label, gid.get(bg), "building")
    for L in json.load(open("data/curated.json")):
        for e in L["entries"]:
            if not re.match(r"\d", e["name"]):
                add(e["name"], gid.get(e["bag"]), "building")

    # listed buildings: by the Colouring London link, then by the entry's point inside a footprint (as s01e_ages)
    pts = pd.read_csv("data/raw/nhle_points.csv")
    entry = dict(zip(pts.ListEntry, pts.Name))
    link = [(g, int(float(n))) for g, n in enumerate(b.planning_list_id) if pd.notna(n)]
    pg = gpd.GeoDataFrame(pts, geometry=gpd.points_from_xy(pts.Easting, pts.Northing), crs=CRS)
    j = gpd.sjoin(pg, gpd.GeoDataFrame({"g": np.arange(len(b))}, geometry=geom, crs=CRS), predicate="within")
    link += list(zip(j.g, j.ListEntry))
    addr = defaultdict(dict)   # street -> number -> gid
    for g, n in dict.fromkeys(link):
        name = entry.get(n)
        if not isinstance(name, str) or LISTED_THINGS.search(name) or NOT_BUILDINGS.search(name):
            continue
        if re.search(r"\d", name):
            a = address(name)
            if a:
                for num in a[0]:
                    addr[a[1]].setdefault(num, int(g))
            continue
        add(title(name), g, "listed")

    # OpenStreetMap names of footprints, through Overture: shops, pubs, blocks of flats
    for g, name in enumerate(b.name):
        if isinstance(name, str) and not re.search(r"\d", name):
            add(name, g, "named")

    cx, cy = shapely.get_x(cent), shapely.get_y(cent)
    names, groups = defaultdict(list), defaultdict(list)
    for label, g, kind in raw:
        for grp in groups[label.lower()]:
            if np.hypot(cx[g] - cx[grp[1][0]], cy[g] - cy[grp[1][0]]) <= SAME_PLACE:
                if g not in grp[1]:
                    grp[1].append(g)
                break
        else:
            groups[label.lower()].append((label, [g], kind))
    for grp in groups.values():
        for label, gs, kind in grp:
            names[kind].append([label, gs[0] if len(gs) == 1 else gs, int(area[gs[0]])])

    # per street its numbers in order, and the borough most of them lie in
    addresses = []
    for street, nums in sorted(addr.items()):
        rows = sorted(nums.items(), key=lambda kv: (int(re.match(r"\d+", kv[0])[0]), kv[0]))
        a = pd.Series([area[g] for _, g in rows]).mode()[0]
        addresses.append([street, int(a), [[n, g] for n, g in rows]])

    # ---- streets
    r = pd.read_parquet("data/raw/overture_roads.parquet", columns=["name", "geometry"])
    r = gpd.GeoDataFrame(r.drop(columns="geometry"), geometry=gpd.GeoSeries.from_wkb(r.geometry), crs=4326).to_crs(CRS)
    r = r[r.name.notna()]
    whole = boroughs.union_all()
    r = r[r.intersects(whole)]
    btree_b = shapely.STRtree(geom)
    streets, members = [], []
    for name, grp in r.groupby("name"):
        lines = list(grp.geometry)
        # one name used in places far apart: each cluster of nearby segments is a street of its own
        blobs = shapely.union_all(shapely.buffer(lines, APART / 2))
        parts = list(getattr(blobs, "geoms", [blobs]))
        for part in parts:
            seg = shapely.union_all([l for l in lines if l.intersects(part)])
            near = btree_b.query(seg, predicate="dwithin", distance=NEAR)
            if not len(near):
                continue
            mid = seg.interpolate(0.5, normalized=True) if seg.geom_type == "LineString" else shapely.centroid(seg)
            a = borough_of(np.array([mid]))[0]
            if a < 0:
                a = np.bincount(area[near][area[near] >= 0]).argmax() if (area[near] >= 0).any() else -1
            streets.append([name, int(a), len(near)])
            members.append(sorted(int(x) for x in near))

    # the borough tells two streets of one name apart in the list
    order = sorted(range(len(streets)), key=lambda i: (streets[i][0], streets[i][1], -streets[i][2]))
    streets = [streets[i] for i in order]
    members = [members[i] for i in order]
    shards = [dict() for _ in range(SHARDS)]
    for i, m in enumerate(members):
        # gids rise along the list; deltas keep the shard small
        shards[i % SHARDS][i] = [m[0]] + list(np.diff(m).tolist())
    (OUT / "search").mkdir(exist_ok=True)
    for k, s in enumerate(shards):
        (OUT / "search" / f"streets-{k}.json").write_text(json.dumps(s, separators=(",", ":")))

    # the index the viewer loads first; the OpenStreetMap names follow in a second file
    dump = lambda path, o: path.write_text(json.dumps(o, ensure_ascii=False, separators=(",", ":")))
    dump(OUT / "search.json", dict(areas=area_names, shards=SHARDS, building=names["building"], listed=names["listed"],
                                   addresses=addresses, streets=streets))
    dump(OUT / "search" / "named.json", names["named"])
    kb = lambda path: path.stat().st_size // 1024
    shard_kb = sum(kb(OUT / "search" / f"streets-{k}.json") for k in range(SHARDS))
    print(f"names: {', '.join(f'{k} {len(v)}' for k, v in names.items())}; "
          f"{sum(len(a[2]) for a in addresses)} listed addresses on {len(addresses)} streets; {len(streets)} streets "
          f"({sum(len(m) for m in members)} street-building links)\n"
          f"search.json {kb(OUT / 'search.json')} KB, named.json {kb(OUT / 'search' / 'named.json')} KB, "
          f"street shards {shard_kb} KB")


if __name__ == "__main__":
    main()
