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


def place(qid, nhle):
    if nhle and listed().get(str(nhle)):
        return sorted(listed()[str(nhle)]), "listing"
    c = coords(qid)
    if not c:
        return [], "no coordinates"
    pt = Point(TO.transform(*c))
    b = buildings()
    hit = b[b.contains(pt)]
    if hit.empty:
        d = b.distance(pt)
        hit = b[d == d.min()] if d.min() < 15 else hit
    return list(hit.identificatie), "point"


def main():
    out, dropped = [], []
    for L in CURATED:
        entries = []
        for name, qid, story, ref, checks, nhle, *group in L["entries"]:
            text, url = article(ref)
            missing = [c for c in checks if c not in text]
            bags, how = place(qid, nhle)
            if missing or not bags:
                dropped.append((L["id"], name, missing, how))
                continue
            for bag in bags:
                entries.append(dict(name=name, qid=qid, bag=bag, story=story, source=url, how=how,
                                    group=group[0] if group and group[0] else L["id"]))
        out.append(dict({k: v for k, v in L.items() if k != "entries"}, entries=entries))
        print(f'{L["id"]:10s} {len({e["name"] for e in entries})}/{len(L["entries"])}  ({len(entries)} footprints)')
    for d in dropped:
        print("dropped:", d)
    json.dump(out, open("data/curated.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
