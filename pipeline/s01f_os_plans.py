"""Was each footprint already built on the OS 1:1250 plans of the 1940s–70s? (data/osplans.parquet)

On these plans buildings are grey-shaded on cream paper. For every footprint (shrunk by a metre so walls of the
neighbours do not count) and every edition, the share of its pixels that are shaded against those that are paper:
over 0.6 reads as built, under 0.25 as not yet built, between as unclear. The shading tone differs from sheet to
sheet, so the paper and shade levels are found per tile. Each footprint also gets the survey or revision year of the
sheet it lies on, from the NLS sheet indexes.

s02_attributes turns this into a bracket for buildings no other source dates: not on a plan of year X and on the
next of year Y means built between X and Y; on the 1890s map's footprints and on none of the plans means rebuilt.
"""
import io
import math
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
from PIL import Image
from rasterio.features import rasterize
from rasterio.transform import from_bounds

from .city import CRS
from .s00_fetch_os_plans import EDITIONS, OUT, Z

R = 6378137 * math.pi


def tile_bounds(x, y, z=Z):
    ts = 2 * R / 2 ** z
    return (-R + x * ts, R - (y + 1) * ts, -R + (x + 1) * ts, R - y * ts)


def sheet_years(b, ed):
    f = OUT / f"nls_sheetindex_National_Grid_WFS_1250{'' if ed == 'A' else '_' + ed}.geojson"
    s = gpd.read_file(f).set_crs(CRS, allow_override=True)
    s["year"] = pd.to_numeric(s.REV_STA.where(s.REV_STA.astype(bool), s.SUR_STA), errors="coerce")
    s = s.sort_values("year").drop_duplicates("SHEET_NO", keep="last")  # one plan per sheet and edition
    pts = gpd.GeoDataFrame({"identificatie": b.identificatie}, geometry=b.geometry.representative_point(), crs=CRS)
    j = gpd.sjoin(pts, s[["year", "geometry"]], predicate="within").drop_duplicates("identificatie")
    return b.identificatie.map(j.set_index("identificatie").year)


def main():
    b = gpd.read_parquet("data/buildings.parquet", columns=["identificatie", "geometry"])
    inner = b.geometry.buffer(-1.0)
    inner = inner.where(~inner.is_empty & (inner.area > 4), b.geometry)
    g = gpd.GeoSeries(inner, crs=CRS).to_crs(3857)
    sidx = g.sindex
    out = pd.DataFrame({"identificatie": b.identificatie})
    for ed in EDITIONS:
        grey = np.zeros(len(b) + 1)
        paper = np.zeros(len(b) + 1)
        files = sorted((OUT / ed).glob("*.png"))
        for f in files:
            if f.stat().st_size == 0:
                continue
            x, y = map(int, f.stem.split("_"))
            bounds = tile_bounds(x, y)
            hit = sidx.query(shapely.box(*bounds), predicate="intersects")
            if not len(hit):
                continue
            a = np.asarray(Image.open(io.BytesIO(f.read_bytes())).convert("RGBA")).astype(int)
            alpha = a[..., 3] > 200
            rgb = a[..., :3]
            lum, spread = rgb.mean(2), rgb.max(2) - rgb.min(2)
            v = lum[alpha & (lum > 150)]
            if v.size < 2000:
                continue
            thr = np.percentile(v, 90) - 7  # paper is the brightest common tone of the tile
            shade = alpha & (spread < 30) & (lum > 150) & (lum < thr - 2)
            paperm = alpha & (lum > thr + 2)
            lab = rasterize(zip(g.values[hit], hit + 1), out_shape=lum.shape, transform=from_bounds(*bounds, *lum.shape[::-1]),
                            fill=0, dtype="int32")
            idx = lab.ravel()
            grey += np.bincount(idx, weights=shade.ravel(), minlength=len(b) + 1)
            paper += np.bincount(idx, weights=paperm.ravel(), minlength=len(b) + 1)
        n = (grey + paper)[1:]
        out[f"fill_{ed}"] = np.where(n >= 6, grey[1:] / np.maximum(n, 1), np.nan)
        out[f"year_{ed}"] = sheet_years(b, ed).values
        print(ed, len(files), "tiles;", f"read {np.isfinite(out[f'fill_{ed}']).mean():.0%} of footprints;",
              f"built {(out[f'fill_{ed}'] > 0.6).mean():.0%}, not yet {(out[f'fill_{ed}'] < 0.25).mean():.0%}")
    out.to_parquet("data/osplans.parquet")


if __name__ == "__main__":
    main()
