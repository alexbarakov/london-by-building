"""DRAFT context layer: street art in inner London, placed by coordinates and attached to the wall's building.

Scope: City of London, Westminster, Camden, Islington, Kensington and Chelsea, Southwark, Lambeth, Tower Hamlets,
Hackney. Entry format (dict variant of curated.py): name, lon, lat, story, ref ("en:Title"), checks, group, plus
`coord` (where lon/lat come from) and `qid` (the artwork's own Wikidata item, where one exists; this is not a
building QID). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited
en.wikipedia article (API prop=extracts, explaintext=1, redirects=1, User-Agent
"london-by-building/0.1 (https://stop-token.com/lab/london/)"); all checks were run on 2026-10-15. Every point is
inside the nine-borough polygon (data/raw/boundary.json). Building distances below are to the nearest footprint in
data/raw/overture_buildings.parquet.

Open data fetched 2026-10-15 (data/raw/streetart/):
- osm_streetart.json: Overpass (overpass-api.de), bbox 51.4108,-0.2290,51.5780,0.0095, tourism=artwork with
  artwork_type mural / graffiti / street_art. 167 features (127 mural, 28 street_art, 12 graffiti; 132 nodes,
  35 ways); 124 fall inside the nine boroughs (the bbox also covers parts of Newham, Lewisham, Haringey and others).
  Field fill: name 60, artist_name 79, start_date 24, wikidata 4, image 4 (+ wikimedia_commons 2, panoramax 7),
  artist:wikidata 21. Licence: ODbL 1.0 (attribution "© OpenStreetMap contributors"; share-alike on derived
  databases).
  Lifecycle tags: no street-art feature carries was:/disused:/removed:. The query also returned 4 was:tourism=artwork
  features (2 sculptures, 2 installations), which were dropped from the file. Free-text signs of loss: node
  948735585 (Banksy, Newman Street, 2008: note "boarded up"; this is One Nation Under CCTV, painted over in April
  2009 per Wikipedia), node 4689273491 ("Banksy - Phone tap", condition=dilapidated), node 4689460589 ("Banksy -
  Very little helps (partially erased)"), node 4692259492 (Bambi, "Lie Lie Land": per en:Bambi (artist) painted over
  by new owners in January 2018, still mapped). OSM therefore over-counts surviving works; it is not a status source.
- wikidata_streetart.csv: SPARQL wikibase:box over the same bbox, items that are instances of (subclasses of) mural
  Q219423, graffiti Q17514, street art Q17516 or wall painting Q1755143, or have genre street art, creator Banksy
  Q133600, or material graffiti. 21 items, all inside the nine boroughs, plus 1 added by label search (Greenwashed
  Tree Q141310187 has P625 but no P31/P170). Field fill: artist 16, start_date 17, image 10, enwiki 14; no item has
  P576. Licence: CC0. The set mixes in non-street works (Nebamun garden fresco in the British Museum, Empire Murals in
  the Foreign Office, Topolski Century, a Bow Common church mosaic, The Drinker sculpture, the 2026 Banksy statue in
  Waterloo Place) and works that no longer exist but carry no end date: One Nation Under CCTV (painted over 2009),
  Pulp Fiction (painted over 2007), Freedom for Humanity (temporary, removed 2012), Royal Courts of Justice (removed
  9-10 September 2025), Goulston Street graffito (1888). Stockwell's memorial mural has two items (Q58642171,
  Q66309299).
- Council / society datasets: none found under an open licence. The London Mural Preservation Society publishes
  descriptions on its website but no licensed dataset; no borough open-data portal publishes a mural register. Not
  used.

Dropped during research (curated part):
- Removed or destroyed: One Nation Under CCTV (Newman Street, painted over April 2009), Pulp Fiction (Old Street,
  painted over 2007), Royal Courts of Justice Banksy (covered 8 Sept 2025, removed 10 Sept), Freedom for Humanity
  (Hanbury Street, temporary, removed 2012), Banksy monkeys on the Brick Lane railway bridge (2024, removed by TfL in
  December; source is the article's table, not its extract), Yellow Line Flower Painter (Bethnal Green Working
  Men's Club, removed 2019), the Blur royal-family Banksy in Stoke Newington (partly painted over 2009), Bambi's Lie
  Lie Land (painted over January 2018), Old Street Israel-Gaza peace mural (removal ordered March 2024), Thierry
  Noir's Museum of London rotunda mural (the London Wall museum site has closed; status not checked).
- Temporary by design: Thierry Noir and Stik's 2013 wall on Village Underground (a rotating wall).
- Exist, but no coordinate on Wikidata or OSM (both checked): Hackney Peace Carnival Mural (Dalston Lane, 1985, en:Dalston
  and en:Ray Walker (artist)), Keith Flint mural by Akse P19 (Beechwood Road, 2021, en:Keith Flint), Big Splash
  (Glenelg Road, 1985) and Dreph's Michelle Obama (Dorrell Place, 2018) from en:Brixton murals, Little Portugal mural
  (South Lambeth, 2023), Brandon Estate Chartist mural by Tony Hollaway, David Attenborough mural (St Matthew's Row,
  en:Bethnal Green). Banksy's elephants on Edith Terrace, Chelsea (August 2024, apparently still there): its
  coordinate exists only in the Wikipedia table, and the plain-text extract of en:Banksy's London animal series
  lacks the table, so nothing about it can be checked.
- No citable article: Shop Till You Drop (Banksy, Bruton Lane, Mayfair; Wikidata Q27949192 has P625 and is probably
  still there), Charlie Burns by Kevin Ledo (used only as the pin for Brick Lane), Peckham Peace Wall (OSM way
  284550496), Banksy's 2017 Barbican pieces (OSM 13442621682 / 13442643902, status unknown), the Bayswater Banksy
  of 21 December 2025 (en:Banksy names no street and gives no status).
- Not street art or out of era: Topolski Century, Empire Murals, Fleet Building murals (Dorothy Annan, 1960),
  History of the Old Kent Road (Kossowski tiles, 1960s), Ten Bells tiles, Camden Lock bridge lettering (1989, on a
  railway bridge, not a building).
- Banksy's 15 works (2001) in the Swiss Embassy's underground car park, Montagu Place: indoor and private; mentioned
  only in en:Banksy's bibliography.

Counts: 14 entries (Banksy 1, Leake Street 1, graffiti walls 1, murals 8, Shoreditch and Brick Lane 3). By borough:
Lambeth 6, Tower Hamlets 4, Islington 1, Camden 1, Hackney 1, Kensington and Chelsea 1. None in the City,
Westminster or Southwark: no surviving work there passed the source tests (candidates: Shop Till You Drop in
Mayfair, Peckham Peace Wall in Southwark).

Doubts to check before publishing:
- Banksy has one entry only: Greenwashed Tree is the only Banksy wall work in the nine boroughs whose survival an
  article states. The group could be renamed or merged.
- Building attachment beyond ~10 m: Nuclear Dawn (OSM node sits 27 m from the nearest Overture footprint; the gable
  may be missing from Overture or the node is placed in the open space in front), National Covid Memorial Wall
  (a river wall, 24 m from St Thomas' Hospital North Wing), Trellick hall of fame (level -1 walls, 16.5 m from
  Trellick Tower's footprint). Leake Street is a tunnel under Waterloo station; the Wikidata point is at the York
  Road mouth, 6.4 m from a small building and 11.7 m from the station footprint.
- Stockwell memorial: the point falls inside a footprint Overture names "Clapham Road Shaft"; the mural is on the
  Stockwell deep-level shelter entrance. Check the footprint's identity.
- Fitzrovia Mural: pinned to OSM node 5720813658 ("Community mural", addr Tottenham Street), matched by position to
  Whitfield Gardens; en:Tottenham Court Road says it was neglected and that a restoration was proposed (en:London
  Mural Preservation Society says a restoration project was supported in 2010).
- ROA's rabbit: the article records the 2011 reprieve but not the current state.
- Rich Mix NHS mural: the article gives no date and no current state ("one of the project's latest murals").
- David Bowie mural: the artist (Jimmy C, 2013) comes from OSM tags; en:David Bowie only mentions the mural.
- Brick Lane: the entry is about the street's walls in general, pinned to the Charlie Burns mural (Wikidata
  Q117834896, which has no article).
"""

