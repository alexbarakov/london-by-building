"""Construction years, floors and heights per building (data/buildings.parquet).

Years come only from Colouring London contributors (see s01_load); nothing is estimated. A year with a range
(most come from comparing historical maps: 'built between the 1890s and the 1910s map') is drawn paler and
marked 'c.'. A building with no known year gets year 0 and its own grey; it stays out of the timeline.
"""
import geopandas as gpd
import numpy as np
import pandas as pd

from .periods import period_index

FLAG_EXACT, FLAG_RANGE, FLAG_UNKNOWN = 0, 1, 7
STOREY_M = 3.2


def main():
    p = gpd.read_parquet("data/panden.parquet")
    lo = pd.to_numeric(p.date_lower, errors="coerce")
    hi = pd.to_numeric(p.date_upper, errors="coerce")
    y = pd.to_numeric(p.y, errors="coerce")
    p["year"] = y.fillna(0).round().astype(int)
    p["year_lo"], p["year_hi"] = lo.fillna(0).astype(int), hi.fillna(0).astype(int)
    ranged = (hi - lo).fillna(0) > 2
    p["date_flag"] = np.where(p.year == 0, FLAG_UNKNOWN, np.where(ranged, FLAG_RANGE, FLAG_EXACT)).astype(np.uint8)
    p["period"] = p.year.map(period_index).astype(np.uint8)
    p["floors"] = np.clip(np.round(p.height / STOREY_M), 1, 99).astype(np.uint8)
    p["floors_src"] = np.uint8(1)
    p = p.sort_values("identificatie").reset_index(drop=True)
    p.to_parquet("data/buildings.parquet")
    print({"buildings": len(p), "exact": int((p.date_flag == 0).sum()), "range": int((p.date_flag == 1).sum()),
           "unknown": int((p.date_flag == 7).sum())})
    print(p.groupby("period").size().to_dict())


if __name__ == "__main__":
    main()
