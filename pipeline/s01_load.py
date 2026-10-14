"""Buildings of the chosen boroughs: Overture footprints (OpenStreetMap and Microsoft, ODbL), clipped to the area,
with what Colouring London knows about them (ODbL): construction date and its source, listing.

Colouring London keys its buildings to Ordnance Survey footprints, which are not open; every Colouring building
has a point, and a footprint takes the points that fall inside it. When a footprint covers several Colouring
buildings (a terrace drawn as one block), it takes their most common date.

Writes data/panden.parquet (one row per footprint, a 16-digit id) for the later steps.
"""
import geopandas as gpd
import numpy as np
import pandas as pd
import shapely

from .city import BOROUGHS, CRS

MIN_AREA = 12.0  # m²; sheds and kiosks below this are left out


def main():
    area = gpd.read_file("data/raw/boundary.json").set_crs(CRS, allow_override=True)
    area = area[area.LAD24NM.isin(BOROUGHS)].union_all()
    raw = pd.read_parquet("data/raw/overture_buildings.parquet")
    p = gpd.GeoDataFrame(raw.drop(columns="geometry"), geometry=gpd.GeoSeries.from_wkb(raw.geometry), crs=4326).to_crs(CRS)
    p["geometry"] = shapely.make_valid(p.geometry.values)
    p = p[p.geometry.geom_type.isin(["Polygon", "MultiPolygon"]) & (p.area >= MIN_AREA)]
    p = p[p.representative_point().within(area)].reset_index(drop=True)
    p["identificatie"] = [f"{i + 1:016d}" for i in range(len(p))]  # 16 digits, like a BAG id, so the viewer keeps one format
    p["osm"] = p.sources.map(lambda s: "OpenStreetMap" in list(s))

    c = pd.read_parquet("data/raw/cb_london.parquet")
    c = c[c.lat.notna()]
    pts = gpd.GeoDataFrame(c, geometry=gpd.points_from_xy(c.lon, c.lat), crs=4326).to_crs(CRS)
    j = gpd.sjoin(pts, p[["identificatie", "geometry"]], predicate="within")
    j["src"] = j.date_source.fillna("")
    # A contributor's year counts, with or without a cited source; the platform's computed guesses do not.
    dated = j[j.y.notna() & (j.y > 1000) & (j.src != "Computational generation")]
    best = (dated.groupby(["identificatie", "y", "date_lower", "date_upper", "src"], dropna=False).size().rename("n").reset_index()
            .sort_values("n", ascending=False).drop_duplicates("identificatie"))
    p = p.merge(best.drop(columns="n"), on="identificatie", how="left")
    listed = j[j.planning_list_id.notna()].drop_duplicates("identificatie")[["identificatie", "planning_list_id", "planning_list_grade"]]
    p = p.merge(listed, on="identificatie", how="left")
    p["colouring"] = p.identificatie.isin(set(j.identificatie))
    p = gpd.GeoDataFrame(p, geometry="geometry", crs=CRS)
    p.to_parquet("data/panden.parquet")
    print(f"{len(p)} buildings ({p.osm.mean():.0%} from OSM); Colouring points in {p.colouring.mean():.0%}; "
          f"dated {p.y.notna().sum()} ({p.y.notna().mean():.0%}); listed {p.planning_list_id.notna().sum()}")
    print(p.src.value_counts().head(8).to_dict())


if __name__ == "__main__":
    main()
