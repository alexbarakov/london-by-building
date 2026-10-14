"""Building heights from the Environment Agency LIDAR (OGL): within each footprint, the 70th percentile of the
surface (DSM) over the median terrain (DTM) of a ring just outside it. The same percentile 3D BAG uses for its
LoD 1.3 roofs, so towers and spires do not lift a whole block.

A footprint crossing two 1 km squares takes the square that holds most of it. Footprints with fewer than four
LIDAR cells or no data keep the height OpenStreetMap gives, else three metres a storey, else 6 m.
"""
from pathlib import Path

import geopandas as gpd
import numpy as np
import rasterio
import shapely
from rasterio.features import rasterize

LIDAR = Path("data/raw/lidar")


def per_label(lab, val, keep, q):
    """Quantile q of val per label, over the cells where keep is true."""
    g, v = lab[keep], val[keep]
    o = np.lexsort((v, g))
    g, v = g[o], v[o]
    ids, start, count = np.unique(g, return_index=True, return_counts=True)
    return ids, v[start + (count * q).astype(int).clip(max=count - 1)], count


def main():
    p = gpd.read_parquet("data/panden.parquet")
    n = len(p)
    gid = np.arange(n) + 1
    sidx = p.sindex
    rings = p.geometry.buffer(3).difference(p.geometry.buffer(0.5)).values
    best = np.zeros(n + 1, np.int32)
    roof = np.full(n + 1, np.nan, np.float32)
    ground = np.full(n + 1, np.nan, np.float32)
    for f in sorted((LIDAR / "dsm").glob("*.tif")):
        with rasterio.open(f) as ds, rasterio.open(LIDAR / "dtm" / f.name) as dt:
            dsm, dtm, nod, tr = ds.read(1), dt.read(1), ds.nodata, ds.transform
            hit = sidx.query(shapely.box(*ds.bounds), predicate="intersects")
        if not len(hit):
            continue
        lab = rasterize(zip(p.geometry.values[hit], gid[hit]), out_shape=dsm.shape, transform=tr, fill=0, dtype="int32")
        ring = rasterize(zip(rings[hit], gid[hit]), out_shape=dsm.shape, transform=tr, fill=0, dtype="int32")
        ids, p70, count = per_label(lab, dsm, (lab > 0) & (dsm != nod) & np.isfinite(dsm) & (dsm > -100), 0.7)
        tids, tmed, _ = per_label(ring, dtm, (ring > 0) & (lab == 0) & np.isfinite(dtm) & (dtm > -100), 0.5)
        better = count > best[ids]
        roof[ids[better]], best[ids[better]] = p70[better], count[better]
        won = set(ids[better].tolist())
        sel = np.array([t in won or np.isnan(ground[t]) for t in tids], bool) if len(tids) else np.zeros(0, bool)
        ground[tids[sel]] = tmed[sel]
    h = (roof - ground)[1:]
    ok = (best[1:] >= 4) & np.isfinite(h) & (h > 1.5) & (h < 330)
    osm = p.height.where(p.height.notna(), p.num_floors * 3.0)
    p["height_src"] = np.where(ok, "lidar", np.where(osm.notna(), "osm", "estimate"))
    p["height"] = np.where(ok, h, osm.fillna(6.0))
    p.to_parquet("data/panden.parquet")
    print(f"LIDAR heights for {ok.sum()} of {n}; median {np.median(h[ok]):.1f} m; tallest {h[ok].max():.0f} m; "
          f"{p.height_src.value_counts().to_dict()}")


if __name__ == "__main__":
    main()
