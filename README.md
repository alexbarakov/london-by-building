# London, building by building

The 213,000 buildings of inner London (the City, Westminster, Camden, Islington, Kensington and Chelsea, Southwark,
Lambeth, Tower Hamlets and Hackney), by age and historical context.
**Live:** https://stop-token.com/lab/london/

A sibling of [LAYRS: Amsterdam](https://github.com/alexbarakov/amsterdam-by-building) and
[LAYRS: Delft](https://github.com/alexbarakov/delft-by-building). A non-commercial project, made for curiosity and
learning. Inspired by Sasha Bogachev's [Paris, building by building](https://paris.bogachev.fr).

**Want to add a layer?** See [CONTRIBUTING.md](CONTRIBUTING.md).
**Know when a building was built?** Add it to [Colouring London](https://colouringbritain.org): this map takes its
years from there.

## How it works

```
open data ──► pipeline/ (Python) ──► web/data/ (binary tiles + JSON) ──► web/ (three.js, no build step)
```

| Step | What it does |
|---|---|
| `s00_fetch_lidar` | Environment Agency LIDAR surface and terrain, 1 m, for every square kilometre of the area |
| `s00_fetch_wikidata` | Wikidata items in the area that are listed or have an English Wikipedia article |
| `s01_load` | Overture footprints clipped to the boroughs, joined to Colouring London's dates and listing |
| `s01c_heights` | Height of each footprint from the LIDAR |
| `s01d_1890s` | Share of each footprint covered by buildings of the 1891–96 OS map |
| `s00_fetch_nhle_text`, `s00_fetch_local_lists`, `s00_fetch_os_plans` | Listing descriptions, Lambeth and Southwark local lists, OS 1:1250 plan tiles (NLS) |
| `s01g_spires` | Towers, spires and domes above the prisms, as 1 m columns from the LIDAR surface (trees and taller neighbours filtered out) |
| `s01f_os_plans` | Whether each footprint is drawn on the OS plans of the 1940s–70s, and the sheet's year |
| `s01e_ages` | Every sourced date for every footprint, one row per source |
| `s02_attributes` | Years (known only), periods, floors |
| `s05_layers` | Resolves every context layer to a bit per building |
| `s03_tiles` | Packs 600 m tiles into 8 bundles, writes per-building attributes and the city config |
| `s04_water` | Water and land polygons |
| `s06_wiki` | Names, photos and extracts from Wikidata, Wikipedia and Commons |
| `s07_labels` | Street, river and canal names placed along their outlines |
| `s08_curated` | Checks hand-written stories against Wikipedia and places them by their Wikidata item |
| `s11_facts` | Checks the 'Did you know' facts the same way |
| `s14_search` | Search index: named and listed buildings, listed buildings' addresses, and the buildings along every street (London has no open address register) |

Raw inputs (not in the repository): `data/raw/boundary.json` (ONS borough boundaries), `overture_buildings.parquet`,
`overture_roads.parquet` and `overture_water.parquet` (Overture Maps release 2026-09-23.1, fetched with DuckDB), and
`cb_london.parquet`, the London rows of a Colouring Britain data extract.

## Data decisions

- **Years.** London has no open register of construction years. Each building takes its date from the most precise
  open source that has one (see `s01e_ages` for the list and the order), and the card names the source. Ranges (a
  listing's century, an energy-certificate band, "after 1952" because the building is not yet on that plan) are
  drawn paler. Map readings are used only where they held up against known years: a footprint with no building on
  the 1890s map was built after 1893 in 93 % of dated cases, one not yet on the 1940s–50s plan after that plan's year
  in 88 %. No model estimates (Colouring London's computed guesses, the Alan Turing Institute's 2020 test) and
  nothing borrowed from neighbours: undated buildings stay grey.
  `data/raw/ages/` holds inputs prepared once: the LBSM2 age bands per UPRN (London Datastore), Price Paid new-build
  candidates per footprint (Land Registry PPD joined through the ONS UPRN Directory), LDD completions matched by site
  point, OSM date and Wikidata tags, and Colouring London contributors' eras from its edit history.
- **Heights.** The 70th percentile of the LIDAR surface within each footprint, over the median terrain just
  outside it.
- **Stories.** Every story names its Wikipedia article and its Wikidata item; `s08_curated` checks the article contains
  the story's key facts, then places the story by the item's listing number or its coordinates.

## Licence

Code: MIT (see [LICENSE](LICENSE)). Data keeps the licence of its source: Overture and OpenStreetMap ODbL;
Colouring London ODbL; Environment Agency LIDAR and ONS boundaries Open Government Licence; Wikidata CC0;
Wikipedia text CC BY-SA; Wikimedia Commons photos each under their own licence, credited in the app.
