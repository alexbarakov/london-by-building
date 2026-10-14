"""Which footprints were already on the Ordnance Survey 1:1,056 map of 1891–1896.

Source: 'A Layer of Late Victorian London' (Petitpierre, McDonough, Fleet et al., Zenodo 10.5281/zenodo.21282700,
CC BY 4.0): building footprints extracted from the map sheets. A footprint today counts as on the 1890s map when
buildings of that map cover at least 60 % of it. That is map evidence, not a year: the house may have been rebuilt
on the same plan since. Writes data/map1890s.parquet (id, share covered).
"""
import geopandas as gpd
import numpy as np
import pandas as pd
import pyogrio
import shapely

from .city import CRS

COVER = 0.6


def main():
    b = gpd.read_parquet("data/buildings.parquet", columns=["identificatie", "geometry"])
    box = b.to_crs(3857).total_bounds
    old = pyogrio.read_dataframe("data/raw/london_1891.gpkg", bbox=tuple(box)).to_crs(CRS)
    old["geometry"] = shapely.make_valid(old.geometry.values)
    sidx = old.sindex
    geom = shapely.make_valid(b.geometry.values)
    share = np.zeros(len(b))
    left, right = sidx.query(geom, predicate="intersects")
    inter = shapely.area(shapely.intersection(geom[left], old.geometry.values[right]))
    s = pd.Series(inter).groupby(left).sum()
    share[s.index] = np.minimum(1.0, s.values / shapely.area(geom[s.index]))
    out = pd.DataFrame({"identificatie": b.identificatie, "share1890s": share.round(2)})
    out.to_parquet("data/map1890s.parquet")
    print(f"{len(old)} buildings on the 1890s map in the area; {(share >= COVER).sum()} of {len(b)} footprints today "
          f"stand on them (≥{COVER:.0%} covered)")


if __name__ == "__main__":
    main()
