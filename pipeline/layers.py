"""Layers: historical contexts, each a set of buildings.

A layer has one or more groups; every group takes one bit of a 64-bit mask per building.
Each source function returns {building id: group}, {building id: (group, note)} or a list of those per building.
Hand-written layers live in curated.py and are checked against Wikipedia by s08_curated.py before they get here.
"""
import json
import os
from functools import cache

import geopandas as gpd

LAYERS = []


def layer(**meta):
    def wrap(fn):
        LAYERS.append(dict(meta, source_fn=fn))
        return fn
    return wrap


@cache
def buildings() -> gpd.GeoDataFrame:
    b = gpd.read_parquet("data/buildings.parquet",
                         columns=["identificatie", "year", "planning_list_id", "planning_list_grade", "geometry"])
    b["bag"] = b.identificatie
    return b


# ---------- layers ----------

@layer(
    id="heritage", section="Architecture", title="Listed buildings", era="All periods",
    text=("Buildings on the National Heritage List for England. Grade I marks exceptional interest, Grade II* "
          "particularly important buildings, Grade II the rest that are of special interest."),
    caveat="Matched through Colouring London; a listing can cover a whole terrace or a single lamp post's house.",
    source=("Historic England, via Colouring London", "https://historicengland.org.uk/listing/the-list/"),
    groups=[("I", "Grade I"), ("II*", "Grade II*"), ("II", "Grade II")],
)
def heritage():
    b = buildings()
    g = b.planning_list_grade.fillna("").str.strip().str.upper()
    return {k: v for k, v in zip(b.bag, g) if v in ("I", "II*", "II")}


# Layers whose groups get colours of their own; the others are one colour, as 64 bits do not cover every group.
GROUPED = {"blitz", "world", "world-europe", "eastend", "potter", "streetart", "power", "modern"}
GROUP_LABELS = {"mapped": "Mapped on OpenStreetMap"}


def _curated_layer(L):
    if L["id"] not in GROUPED:
        L = dict(L, groups=None, entries=[dict(e, group=L["id"]) for e in L["entries"]])
    # a layer's groups are the group keys of its entries, in order of first appearance
    keys = list(dict.fromkeys(e["group"] for e in L["entries"]))
    groups = L.get("groups") or [(k, GROUP_LABELS.get(k, k[:1].upper() + k[1:]) if k != L["id"] else L["title"])
                                 for k in keys]

    def fn():
        out = {}
        for e in L["entries"]:
            out.setdefault(e["bag"], []).append((e["group"], {"story": e["story"], "source": e["source"], "name": e["name"]}))
        return out

    LAYERS.append(dict(id=L["id"], section=L.get("section", "Discover"), title=L["title"], era=L["era"], text=L["intro"],
                       caveat=L.get("caveat"), source=("Wikipedia, per building", "https://www.wikipedia.org"),
                       groups=[tuple(g) for g in groups], source_fn=fn))


if os.path.exists("data/curated.json"):
    for _L in json.load(open("data/curated.json")):
        _curated_layer(_L)


@layer(
    id="map1890s", section="Discover", title="On the 1890s map", era="1891–1896",
    text=("In the 1890s the Ordnance Survey mapped London at five feet to the mile, every building drawn. Where a "
          "footprint today is covered by buildings of that map, something already stood on this spot then."),
    caveat=("Map evidence, not a year: many buildings were rebuilt on the plan of the one before. Footprints from the "
            "map were traced by a neural network (97 % precision)."),
    source=("Petitpierre, McDonough, Fleet et al., A Layer of Late Victorian London (CC BY 4.0)",
            "https://doi.org/10.5281/zenodo.21282700"),
    groups=[("stood", "A building stood here in the 1890s")],
)
def map1890s():
    import pandas as pd
    m = pd.read_parquet("data/map1890s.parquet")
    return {k: "stood" for k, s in zip(m.identificatie, m.share1890s) if s >= 0.6}
