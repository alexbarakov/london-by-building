"""Wikidata items in the area that are listed (P1216, National Heritage List for England) or have an English
Wikipedia article, with
labels, images, articles, architects and styles (CC0). s06_wiki places them on footprints."""
import csv
import io
import time
from pathlib import Path

import requests

from .city import UA

WD = "https://query.wikidata.org/sparql"
# the area's box, queried in cells so each query stays under the service's time limit
WEST, SOUTH, EAST, NORTH = -0.2290, 51.4108, 0.0095, 51.5780
NX, NY = 8, 6
Q = """SELECT ?i (SAMPLE(?c0) AS ?coord) (SAMPLE(?nhle0) AS ?nhle) ?labelEn (SAMPLE(?image0) AS ?image) ?en
 (SAMPLE(?inc0) AS ?inception) (SAMPLE(?end0) AS ?ended)
 (GROUP_CONCAT(DISTINCT ?archLabel; separator="|") AS ?architects) (GROUP_CONCAT(DISTINCT ?styleLabel; separator="|") AS ?styles) WHERE {{
 SERVICE wikibase:box {{ ?i wdt:P625 ?c0 . bd:serviceParam wikibase:cornerSouthWest "{SW}"^^geo:wktLiteral .
                                          bd:serviceParam wikibase:cornerNorthEast "{NE}"^^geo:wktLiteral . }}
 {{ ?i wdt:P1216 [] }} UNION {{ ?en0 schema:about ?i ; schema:isPartOf <https://en.wikipedia.org/> }}
 OPTIONAL {{ ?i wdt:P1216 ?nhle0 }} OPTIONAL {{ ?i wdt:P571 ?inc0 }} OPTIONAL {{ ?i wdt:P576 ?end0 }}
 OPTIONAL {{ ?i rdfs:label ?labelEn FILTER(lang(?labelEn)="en") }}
 OPTIONAL {{ ?i wdt:P18 ?image0 }}
 OPTIONAL {{ ?en schema:about ?i ; schema:isPartOf <https://en.wikipedia.org/> }}
 OPTIONAL {{ ?i wdt:P84 ?a . ?a rdfs:label ?archLabel FILTER(lang(?archLabel)="en") }}
 OPTIONAL {{ ?i wdt:P149 ?s . ?s rdfs:label ?styleLabel FILTER(lang(?styleLabel)="en") }}
}} GROUP BY ?i ?labelEn ?en"""


def cell(i, j):
    w, e = WEST + (EAST - WEST) * i / NX, WEST + (EAST - WEST) * (i + 1) / NX
    s, n = SOUTH + (NORTH - SOUTH) * j / NY, SOUTH + (NORTH - SOUTH) * (j + 1) / NY
    q = Q.format(SW=f"Point({w} {s})", NE=f"Point({e} {n})")
    for attempt in range(4):
        r = requests.post(WD, data={"query": q}, headers={"Accept": "text/csv", **UA}, timeout=300)
        if r.ok:
            return list(csv.DictReader(io.StringIO(r.text)))
        time.sleep(10 * (attempt + 1))
    print("cell failed", i, j, r.status_code)
    return []


def main():
    rows, seen = [], set()
    for i in range(NX):
        for j in range(NY):
            for r in cell(i, j):
                if r["i"] not in seen:
                    seen.add(r["i"]); rows.append(r)
    with open("data/raw/wd_buildings.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
    print(len(rows), "items;", sum(bool(x["nhle"]) for x in rows), "listed;", sum(bool(x["en"]) for x in rows),
          "with an article;", sum(bool(x["image"]) for x in rows), "with a photo")


if __name__ == "__main__":
    main()
