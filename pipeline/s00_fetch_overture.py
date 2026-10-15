"""Overture Maps (release 2026-09-23.1) for the area's box: buildings, named roads and water, as GeoParquet with WKB.
Buildings come from OpenStreetMap and Microsoft's ML footprints (ODbL); roads and water from OpenStreetMap."""
import duckdb

R = "s3://overturemaps-us-west-2/release/2026-09-23.1"
BOX = "bbox.xmin > -0.2290 AND bbox.xmax < 0.0095 AND bbox.ymin > 51.4108 AND bbox.ymax < 51.5780"
OVERLAP = "bbox.xmin < 0.0095 AND bbox.xmax > -0.2290 AND bbox.ymin < 51.5780 AND bbox.ymax > 51.4108"


def main():
    c = duckdb.connect()
    c.sql("INSTALL httpfs; LOAD httpfs; SET s3_region='us-west-2';")
    c.sql(f"""COPY (SELECT id, height, num_floors, min_height, roof_shape, names.primary AS name, class, subtype,
                 list_transform(sources, s -> s.dataset) AS sources, geometry
          FROM read_parquet('{R}/theme=buildings/type=building/*', hive_partitioning=1) WHERE {BOX})
          TO 'data/raw/overture_buildings.parquet' (FORMAT parquet)""")
    c.sql(f"""COPY (SELECT id, names.primary AS name, class, subtype, geometry
          FROM read_parquet('{R}/theme=transportation/type=segment/*', hive_partitioning=1)
          WHERE {BOX} AND subtype = 'road' AND names.primary IS NOT NULL) TO 'data/raw/overture_roads.parquet' (FORMAT parquet)""")
    c.sql(f"""COPY (SELECT id, names.primary AS name, class, subtype, geometry
          FROM read_parquet('{R}/theme=base/type=water/*', hive_partitioning=1) WHERE {OVERLAP})
          TO 'data/raw/overture_water.parquet' (FORMAT parquet)""")
    parks()


def parks():
    """Parks, gardens, commons and churchyards (Overture land use, from OpenStreetMap, ODbL)."""
    c = duckdb.connect()
    c.sql("INSTALL httpfs; LOAD httpfs; SET s3_region='us-west-2';")
    c.sql(f"""COPY (SELECT id, names.primary AS name, class, subtype, geometry
          FROM read_parquet('{R}/theme=base/type=land_use/*', hive_partitioning=1)
          WHERE {OVERLAP} AND (subtype IN ('park', 'recreation', 'cemetery', 'grass')
                OR class IN ('park', 'garden', 'recreation_ground', 'village_green', 'common', 'nature_reserve',
                             'cemetery', 'grave_yard', 'playground', 'pitch', 'grass', 'meadow')))
          TO 'data/raw/overture_parks.parquet' (FORMAT parquet)""")


if __name__ == "__main__":
    import sys
    parks() if sys.argv[1:] == ["parks"] else main()