LAYER = dict(
    id="streetart",
    section="The modern city",
    title="Street art",
    era="1980s–today",
    intro=(
        "Paint on walls: the community murals that councils funded after the 1981 riots and the GLC years, "
        "the legal walls and tunnels where graffiti writers practise, and the stencils that made Banksy famous. "
        "Street art is short-lived by nature, so only works that still stand are shown, each pinned to the "
        "building whose wall carries it."
    ),
    entries=[
        # --- Banksy ---
        dict(
            name="Greenwashed Tree (Banksy)",
            lon=-0.11951, lat=51.564687, coord="Wikidata Q141310187 P625", qid="Q141310187",
            story=(
                "Banksy painted a burst of green leaves on the flank wall of a residential block on Hornsey Road "
                "on 18 March 2024, behind a heavily pollarded tree, with a stencilled figure holding a sprayer. "
                "It was vandalised within days and is now protected."
            ),
            ref="en:Greenwashed Tree",
            checks=(
                "on Hornsey Road in north London",
                "18 March 2024",
                "behind a tree that had recently been heavily pollarded",
                "As of 2026, the mural remains visible and protected, although damaged",
            ),
            group="Banksy",
        ),
        # --- Leake Street ---
        dict(
            name="Leake Street tunnel",
            lon=-0.1157, lat=51.502, coord="Wikidata Q6509320 P625 (York Road end)", qid=None,
            story=(
                "A 300-metre road tunnel under the platforms of Waterloo station where graffiti is legal. Its walls "
                "were first painted at Banksy's Cans Festival in May 2008."
            ),
            ref="en:Leake Street",
            checks=(
                "Banksy Tunnel",
                "where graffiti is legal",
                "under the platforms and tracks of Waterloo station",
                "Cans Festival organised by Banksy on 3–5 May 2008",
            ),
            group="Leake Street",
        ),
        # --- graffiti walls ---
        dict(
            name="Trellick Tower graffiti wall",
            lon=-0.20516, lat=51.52331, coord="OSM node 11415654182", qid=None,
            story=(
                "The hall-of-fame walls at the foot of Goldfinger's tower. A 2021 redevelopment plan would have "
                "destroyed them; it met fierce opposition and was dropped in December 2021."
            ),
            ref="en:Trellick Tower",
            checks=(
                "destroying a graffiti wall",
                "faced fierce opposition and were abandoned in December 2021",
            ),
            group="graffiti walls",
        ),
        # --- murals ---
        dict(
            name="Cable Street Mural",
            lon=-0.05861, lat=51.51094, coord="OSM node 2673685170 (Wikidata Q18159700 P625 is 1.8 m away)",
            qid="Q18159700",
            story=(
                "Painted across the side of St George's Town Hall between 1979 and 1983 to commemorate the Battle "
                "of Cable Street of 1936, when East Londoners blocked Mosley's fascists. Right-wing vandals "
                "attacked it before it was finished; it has been restored several times."
            ),
            ref="en:Cable Street Mural",
            checks=(
                "painted on the side of St George's Town Hall",
                "between 1979 and 1983 to commemorate the Battle of Cable Street in 1936",
                "The uncompleted mural was vandalised on 23 May 1982",
                "restored again by Butler for the 75th anniversary",
            ),
            group="murals",
        ),
        dict(
            name="Poplar Rates Rebellion Mural",
            lon=-0.01755, lat=51.50967, coord="OSM way 860033290 (centroid)", qid="Q20713184",
            story=(
                "Mark Francis's 1990 mural on a council depot in Hale Street remembers 1921, when Poplar's "
                "councillors under George Lansbury refused to pay precepts and 30 of them went to prison."
            ),
            ref="en:Poplar Rates Rebellion Mural",
            checks=(
                "Hale Street, Poplar",
                "depot of Tower Hamlets Parks Department",
                "30 councillors were imprisoned",
                "painted by Mark Francis in 1990",
            ),
            group="murals",
        ),
        dict(
            name="Children at Play, Brixton Academy",
            lon=-0.114776, lat=51.465882, coord="Wikidata Q113511423 P625", qid="Q113511423",
            story=(
                "Commissioned by Lambeth Council after the 1981 Brixton riot, Stephen Pusey's 32-metre mural of "
                "children playing covers the back of the Academy. Locals call it the 'Zombie Children'."
            ),
            ref="en:Children at Play",
            checks=(
                "rear of the Brixton Academy on Stockwell Park Walk",
                "in the wake of the 1981 Brixton riot",
                "'Zombie Children'",
                "The mural is 32 meters by 9 meters",
            ),
            group="murals",
        ),
        dict(
            name="Nuclear Dawn",
            lon=-0.11127, lat=51.46189, coord="OSM node 12463302374", qid=None,
            story=(
                "Brian Barnes and Dale McCrea's Cold War mural on Coldharbour Lane: a giant skeleton straddles "
                "London as the bomb falls, while the government shelters in a bunker."
            ),
            ref="en:Brixton murals",
            checks=(
                "Nuclear Dawn, Coldharbour Lane, by Brian Barnes and Dale McCrea",
                "a giant skeleton standing over London",
                "with the Conservative Party in a bunker",
            ),
            group="murals",
        ),
        dict(
            name="Stockwell War Memorial mural",
            lon=-0.122059655, lat=51.473082131, coord="Wikidata Q58642171 P625 (OSM node 10915942901 agrees)",
            qid="Q58642171",
            story=(
                "Brian Barnes painted the entrance of the Stockwell deep-level shelter in 2001 with local "
                "children, honouring Violette Szabo, Van Gogh and the area's war dead."
            ),
            ref="en:Brixton murals",
            checks=(
                "Stockwell War Memorial, Stockwell Road, by Brian Barnes – 2001",
                "Painted on the exterior of the entrance to a deep-level shelter",
                "Violette Szabo and Vincent van Gogh",
            ),
            group="murals",
        ),
        dict(
            name="David Bowie mural, Brixton",
            lon=-0.11567, lat=51.46262, coord="OSM node 4596880090", qid=None,
            story=(
                "A portrait of Bowie near his birthplace (by Jimmy C, 2013, per OSM). When he died in 2016 it "
                "became a shrine where fans left flowers and sang."
            ),
            ref="en:David Bowie",
            checks=(
                "At the mural of Bowie in his birthplace of Brixton, south London, fans laid flowers and sang his songs.",
            ),
            group="murals",
        ),
        dict(
            name="Fitzrovia Mural",
            lon=-0.13506, lat=51.52077, coord="OSM node 5720813658", qid=None,
            story=(
                "A 20-metre wall of people at work and play above Whitfield Gardens, painted in 1980 in the manner "
                "of Diego Rivera."
            ),
            ref="en:Tottenham Court Road",
            checks=(
                "Whitfield Gardens",
                "Fitzrovia Mural",
                "painted in 1980 in a style resembling that of Diego Rivera",
            ),
            group="murals",
        ),
        dict(
            name="National Covid Memorial Wall",
            lon=-0.12006, lat=51.49996, coord="OSM node 9318398386", qid="Q106509908",
            story=(
                "Begun without permission in March 2021: volunteers hand-painted red hearts along the river wall "
                "opposite Parliament, one for each Covid death. Bereaved families now keep them repainted."
            ),
            ref="en:National Covid Memorial Wall",
            checks=(
                "opposite the Palace of Westminster",
                "Led By Donkeys",
                "the project was started without council permission",
                "The Friends of the Wall completely repainted the hearts",
            ),
            group="murals",
        ),
        # --- Shoreditch and Brick Lane ---
        dict(
            name="Brick Lane walls",
            lon=-0.07172, lat=51.52397, coord="Wikidata Q117834896 P625 (Charlie Burns mural by Kevin Ledo)",
            qid="Q117834896",
            story=(
                "The best-known street-art gallery in London, with walls by Banksy, Stik, ROA, D*Face and Ben Eine "
                "painted and repainted. Pinned to Kevin Ledo's portrait of Charlie Burns."
            ),
            ref="en:Brick Lane",
            checks=(
                "Brick Lane has a regular display of graffiti, which features artists such as Banksy, Stik, ROA, "
                "D*Face, Ben Eine and Omar Hassan.",
            ),
            group="Shoreditch and Brick Lane",
        ),
        dict(
            name="ROA's rabbit, Hackney Road",
            lon=-0.07159, lat=51.53115, coord="OSM way 824820039 (The Premises Studios, centroid)", qid=None,
            story=(
                "The Belgian artist ROA painted a 3.5-metre rabbit on The Premises Studios with the owners' "
                "permission. In 2011 Hackney Council moved to paint it over; a campaign by the owners and "
                "residents changed the council's mind."
            ),
            ref="en:ROA (artist)",
            checks=(
                "a 3.5 m high rabbit",
                "The Premises Studios in Hackney Road",
                "forcing the council to change its mind",
            ),
            group="Shoreditch and Brick Lane",
        ),
        dict(
            name="NHS flowers mural, Rich Mix",
            lon=-0.07313, lat=51.5244, coord="OSM way 274608954 (Rich Mix, centroid)", qid=None,
            story=(
                "A four-storey crowdsourced mural for the NHS on the Rich Mix arts centre, designed by ATMA with "
                "more than 200 flowers drawn by members of the public."
            ),
            ref="en:Paint the Change",
            checks=(
                "four-storey crowdsourced mural celebrating the UK's National Health Service",
                "more than 200 flowers drawn by members of the public",
                "35-47 Bethnal Green Road",
                'Matt "ATMA" Dufour',
            ),
            group="Shoreditch and Brick Lane",
        ),
    ],
)
