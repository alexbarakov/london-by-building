"""Environment Agency LIDAR composite, 1 m (Open Government Licence): surface (DSM, first return) and terrain (DTM)
for every 1 km square of the area, from the EA's WCS. Building heights are the surface over the terrain."""
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import geopandas as gpd
import requests
from shapely.geometry import box

BASE = "https://environment.data.gov.uk/spatialdata"
LAYERS = {
    "dsm": ("lidar-composite-digital-surface-model-first-return-dsm-1m",
            "df4e3ec3-315e-48aa-aaaf-b5ae74d7b2bb__Lidar_Composite_Elevation_FZ_DSM_1m"),
    "dtm": ("lidar-composite-digital-terrain-model-dtm-1m",
            "13787b9a-26a4-4775-8523-806d13af58fc__Lidar_Composite_Elevation_DTM_1m"),
}
OUT = Path("data/raw/lidar")


def squares():
    area = gpd.read_file("data/raw/boundary.json").set_crs(27700, allow_override=True).union_all()
    x0, y0, x1, y1 = (int(v // 1000) * 1000 for v in area.bounds)
    return [(x, y) for x in range(x0, x1 + 1000, 1000) for y in range(y0, y1 + 1000, 1000)
            if box(x, y, x + 1000, y + 1000).intersects(area)]


def fetch(kind, x, y):
    f = OUT / kind / f"{x}_{y}.tif"
    if f.exists() and f.stat().st_size > 100000:
        return
    svc, cov = LAYERS[kind]
    for attempt in range(4):
        r = requests.get(f"{BASE}/{svc}/wcs", timeout=180, params=[
            ("service", "WCS"), ("version", "2.0.1"), ("request", "GetCoverage"), ("CoverageId", cov),
            ("format", "image/tiff"), ("subset", f"E({x},{x + 1000})"), ("subset", f"N({y},{y + 1000})")])
        if r.ok and r.content[:2] in (b"MM", b"II"):
            f.write_bytes(r.content)
            return
    print("failed", kind, x, y, r.status_code)


def main():
    sq = squares()
    for kind in LAYERS:
        (OUT / kind).mkdir(parents=True, exist_ok=True)
    jobs = [(k, x, y) for k in LAYERS for x, y in sq]
    with ThreadPoolExecutor(6) as ex:
        list(ex.map(lambda j: fetch(*j), jobs))
    print(len(sq), "squares")


if __name__ == "__main__":
    main()
