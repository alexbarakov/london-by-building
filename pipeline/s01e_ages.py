"""Every sourced date for every footprint, one row per (footprint, source): data/ages.parquet.

Sources, most precise first (s02_attributes takes the first that dates a building):
  colouring   Colouring London contributors' years (s01_load), ODbL
  nhle        the National Heritage List entry's description (s00_fetch_nhle_text), OGL, Historic England
  wikidata    inception (P571) of the Wikidata item an OpenStreetMap building is tagged with, CC0
  osm         OpenStreetMap start_date / building:start_date, ODbL
  ldd         London Development Database completions 2000–2019, schemes of 20+ homes whose site point lies in the
              footprint, OGL, GLA
  pricepaid   first sale of new-build homes in HM Land Registry Price Paid Data, where the footprint's addresses
              (ONS UPRN Directory) mostly sit in postcodes that were new-build when first sold, OGL
  locallist   Lambeth and Southwark local lists (s00_fetch_local_lists), OGL
  era         an era a Colouring London contributor chose ('Victorian (1837-1901)'), ODbL
  osmaps      brackets from the Ordnance Survey maps: the 1890s footprints (s01d_1890s) and the 1:1250 plans
              of the 1940s–70s (s01f_os_plans); see the rules below
  epc         (a band with no lower end, 'before 1900', is drawn from its last year)
              the construction age band of the homes in the footprint, from the GLA's London Building Stock Model 2
              (OGL), which takes it from energy certificates; only bands marked known, and only when at least 60 %
              of a footprint's homes agree. The 1900–1929 band is often given to Victorian houses: where the
              footprint was already built on the 1890s map, it reads as 'before 1900'.
The prepared inputs for ldd, pricepaid, osm and era sit in data/raw/ages/ (see the README).
"""
import json
import re
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd

from .city import CRS
from .dates import parse, parse_free

RAW = Path("data/raw")
BANDS = {"pre-1900": (1800, 1899), "1900-1929": (1900, 1929), "1930-1949": (1930, 1949), "1950-1966": (1950, 1966),
         "1967-1982": (1967, 1982), "1983-1995": (1983, 1995), "1996-2011": (1996, 2011), "2012 onwards": (2012, 2026),
         "2012-onwards": (2012, 2026), "2012+": (2012, 2026)}
ERA = re.compile(r"(1[6-9]\d\d|20\d\d)\s*-\s*(1[6-9]\d\d|20\d\d)")
LISTED_THINGS = re.compile(r"\b(railings?|lamp|bollard|kiosk|wall|gate piers?|post|pump|statue|memorial|drinking fountain|"
                           r"boundary|milestone|bench|telephone)\b", re.I)


def row(k, y, lo, hi, src):
    return dict(identificatie=f"{int(k):016d}" if not isinstance(k, str) else k, y=int(round(y)), lo=int(lo),
                hi=int(hi), src=src)


