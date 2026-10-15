"""Verify the curated entries against their Wikipedia articles and place them on footprints.

An entry names its building's Wikidata item. It lands on the footprints listed under the item's National Heritage
List number (through Colouring London), else on the footprint its Wikidata point falls in, else on the nearest one
within 15 m. Entries whose article lacks a check string, or that land nowhere, are dropped and reported.
"""
import json
import time
from functools import cache

import geopandas as gpd
import requests
from pyproj import Transformer
from shapely.geometry import Point

from .city import CRS, UA
from .curated import CURATED

TO = Transformer.from_crs(4326, CRS, always_xy=True)


@cache
def article(ref):
    lang, title = ref.split(":", 1)
    for attempt in range(5):
        r = requests.get(f"https://{lang}.wikipedia.org/w/api.php", headers=UA, timeout=60, params={
            "action": "query", "prop": "extracts|info", "inprop": "url", "explaintext": 1, "redirects": 1,
            "format": "json", "titles": title})
        if r.ok and r.headers.get("content-type", "").startswith("application/json"):
            page = next(iter(r.json()["query"]["pages"].values()))
            return (page.get("extract") or ""), page.get("fullurl")
        time.sleep(2 ** attempt)
    return "", None


@cache
def buildings():
    b = gpd.read_parquet("data/buildings.parquet", columns=["identificatie", "planning_list_id", "geometry"])
    return b


@cache
def listed():
    out = {}
    for k, nr in zip(buildings().identificatie, buildings().planning_list_id):
        if isinstance(nr, str) and nr.strip():
            out.setdefault(nr.strip().split(".")[0], set()).add(k)
    return out


@cache
def coords(qid):
    for attempt in range(5):
        r = requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json", headers=UA, timeout=60)
        if r.ok:
            claims = r.json()["entities"][qid]["claims"]
            v = claims.get("P625", [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value")
            return (v["longitude"], v["latitude"]) if v else None
        time.sleep(2 ** attempt)
    return None


def place_point(lon, lat, within=15):
    pt = Point(TO.transform(lon, lat))
    b = buildings()
    hit = b[b.contains(pt)]
    if hit.empty:
        d = b.distance(pt)
        hit = b[d == d.min()] if d.min() < within else hit
    return list(hit.identificatie), "point"


def place(qid, nhle, within=15):
    if nhle and listed().get(str(nhle)):
        return sorted(listed()[str(nhle)]), "listing"
    c = coords(qid)
    if not c:
        return [], "no coordinates"
    return place_point(*c, within)


# Works OpenStreetMap still maps but articles say are gone: painted over or removed.
GONE = {"One Nation Under CCTV", "Lie Lie Land", "Pulp Fiction", "Very little helps", "Phone tap", "Freedom for Humanity"}


def osm_streetart(taken):
    """Murals and graffiti mapped on OpenStreetMap (ODbL), pinned to the building whose wall carries them."""
    d = json.load(open("data/raw/streetart/osm_streetart.json"))
    out = []
    for el in d.get("elements", []):
        tags = el.get("tags", {})
        name = tags.get("name") or tags.get("artwork_type", "mural").replace("_", " ").capitalize()
        if any(g.lower() in name.lower() for g in GONE):
            continue
        lon, lat = (el["lon"], el["lat"]) if "lon" in el else (el.get("center", {}).get("lon"), el.get("center", {}).get("lat"))
        if lon is None:
            continue
        bags, _ = place_point(lon, lat, 10)
        artist = tags.get("artist_name") or tags.get("artist")
        story = f"{name}{', by ' + artist if artist else ''}{', ' + tags['start_date'] if tags.get('start_date') else ''}."
        url = f"https://www.openstreetmap.org/{el['type']}/{el['id']}"
        out += [dict(name=name, qid=None, bag=b, story=story, source=url, how="osm", group="mapped") for b in bags
                if b not in taken]
    return out


def main():
    out, dropped = [], []
    for L in CURATED:
        entries = []
        for e in L["entries"]:
            if isinstance(e, dict):  # placed by its own coordinates (street art on a wall)
                name, qid, story, ref, checks, nhle, group = (e["name"], e.get("qid"), e["story"], e["ref"], e["checks"],
                                                              None, [e.get("group")])
                bags, how = place_point(e["lon"], e["lat"], 30)
            else:
                name, qid, story, ref, checks, nhle, *group = e
                # an estate's point often lies in its open ground: the nearest of its blocks within 60 m stands for it
                bags, how = place(qid, nhle, 60 if "Estate" in name or L["id"] == "housing" else 15)
            text, url = article(ref)
            missing = [c for c in checks if c not in text]
            if missing or not bags:
                dropped.append((L["id"], name, missing, how))
                continue
            for bag in bags:
                entries.append(dict(name=name, qid=qid, bag=bag, story=story, source=url, how=how,
                                    group=group[0] if group and group[0] else L["id"]))
        if L["id"] == "streetart":
            entries += osm_streetart({e["bag"] for e in entries})
        out.append(dict({k: v for k, v in L.items() if k != "entries"}, entries=entries))
        print(f'{L["id"]:10s} {len({e["name"] for e in entries})}/{len(L["entries"])}  ({len(entries)} footprints)')
    for d in dropped:
        print("dropped:", d)
    json.dump(out, open("data/curated.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
