"""Ordnance Survey National Grid 1:1250 plans of the 1940s–70s as published by the National Library of Scotland
(georeferenced tiles, re-use CC BY, National Library of Scotland): edition A (surveyed 1940s–50s), B (revised
1950s–70s), C (revised 1960s–70s). Zoom 17 (about 1.2 m a pixel), only the tiles that hold our footprints,
cached in data/raw/osplans/{edition}/ so a rerun resumes. Sheet dates come from the NLS sheet indexes (WFS).
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import geopandas as gpd
import requests

from .city import UA

Z = 17
EDITIONS = {
    "A": "https://mapseries-tilesets.s3.amazonaws.com/london_1940s/{z}/{x}/{y}.png",
    "B": "https://geo.nls.uk/maps/os/1250_B_1eng/{z}/{x}/{y}.png",
    "C": "https://geo.nls.uk/maps/os/1250_C/{z}/{x}/{y}.png",
}
OUT = Path("data/raw/osplans")


def tile_of(lon, lat, z=Z):
    n = 2 ** z
    return int((lon + 180) / 360 * n), int((1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n)


def tiles():
    b = gpd.read_parquet("data/buildings.parquet", columns=["geometry"]).to_crs(4326)
    out = set()
    for x0, y0, x1, y1 in b.bounds.itertuples(index=False):
        tx0, ty1 = tile_of(x0, y0)
        tx1, ty0 = tile_of(x1, y1)
        for tx in range(tx0, tx1 + 1):
            for ty in range(ty0, ty1 + 1):
                out.add((tx, ty))
    return sorted(out)


def get(ed, x, y):
    f = OUT / ed / f"{x}_{y}.png"
    if f.exists():
        return
    for attempt in range(4):
        try:
            r = requests.get(EDITIONS[ed].format(z=Z, x=x, y=y), headers=UA, timeout=60)
        except requests.RequestException:
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code == 200 and r.headers.get("content-type", "").startswith("image"):
            f.write_bytes(r.content)
            break
        if r.status_code in (403, 404):
            f.write_bytes(b"")  # no sheet here
            break
        time.sleep(5 * (attempt + 1))
    time.sleep(0.4)  # a polite pace: about 10 tiles a second over four threads


def main():
    ts = tiles()
    print(len(ts), "tiles per edition")
    for ed in EDITIONS:
        (OUT / ed).mkdir(parents=True, exist_ok=True)
        with ThreadPoolExecutor(4) as ex:
            list(ex.map(lambda t: get(ed, *t), ts))
        print(ed, "done", flush=True)


if __name__ == "__main__":
    main()
