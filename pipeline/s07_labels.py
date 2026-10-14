"""Street, river and canal names, placed along their own outlines.

Source: Overture Maps roads and water (OpenStreetMap, ODbL), fetched to data/raw/overture_roads.parquet and
overture_water.parquet. A street line is widened by its class into a band; water keeps its own outline. Each outline
is cut into 300 m cells; every piece longer than it is wide gets one label at its centre, turned along its long
side. Tier 1 (the river, canals and main roads) shows from afar, tier 2 only up close.
"""
import json
import math
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import shapely
from shapely.geometry import box

from .city import CRS
from .s03_tiles import DAM

CELL = 300.0
WIDTH = {"motorway": 24, "trunk": 22, "primary": 18, "secondary": 14, "tertiary": 11, "unclassified": 9,
         "residential": 9, "living_street": 7, "pedestrian": 8}
TIER1_CLASSES = {"motorway", "trunk", "primary"}
TIER1 = {"River Thames", "Regent's Canal", "Grand Union Canal", "Oxford Street", "Regent Street", "Strand", "Whitehall",
         "The Mall", "Piccadilly", "Fleet Street", "Kingsway", "Euston Road", "City Road", "Victoria Embankment",
         "Albert Embankment", "Chelsea Embankment", "Pall Mall", "Charing Cross Road", "Shaftesbury Avenue",
         "Tottenham Court Road", "Baker Street", "Park Lane", "Kensington High Street", "King's Road", "Brick Lane",
         "Whitechapel Road", "Commercial Road", "Bishopsgate", "Cheapside", "Upper Street", "Kingsland Road",
         "Borough High Street", "Old Kent Road", "Brixton Road", "Westminster Bridge", "London Bridge", "Tower Bridge"}


def outlines():
    """(name, is water, tier-1 class, polygon) for every named road segment and water body."""
    r = pd.read_parquet("data/raw/overture_roads.parquet")
    r = gpd.GeoDataFrame(r.drop(columns="geometry"), geometry=gpd.GeoSeries.from_wkb(r.geometry), crs=4326).to_crs(CRS)
    for name, cls, g in zip(r.name, r["class"], r.geometry):
        if cls in WIDTH:
            yield name, False, cls in TIER1_CLASSES, g.buffer(WIDTH[cls] / 2, cap_style="flat")
    w = pd.read_parquet("data/raw/overture_water.parquet")
    w = w[w.name.notna()]
    w = gpd.GeoDataFrame(w.drop(columns="geometry"), geometry=gpd.GeoSeries.from_wkb(w.geometry), crs=4326).to_crs(CRS)
    for name, g in zip(w.name, w.geometry):
        if g.geom_type in ("Polygon", "MultiPolygon"):
            yield name, True, True, g
        elif g.geom_type in ("LineString", "MultiLineString"):
            yield name, True, True, g.buffer(6, cap_style="flat")


def pieces(geom):
    x0, y0, x1, y1 = geom.bounds
    for cx in np.arange(math.floor(x0 / CELL) * CELL, x1, CELL):
        for cy in np.arange(math.floor(y0 / CELL) * CELL, y1, CELL):
            part = geom.intersection(box(cx, cy, cx + CELL, cy + CELL))
            for p in getattr(part, "geoms", [part]):
                if p.geom_type == "Polygon" and p.area > 200:
                    yield p


def placement(p):
    """Centre and angle (degrees, local frame) of a piece, or None if it is not elongated."""
    r = p.minimum_rotated_rectangle
    c = np.array(r.exterior.coords)[:4]
    e1, e2 = c[1] - c[0], c[2] - c[1]
    long, short = (e1, e2) if np.hypot(*e1) >= np.hypot(*e2) else (e2, e1)
    if np.hypot(*long) < 2.2 * np.hypot(*short) or np.hypot(*long) < 60:
        return None
    pt = p.representative_point() if not p.contains(p.centroid) else p.centroid
    ang = math.degrees(math.atan2(-long[1], long[0]))  # local z points south
    ang = (ang + 90) % 180 - 90  # keep text upright
    # The piece's width: area over length is the street's mean width, steadier than the rectangle's short side.
    width = p.area / max(np.hypot(*long), 1)
    return [round(pt.x - DAM[0], 1), round(-(pt.y - DAM[1]), 1), round(ang, 1), round(float(np.hypot(*long))),
            round(float(width), 1)]


def main():
    by_name = {}
    for name, water, main, g in outlines():
        w, m, gs = by_name.setdefault(name, [False, False, []])
        gs.append(shapely.make_valid(g))
        by_name[name] = [w or water, m or main, gs]
    area = gpd.read_file("data/raw/boundary.json").set_crs(CRS, allow_override=True).union_all().buffer(200)
    labels = []
    for name, (water, main, gs) in by_name.items():
        geom = shapely.union_all(gs).intersection(area)
        if geom.is_empty:
            continue
        pts = [pl for p in pieces(geom) if (pl := placement(p))]
        if pts:
            labels.append(dict(name=name, water=water, tier=1 if (main or name in TIER1) else 2, pts=pts))
    # One entry per name: a canal is registered both as water and as the street along it; keep the water.
    merged = {}
    for l in sorted(labels, key=lambda l: not l["water"]):
        m = merged.setdefault(l["name"], dict(l, pts=[]))
        m["pts"] += l["pts"]
    labels = []
    for m in merged.values():
        # Keep placements at least 350 m apart, longest stretches first.
        kept = []
        for p in sorted(m["pts"], key=lambda p: -p[3]):
            if all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 > 350 ** 2 for q in kept):
                kept.append(p)
        m["pts"] = kept
        labels.append(m)
    Path("web/data/labels.json").write_text(json.dumps(labels, ensure_ascii=False, separators=(",", ":")))
    print(len(labels), "names,", sum(len(l["pts"]) for l in labels), "placements,",
          sum(l["tier"] == 1 for l in labels), "tier 1;", Path("web/data/labels.json").stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
