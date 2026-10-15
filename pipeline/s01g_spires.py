"""Towers, spires and domes above the LIDAR prisms (data/spires.parquet).

Each building is drawn as one prism at its LIDAR height, which flattens a church to its nave and cuts
St Paul's below its dome. For listed, named and religious buildings the Environment Agency surface model (DSM, 1 m, OGL; s00_fetch_lidar)
is read inside the footprint over the terrain model (DTM); every cell more than SPIRE_MIN above the prism becomes
a 1 m square at its height. The viewer raises walls under these squares, so a tower reads as a stack of fine
columns, the way a point cloud does. The margin keeps chimney stacks out."""
import glob
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
import rasterio.windows
import shapely
from shapely.geometry import box

LIDAR = Path("data/raw/lidar")
SPIRE_MIN = 8.0     # metres above the prism
TALL_MIN = 12.0     # metres: shorter buildings are left as they are
TOP_MIN = 35.0      # the first-return surface includes tree crowns, up to about 30 m in London: below this only
TOP_MIN_TOWER = 25.0  # churches and buildings named for a tower count
SHARE_MAX = 0.35    # tall cells over more of a footprint mean another, taller building stands over or beside it
WORSHIP = {"church", "cathedral", "chapel", "religious", "mosque", "synagogue", "temple"}
TOWERISH = r"(?i)\b(church|chapel|cathedral|abbey|tower|steeple|monument|st\.? |saint )"


def cells(kind, geom):
    """(x, y, value) of the 1 m cells of `kind` (dsm/dtm) whose centre lies in geom."""
    x0, y0, x1, y1 = geom.bounds
    out = []
    for tx in range(int(x0 // 1000) * 1000, int(x1 // 1000) * 1000 + 1000, 1000):
        for ty in range(int(y0 // 1000) * 1000, int(y1 // 1000) * 1000 + 1000, 1000):
            f = LIDAR / kind / f"{tx}_{ty}.tif"
            if not f.exists():
                continue
            with rasterio.open(f) as src:
                win = rasterio.windows.from_bounds(max(x0, tx), max(y0, ty), min(x1, tx + 1000), min(y1, ty + 1000),
                                                   src.transform).round_offsets().round_lengths()
                a = src.read(1, window=win, boundless=True, fill_value=np.nan).astype(float)
                tf = src.window_transform(win)
                nod = src.nodata
            if nod is not None:
                a[a == nod] = np.nan
            a[a < -100] = np.nan
            for i, j in zip(*np.where(np.isfinite(a))):
                cx, cy = tf * (j + 0.5, i + 0.5)
                out.append((cx, cy, a[i, j]))
    if not out:
        return pd.DataFrame(columns=["x", "y", "v"])
    d = pd.DataFrame(out, columns=["x", "y", "v"])
    return d[shapely.contains_xy(geom, d.x.values, d.y.values)]


def main():
    b = gpd.read_parquet("data/buildings.parquet",
                         columns=["identificatie", "height", "planning_list_id", "class", "name", "geometry"])
    # listed, a place of worship, or named (the landmarks: St Paul's and the Abbey carry no listing link here)
    tower = b["class"].isin(WORSHIP) | b.name.fillna("").str.contains(TOWERISH)
    cand = b[(b.planning_list_id.notna() | tower | b.name.notna()) & (b.height > TALL_MIN)]
    cand = cand.assign(tower=tower[cand.index])
    print(len(cand), "candidates")
    rows = []
    for r in cand.itertuples():
        g = shapely.make_valid(r.geometry)
        s, t = cells("dsm", g), cells("dtm", g)
        if s.empty or t.empty:
            continue
        m = s.merge(t, on=["x", "y"], suffixes=("_s", "_t"))
        m["rel"] = m.v_s - m.v_t
        hi = m[m.rel > r.height + SPIRE_MIN]
        if len(hi) < 2:   # one stray cell is a bird, a mast or noise
            continue
        if hi.rel.max() < (TOP_MIN_TOWER if r.tower else TOP_MIN) or len(hi) > SHARE_MAX * len(m):
            continue
        squares = [shapely.force_3d(box(x - 0.5, y - 0.5, x + 0.5, y + 0.5), round(float(h), 1))
                   for x, y, h in zip(hi.x, hi.y, hi.rel)]
        rows.append((r.identificatie, shapely.MultiPolygon(squares), float(r.height), float(hi.rel.max())))
    sp = gpd.GeoDataFrame(pd.DataFrame(rows, columns=["identificatie", "geometry", "prism", "top"]),
                          geometry="geometry", crs=27700)
    sp.to_parquet("data/spires.parquet")
    for r in sp.sort_values("top", ascending=False).head(15).itertuples():
        print(f"{r.identificatie}  prism {r.prism:5.1f} m  ->  {r.top:5.1f} m  ({len(r.geometry.geoms)} cells)")
    print(len(sp), "buildings get towers, spires or domes")


if __name__ == "__main__":
    main()