def main():
    # the footprints with Colouring London's own dates as s01_load joined them (buildings.parquet already carries
    # the merged years of an earlier run)
    b = gpd.read_parquet("data/panden.parquet", columns=["identificatie", "y", "date_lower", "date_upper",
                                                          "planning_list_id", "geometry"])
    rows = []
    # colouring
    for k, y, lo, hi in zip(b.identificatie, b.y.fillna(0).round().astype(int), b.date_lower, b.date_upper):
        if y > 1000:
            lo = int(lo) if pd.notna(pd.to_numeric(lo, errors="coerce")) else y
            hi = int(hi) if pd.notna(pd.to_numeric(hi, errors="coerce")) else y
            rows.append(row(k, y, lo, hi, "colouring"))
    # nhle: by the Colouring link, then by the entry's point inside a footprint
    texts = {p.stem: p.read_text() for p in (RAW / "nhle_text").glob("*.txt")}
    names = dict(zip(pd.read_csv(RAW / "nhle_points.csv").ListEntry.astype(str), pd.read_csv(RAW / "nhle_points.csv").Name))
    link = [(k, str(n).split(".")[0]) for k, n in zip(b.identificatie, b.planning_list_id) if pd.notna(n)]
    pts = pd.read_csv(RAW / "nhle_points.csv")
    pts = gpd.GeoDataFrame(pts, geometry=gpd.points_from_xy(pts.Easting, pts.Northing), crs=CRS)
    j = gpd.sjoin(pts, b[["identificatie", "geometry"]], predicate="within")
    link += [(k, str(n)) for k, n in zip(j.identificatie, j.ListEntry)]
    for k, n in dict.fromkeys(link):
        t = texts.get(n)
        if not t or LISTED_THINGS.search(str(names.get(n, ""))):
            continue
        p = parse(t)
        if p and 1000 < p[0] <= 2026:
            rows.append(row(k, *p[:3], "nhle"))
    # wikidata through OSM tags, and OSM start dates
    osm = pd.read_csv(RAW / "ages/osm_year0_candidates.csv")
    wd = pd.read_csv(RAW / "wd_buildings.csv", usecols=["i", "inception", "ended"])
    wd = wd[wd.ended.isna() & wd.inception.notna()]
    inc = {i.rsplit("/", 1)[1]: int(str(v)[:4]) for i, v in zip(wd.i, wd.inception) if str(v)[:4].isdigit()}
    for k, q in zip(osm.identificatie, osm.wd):
        if isinstance(q, str) and q in inc and 1000 < inc[q] <= 2026:
            rows.append(row(k, inc[q], inc[q], inc[q], "wikidata"))
    for k, y, precise in zip(osm.identificatie, osm.y, osm.precise):
        if pd.notna(y) and 1000 < y <= 2026:
            rows.append(row(k, y, y if precise else y - 5, y if precise else y + 5, "osm"))
    # new homes
    ldd = pd.read_csv(RAW / "ages/ldd_site_point_footprint_matches.csv")
    for k, y in zip(*ldd[(ldd.units >= 20) & (ldd.dist == 0)][["identificatie", "year"]].values.T):
        rows.append(row(k, y, y - 1, y, "ldd"))
    ppd = pd.read_csv(RAW / "ages/ppd_newbuild_footprint_candidates.csv")
    for k, y in zip(*ppd[ppd.conf == "high"][["identificatie", "ppd_first_sale_year"]].values.T):
        rows.append(row(k, y, y - 2, y, "pricepaid"))
    # local lists
    lam = gpd.read_file(RAW / "ages/lambeth_local_list.geojson").to_crs(CRS)
    lam["date"] = lam.DESCRIPTIO.fillna("").map(parse_free)
    sw = gpd.read_file(RAW / "ages/southwark_local_list.geojson").to_crs(CRS)
    swt = {p.stem: p.read_text() for p in (RAW / "ages/southwark").glob("*.txt")}

    def sw_date(nid):
        t = swt.get(str(nid), "")
        t = t.split("Local List Description", 1)[-1]
        return parse_free(t) if t.strip() else None

    sw["date"] = sw.ID.map(sw_date)
    for ll in (lam, sw):
        ll = ll[ll.date.notna()]
        jj = gpd.sjoin(gpd.GeoDataFrame({"identificatie": b.identificatie}, geometry=b.geometry.representative_point(),
                                        crs=CRS), ll[["date", "geometry"]], predicate="within")
        for k, d in zip(jj.identificatie, jj.date):
            if 1000 < d[0] <= 2026:
                rows.append(row(k, *d[:3], "locallist"))
    # contributor eras
    cl = pd.read_csv(RAW / "ages/colouring_year0_candidates.csv")
    for k, s in zip(cl.identificatie, cl["style"]):
        m = ERA.search(str(s))
        if m:
            lo, hi = int(m.group(1)), int(m.group(2))
            rows.append(row(k, (lo + hi) / 2, lo, hi, "era"))
    # energy certificate bands
    u = pd.read_parquet(RAW / "ages/lbsm2_uprn_age_band_9boroughs.parquet")
    u = u[(u.known == 1) & u.band.isin(BANDS)]
    up = gpd.GeoDataFrame(u[["band"]], geometry=gpd.points_from_xy(u.e.astype(float), u.n.astype(float)), crs=CRS)
    jj = gpd.sjoin(up, b[["identificatie", "geometry"]], predicate="within")
    share = jj.groupby(["identificatie", "band"]).size().unstack(fill_value=0)
    top, frac = share.idxmax(axis=1), share.max(axis=1) / share.sum(axis=1)
    m1890 = pd.read_parquet("data/map1890s.parquet").set_index("identificatie").share1890s
    for k in top[frac >= 0.6].index:
        lo, hi = BANDS[top[k]]
        if (lo, hi) == (1900, 1929) and m1890.get(k, 0) >= 0.6:
            lo, hi = 1800, 1899
        # 'before 1900' has no lower end: the map shows the building from 1899, the latest it can be
        rows.append(row(k, hi if lo == 1800 else (lo + hi) / 2, lo, hi, "epc"))
    # brackets from the maps, only the readings that held up against known years: a footprint with no building on
    # the 1890s map (under 5 % covered) was built after 1893 in 93 % of dated cases; one not yet drawn on the
    # 1940s–50s plan (edition A, shading under 25 %) was built after that plan's year in 88 %. 'Built' readings are
    # not used: many buildings stand on the plan of the one before. Edition B closes a bracket where it shows the
    # building; otherwise the bracket stays open (hi 2026) and the building is drawn at its earliest year.
    plans = Path("data/osplans.parquet")
    if plans.exists():
        o = pd.read_parquet(plans).merge(m1890.rename("m").reset_index(), on="identificatie", how="left")
        for r in o.itertuples():
            if pd.notna(r.fill_A) and pd.notna(r.year_A) and r.fill_A < 0.25:
                lo = int(r.year_A)
                hi = int(r.year_B) if pd.notna(r.fill_B) and pd.notna(r.year_B) and r.fill_B > 0.6 and r.year_B > lo else 2026
                rows.append(row(r.identificatie, lo if hi == 2026 else (lo + hi) / 2, lo, hi, "osmaps"))
            elif pd.notna(r.m) and r.m < 0.05:
                rows.append(row(r.identificatie, 1893, 1893, 2026, "osmaps"))
    out = pd.DataFrame(rows).drop_duplicates()
    out.to_parquet("data/ages.parquet")
    dated = out.groupby("src").identificatie.nunique()
    print(dated.to_dict(), "footprints with any date:", out.identificatie.nunique(), "of", len(b))


if __name__ == "__main__":
    main()
