"""Construction years, floors and heights per building (data/buildings.parquet).

Every year has a source; nothing is borrowed from neighbours. The first pass takes Colouring London contributors'
years (s01_load); once s01e_ages has gathered the other sources into data/ages.parquet, a second pass takes, for
each building, the first source in SOURCES that dates it. A year with a range (a century, an energy-certificate
band, a bracket between two maps) is drawn paler and marked 'c.' with the range. A building with no year gets
year 0 and its own grey; it stays out of the timeline.
"""
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd

from .periods import period_index

FLAG_EXACT, FLAG_RANGE, FLAG_UNKNOWN = 0, 1, 7
# most precise first; the index is the source code the viewer reads
SOURCES = ["", "colouring", "nhle", "wikidata", "osm", "ldd", "pricepaid", "locallist", "era", "epc", "osmaps"]
STOREY_M = 3.2


def main():
    p = gpd.read_parquet("data/panden.parquet")
    lo = pd.to_numeric(p.date_lower, errors="coerce")
    hi = pd.to_numeric(p.date_upper, errors="coerce")
    y = pd.to_numeric(p.y, errors="coerce")
    p["year"] = y.fillna(0).round().astype(int)
    p["year_lo"], p["year_hi"] = lo.fillna(p.year).astype(int), hi.fillna(p.year).astype(int)
    p["year_src"] = np.where(p.year > 0, SOURCES.index("colouring"), 0)
    ages = Path("data/ages.parquet")
    if ages.exists():
        a = pd.read_parquet(ages)
        a["rank"] = a.src.map(SOURCES.index)
        a = a.sort_values(["identificatie", "rank", "hi"]).drop_duplicates("identificatie").set_index("identificatie")
        k = p.identificatie
        p["year"] = k.map(a.y).fillna(0).astype(int)
        p["year_lo"] = k.map(a.lo).fillna(0).astype(int)
        p["year_hi"] = k.map(a.hi).fillna(0).astype(int)
        p["year_src"] = k.map(a["rank"]).fillna(0).astype(int)
        lo, hi = p.year_lo.astype(float), p.year_hi.astype(float)
    ranged = (hi - lo).fillna(0) > 2
    p["date_flag"] = np.where(p.year == 0, FLAG_UNKNOWN, np.where(ranged, FLAG_RANGE, FLAG_EXACT)).astype(np.uint8)
    p["period"] = p.year.map(period_index).astype(np.uint8)
    p["floors"] = np.clip(np.round(p.height / STOREY_M), 1, 99).astype(np.uint8)
    p["floors_src"] = np.uint8(1)
    p = p.sort_values("identificatie").reset_index(drop=True)
    p.to_parquet("data/buildings.parquet")
    print(p[p.year > 0].year_src.map(lambda i: SOURCES[i]).value_counts().to_dict())
    print({"buildings": len(p), "exact": int((p.date_flag == 0).sum()), "range": int((p.date_flag == 1).sum()),
           "unknown": int((p.date_flag == 7).sum())})
    print(p.groupby("period").size().to_dict())


if __name__ == "__main__":
    main()
