"""List-entry descriptions of the listed buildings that still lack a year, which usually date the building
("C18", "1820-25", "c.1890"). Historic England publishes the National Heritage List for England under the Open
Government Licence, but serves no bulk text and blocks scripts; British Listed Buildings mirrors the entries and its
robots.txt allows the pages. One request a second, cached in data/raw/nhle_text/ so a rerun resumes.

Targets: entries linked to a footprint through Colouring London, and entries whose point (data/raw/nhle_points.csv,
from Historic England's open GIS layer) falls inside a footprint.
"""
import html
import re
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests

from .city import CRS, UA

OUT = Path("data/raw/nhle_text")


def targets():
    # footprints without a contributor's year in Colouring London (the merged years of buildings.parquet would
    # hide listed buildings dated only by an energy-certificate band)
    b = gpd.read_parquet("data/panden.parquet", columns=["identificatie", "y", "planning_list_id", "geometry"])
    b["year"] = b.y.fillna(0)
    ids = {str(x).split(".")[0] for x in b.loc[b.year == 0, "planning_list_id"].dropna()}
    pts = pd.read_csv("data/raw/nhle_points.csv")
    pts = gpd.GeoDataFrame(pts, geometry=gpd.points_from_xy(pts.Easting, pts.Northing), crs=CRS)
    j = gpd.sjoin(pts, b[b.year == 0][["geometry"]], predicate="within")
    return sorted(ids | {str(x) for x in j.ListEntry})


def fetch(nhle):
    r = requests.get(f"https://britishlistedbuildings.co.uk/10{nhle}", headers=UA, timeout=(10, 30))
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", r.text, flags=re.S)
    s = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    a, b = s.find(" Description "), s.find("Listing NGR")
    if b < 0:
        b = s.find("External Links")
    return r.status_code, (s[a + 13:b].strip() if a > 0 else "")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    todo = [n for n in targets() if not (OUT / f"{n}.txt").exists()]
    print(len(todo), "to fetch")
    codes = {}
    t0 = time.time()
    for i, n in enumerate(todo):
        try:
            code, text = fetch(n)
        except requests.RequestException as e:
            code, text = type(e).__name__, ""
        codes[code] = codes.get(code, 0) + 1
        if code == 200:
            (OUT / f"{n}.txt").write_text(text)
        elif code == 404:
            (OUT / f"{n}.txt").write_text("")  # not on the mirror; do not ask again
        elif code == 429:
            time.sleep(30)
        time.sleep(1.0)
        if i % 50 == 0:
            print(i, codes, f"{time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
