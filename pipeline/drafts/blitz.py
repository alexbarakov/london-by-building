"""DRAFT context layer: The Blitz and the war (1940-1945). Replaces the 14-entry 'blitz' layer in pipeline/curated.py;
all 14 old entries are kept word for word (only the group "command" is renamed "war rooms and shelters").

Same entry format as pipeline/curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or
None, group). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia
article (API prop=extracts, explaintext=1, redirects=1); all 100 entries were checked on 2026-10-15. Each QID was read
from Special:EntityData: it has P625, and that point falls inside the polygon of one of the nine boroughs
(data/raw/boundary.json, point-in-polygon, not nearest postcode). The NHLE number is the item's P1216, or None when
the item has none. Groups: ruin kept 7, hit and restored 35, rebuilt after 24, war rooms and shelters 17,
V-weapons 12, memorials 5.

Point dataset of impacts (task B):
- Zenodo record 14882793, "V1 and V2 impact sites in London" (Liam Shaw, 17 Feb 2025), licence CC BY 4.0. That
  version holds only an HTML analysis file; the data are in the sibling version 14883986 (same concept record
  14882695, DOI 10.5281/zenodo.14883986, also CC BY 4.0). Saved, md5 matching Zenodo, to
  data/raw/blitz/zenodo_14883986/ (V1-impacts.csv, V2-impacts.csv, bomb_map.kml, data-conversion.R).
  Attribution required: "Shaw, L. (2025). V1 and V2 impact sites in London. Zenodo. doi:10.5281/zenodo.14883986".
- Combined copies: data/raw/blitz/v_weapon_impacts_lcc.csv and .geojson (EPSG:4326 points), 1,006 rows: 887 V1,
  119 V2. Fields: id (V1.n / V2.n as in the source), weapon (V1 | V2), ward_page (page in Ward 2015), street
  (nearest street name given by the compiler), lon, lat (WGS84), easting, northing (EPSG:27700, from the source),
  borough (LAD24NM from boundary.json, empty outside the nine). Inside the nine boroughs: 446 V1 + 57 V2 = 503.
- There is NO date field: the source records only weapon type, map page and street. Dates would have to come from
  elsewhere (e.g. the Bomb Sight/LCC records, which we may not use).
- Coverage: only the County of London (LCC) area, and the author warns it is not a comprehensive list of V-weapon
  impacts. Doubt: the points were hand-digitised from the LCC bomb damage maps as reproduced in Laurence Ward, "The
  London County Council Bomb Damage Maps 1939-1945" (Thames & Hudson, 2015). The maps themselves are copyright
  (London Metropolitan Archives / City of London); Shaw releases his derived points under CC BY 4.0. Point positions
  are facts, but check that reading before publishing.
- Historic England: no open bomb or V-weapon impact dataset found. The NHLE GIS downloads (OGL) carry list entries
  only; war damage appears in list-entry text, not as points.
- London Datastore: the CKAN catalogue (package_search, ~1,300 datasets) has no bomb, Blitz or war-damage dataset.
- Not used, as instructed: Bomb Sight (bombsight.org, Blitz bomb census Oct 1940 - Jun 1941; non-commercial terms)
  and the LCC bomb damage maps (copyright).

Dropped during research:
- No longer standing / not a building: St Mary Aldermanbury (shell moved to Fulton, Missouri; only a garden on the
  site), St Mildred Bread Street, St Swithin London Stone, St Stephen Coleman Street, St Mary Matfelon, St Mary
  Haggerston, Holy Trinity Minories, St Mary Bromley St Leonard, St John Horsleydown (closed 1968, demolished),
  St Peter's Regent Square, Queen's Hall, Broderers' Hall, Cordwainers' Hall, Serjeant's Inn, Columbia Market
  (demolished; Q137639300 has no war text), Highbury & Islington station building (V-1 1944, demolished 1960s),
  Arsenal Stadium (ARP post and bombed, but item has P576; only the converted stands remain), Hughes Mansions (no
  article), Kingsway telephone exchange (tunnels; used Chancery Lane station instead), London Wall, Smithfield
  (Q3182018 is an area; the 1945 V-2 on Charterhouse Street has no building item), Kennington Park trench shelter
  (a park), Stockwell War Memorial on the shelter shaft (Q27082975, no en article).
- Already in another curated layer (each QID appears only once in curated.py, so left out here): Kensington Palace,
  Clarence House, Lambeth Palace, Tower of London (White Tower in 'power'), Imperial War Museum, Natural History
  Museum, Royal Albert Hall, Somerset House, Old Bailey, Royal Hospital Chelsea (infirmary bombed), Goldsmiths',
  Fishmongers' and Merchant Taylors' halls, Trinity House (Q90804634; gutted 29 Dec 1940), Middle Temple Hall,
  St Bride's, St Vedast, St Lawrence Jewry, St Olave Hart Street, St James Garlickhythe, St Mary Aldermary,
  St Etheldreda's, St George in the East (modern church in the shell, 1964), All Souls Langham Place, Barbican
  Estate, Bevin Court, Spa Green, Churchill Gardens, Down Street and Aldwych stations, St Pancras, Cannon Street,
  Paddington, London Bridge, Euston and Charing Cross stations, Jewel Tower, 10 Downing Street, Spencer House,
  Senate House (Ministry of Information), Liverpool Street station, Sandys Row Synagogue.
- Weak or no war text in the article: Broadcasting House, Tate Britain (only "bomb damage during World War II"; no
  mention of the shrapnel scars on its walls), Mansion House, Royal
  Courts, Royal Exchange (survived), Drapers' and Grocers' halls (survived), St Bartholomew-the-Great, St Helen's
  Bishopsgate, St Andrew Undershaft (all escaped), Stationers' Hall (company article has no war text), Brewers' and
  Salters' halls (company articles only mention the old halls), Christ Church Spitalfields, Wilton's Music Hall,
  Windmill Theatre, Garden Museum (glass only), Lincoln's Inn, UCL.
- Cut for length (verified, usable as replacements): Holy Trinity Hoxton, St Andrew Holborn,
  Clapham North station, St Mary Abbots (fire-bombs 1944), Holy Trinity Sloane Street, St Mark's Kennington,
  St George the Martyr, Saint Sophia Cathedral, St Mary The Boltons, St Peter's London Docks, St Botolph's Aldgate,
  Mount Pleasant, Poplar Baths, Streatham Hill Theatre, Prince Edward Theatre, Madame Tussauds, Ritz, Bridgewater
  House, Savoy (air-raid shelters), Holborn Viaduct, Blackfriars, Westminster School,
  Speaker's House, Bermondsey Town Hall, St Mary of Eton, St Michael's Highgate.
- Livery halls rebuilt after the war mostly lack building items on Wikidata (Barber-Surgeons', Bakers',
  Leathersellers', Haberdashers', Saddlers', Mercers', Clothworkers'): only company items without coordinates.
- ARP posts: no surviving ARP post with a Wikidata item and article was found. Civil-defence buildings used
  instead: Finsbury Town Hall (shelter and control centre) and Stoke Newington Town Hall (civil defence HQ).

Doubts to check before publishing:
- Five QIDs are also in other curated layers: St Paul's Cathedral and St Mary-le-Bow ('fire'), Buckingham Palace,
  Westminster Abbey and Palace of Westminster ('power'). Kept because the brief names them; drop or re-point if a
  QID may appear in one layer only.
- Station items (Bank, Bethnal Green, Sloane Square, Goodge Street, Belsize Park, Camden Town, Chancery Lane,
  Stockwell, Clapham Common, Brompton Road, Victoria, Waterloo) are station items, not shelter buildings: the map
  will light whatever footprint the station point falls on. Deep-shelter surface blockhouses have no items.
- Institution-type items carrying building coordinates: Gray's Inn (P1216 1000351 is its registered garden),
  Morley College, Minet Library, British Museum, V&A (no P1216), Churchill War Rooms, Café de Paris, Electra House.
- P576 (end date) is set on Christ Church Greyfriars, St Dunstan-in-the-East, St Augustine Watling Street (wartime
  destruction; ruins kept deliberately), Temple Church and the Charterhouse (dissolution dates); all stand.
- Admiralty Citadel (Q26319560) has no en article of its own; the story rests on the 'Military citadels under
  London' article.
- American International Church: Wikipedia says Whitefield's Tabernacle was hit by "the last V-2 rocket to fall on
  London"; other sources put the last V-2 at Orpington on 27 March 1945, so the story says "one of the last".
- St Paul's, Bow Common, Holy Trinity Rotherhithe, St Boniface's, Sacred Heart Camberwell, Christ Church Southwark,
  All Hallows Bow, Jack Straw's Castle, Central Synagogue, Guildhall Art Gallery, Morley College, Minet Library and
  Our Lady of Victories are post-war replacements: the building on the map is the rebuild, not the bombed one.
- 10 Trinity Square and the Dutch Church each have two P1216 values; the first is recorded.
- Southwark Cathedral: the 20 February 1941 date is when the damage was reported, not when the bomb fell.
"""

LAYER = dict(
    id="blitz", section="War and disaster", title="The Blitz and the war", era="1940–1945",
    intro=("German bombing hit London from September 1940 to May 1941, came back in the 'Baby Blitz' of 1944, and "
           "ended with V-1 flying bombs and V-2 rockets in 1944–45. The fire raid of 29 December 1940 burned out much "
           "of the City. Some buildings were repaired, some were left as ruins and gardens, and many were rebuilt "
           "after the war; others stand over the shelters and bunkers dug for the raids."),
    entries=[
        # ---- ruin kept ----
        ("Christ Church Greyfriars", "Q1077970",
         "Wren's church was gutted by a firebomb on 29 December 1940; only the tower was kept. The nave "
         "became a public garden in 1989.",
         "en:Christ Church Greyfriars", ("29 December 1940", "1989", "public garden"),
         "1359217", "ruin kept"),
        ("St Dunstan-in-the-East", "Q12408518",
         "Wren's tower and spire survived the bombs of 1941, but little else did. The City opened the ruin as"
         " a public garden in 1971.",
         "en:St Dunstan-in-the-East", ("1941", "opened in 1971", "Wren's tower"),
         "1359173", "ruin kept"),
        ("St Alban, Wood Street", "Q7592245",
         "The church burned out in 1940 and the remains of its body were demolished in 1965. The tower stands"
         " alone on a traffic island and is now a private house.",
         "en:St Alban, Wood Street", ("1940", "1965", "private dwelling on a traffic island"),
         "1079120", "ruin kept"),
        ("Holland House", "Q2342832",
         "A Jacobean country house built in 1605, later a gathering place for Whigs. Firebombs in 1940 left "
         "only the east wing and some ruins standing in Holland Park.",
         "en:Holland House", ("1605", "Whigs", "1940", "east wing"),
         "1267135", "ruin kept"),
        ("St Augustine Watling Street", "Q7592558",
         "Bombing in 1941 destroyed the church but not its tower, which was restored and built into St Paul's "
         "choir school in 1967. Faith, the church cat, was found guarding her kitten in the ruins.",
         "en:St Augustine Watling Street",
         ("destroyed by bombing in 1941", "the tower was restored in 1954", "completed in 1967",
          "Faith the cat who defied the London Blitz"),
         "1079121", "ruin kept"),
        ("St Alphege London Wall", "Q7592313",
         "The nave had gone in 1923, and the medieval tower that was left was gutted by fire in 1940. The ruin, "
         "listed in 1950, is now the centrepiece of London Wall Place.",
         "en:St Alphege London Wall",
         ("The nave was demolished in 1923", "The tower was gutted by fire in 1940", "4 January 1950",
          "London Wall Place"),
         "1193558", "ruin kept"),
        ("St John's Church, Wapping", "Q27081780",
         "The church was bombed in the Second World War and only a shell remained. The London County Council "
         "restored the tower in 1964, and the rest became flats in the 1990s.",
         "en:St John's Church, Wapping",
         ("only a fragmentary rectangular shell remaining", "restored in 1964 by the London County Council",
          "converted into flats in the 1990s"),
         "1241683", "ruin kept"),

        # ---- hit and restored ----
        ("Guildhall", "Q81279",
         "The roof of the medieval great hall was destroyed in the fire raid of 29/30 December 1940. Giles "
         "Gilbert Scott designed its replacement in 1954.",
         "en:Guildhall, London", ("29/30 December 1940", "1954", "Giles Gilbert Scott"),
         "1064675", "hit and restored"),
        ("Temple Church", "Q1429312",
         "The round church of the Knights Templar was consecrated in 1185. It was heavily damaged by German "
         "bombing and has since been restored.",
         "en:Temple Church", ("1185", "round church", "German bombing"),
         "1064646", "hit and restored"),
        ("St Clement Danes", "Q2038269",
         "Wren's church on the Strand was gutted in the Blitz and restored only in 1958, as the central "
         "church of the Royal Air Force.",
         "en:St Clement Danes", ("Blitz", "1958", "Royal Air Force"),
         "1237099", "hit and restored"),
        ("St Giles-without-Cripplegate", "Q2323930",
         "A medieval church that escaped the fire of 1666 but was gutted by German bombs. John Milton was "
         "buried here in 1674; the church now stands inside the Barbican.",
         "en:St Giles-without-Cripplegate", ("1666", "German bombs", "John Milton", "1674", "Barbican"),
         "1359183", "hit and restored"),
        ("All Hallows-by-the-Tower", "Q579381",
         "The church survived the fire of 1666 but was badly damaged in the Blitz. After rebuilding it was "
         "rededicated in 1957.",
         "en:All Hallows-by-the-Tower", ("survived the Great Fire", "Blitz", "1957"),
         "1064671", "hit and restored"),
        ("The Charterhouse", "Q6670230",
         "On the night of 10–11 May 1941 bombs burned out the Tudor courtyard house's great hall and Master's"
         " Court. They were restored after the war, and the almshouse is still lived in.",
         "en:London Charterhouse", ("10–11 May 1941", "Master's Court", "almshouse"),
         "1298101", "hit and restored"),
        ("Café de Paris", "Q5017277",
         "A bomb hit the Coventry Street nightclub on 8 March 1941 and killed at least 34 people. It reopened"
         " in 1948.",
         "en:Café de Paris, London", ("8 March 1941", "34 people", "1948"),
         None, "hit and restored"),
        ("St Paul's Cathedral", "Q173882",
         "On 12 September 1940 Royal Engineers under Robert Davies defused a time bomb that had struck the "
         "cathedral. Herbert Mason's photograph St Paul's Survives shows the dome above the smoke of 29 December "
         "1940.",
         "en:St Paul's Cathedral",
         ("On 12 September 1940, a time-delayed bomb", "Robert Davies", "St Paul's Survives", "29 December 1940",
          "Herbert Mason"),
         "1079157", "hit and restored"),
        ("St Mary-le-Bow", "Q2301992",
         "The Bow Bells church took several direct hits on the last night of the Blitz, 10–11 May 1941. Laurence "
         "King rebuilt it to Wren's design between 1956 and 1964.",
         "en:St Mary-le-Bow", ("10–11 May 1941", "Laurence King", "from 1956 to 1964"),
         "1064696", "hit and restored"),
        ("St Mary Abchurch", "Q7594555",
         "A bomb hit the church in September 1940 and did most harm to its painted dome, repaired between 1948 "
         "and 1953. The carved reredos had been taken to a place of safety for the war.",
         "en:St Mary Abchurch",
         ("A bomb hit the church in September 1940", "The greatest damage was to the dome", "between 1948 and 1953",
          "kept in a place of safety"),
         "1359119", "hit and restored"),
        ("St Nicholas Cole Abbey", "Q7594953",
         "German bombs left the church a gutted shell, which is the scene of the gold heist in The Lavender Hill "
         "Mob (1951). Arthur Bailey rebuilt it in 1961–62.",
         "en:St Nicholas Cole Abbey",
         ("substantial bomb damage", "The gutted shell", "The Lavender Hill Mob", "Arthur Bailey in 1961–62"),
         "1079146", "hit and restored"),
        ("St Andrew-by-the-Wardrobe", "Q7586911",
         "German bombing gutted Wren's church, leaving only the tower and walls. It was rebuilt inside them and "
         "rededicated in 1961.",
         "en:St Andrew-by-the-Wardrobe", ("only the tower and walls survived", "rededicated in 1961"),
         "1079148", "hit and restored"),
        ("St Anne and St Agnes", "Q3495309",
         "The church was largely destroyed on the night of 29–30 December 1940. It was rededicated in 1966 for "
         "the exiled Estonian and Latvian Lutheran communities.",
         "en:St Anne and St Agnes", ("29–30 December 1940", "rededicated in 1966", "Estonian and Latvian"),
         "1286384", "hit and restored"),
        ("St Magnus the Martyr", "Q7594088",
         "A bomb that fell on London Bridge in 1940 blew out all the church's windows and damaged its plasterwork"
         " and roof. Its ten bells were stored in the churchyard for safe keeping.",
         "en:St Magnus the Martyr",
         ("A bomb which fell on London Bridge in 1940", "blew out all the windows", "stored in the churchyard"),
         "1064601", "hit and restored"),
        ("Bank station", "Q806704",
         "Londoners sheltered in the station during the Blitz. On 11 January 1941 a bomb hit the booking hall "
         "and the blast ran down the escalators to the platforms, killing 56 people.",
         "en:Bank and Monument stations",
         ("used as a bomb shelter", "11 January 1941", "56 people were killed", "escalators to the platforms"),
         None, "hit and restored"),
        ("10 Trinity Square", "Q7699363",
         "German bombing in the Blitz destroyed the domed rotunda at the heart of the Port of London Authority's "
         "headquarters. Its place is now a plain courtyard.",
         "en:10 Trinity Square",
         ("domed rotunda was destroyed", "Port of London Authority",
          "Plain courtyard formerly filled by large rotunda destroyed in World War II"),
         "1079138", "hit and restored"),
        ("Buckingham Palace", "Q42182",
         "The palace was bombed nine times in the war; one raid in 1940 destroyed the chapel while the King and "
         "Queen were at home. The Queen said she was glad, because she could now look the East End in the face.",
         "en:Buckingham Palace",
         ("bombed nine times", "destroyed the palace chapel in 1940", "I'm glad we have been bombed",
          "look the East End in the face"),
         "1239087", "hit and restored"),
        ("St James's Church, Piccadilly", "Q4893186",
         "Wren's church was severely damaged in the raid of 14 October 1940. Its restoration was completed in "
         "1954.",
         "en:St James's Church, Piccadilly", ("14 October 1940", "completed in 1954"),
         "1226621", "hit and restored"),
        ("Smith Square Hall", "Q7593525",
         "Thomas Archer's church of St John, Smith Square was gutted by firebombs in 1941. The ruin was restored "
         "and reopened as a concert hall in 1969.",
         "en:Smith Square Hall",
         ("The church was gutted by bombing in 1941", "Thomas Archer", "reopened as a concert hall in 1969"),
         "1236250", "hit and restored"),
        ("St Marylebone Parish Church", "Q211300",
         "A bomb in the churchyard blew out every window and drove pieces of the school railings through the "
         "ceiling. The church stayed closed for repairs until 1949.",
         "en:St Marylebone Parish Church",
         ("blowing out all the windows", "pieces of iron railing", "until 1949"),
         "1239817", "hit and restored"),
        ("Royal College of Surgeons", "Q1584160",
         "A German incendiary bomb hit the college on Lincoln's Inn Fields in 1941. The damage took major "
         "rebuilding in the 1950s and 60s.",
         "en:Royal College of Surgeons of England",
         ("In 1941 a German incendiary bomb hit the college", "major rebuilding during the 1950s and 60s"),
         "1222011", "hit and restored"),
        ("London Palladium", "Q676755",
         "On 11 May 1941 a German parachute mine came down on the theatre without exploding. A Royal Navy bomb "
         "disposal team was sent to make it safe.",
         "en:London Palladium",
         ("unexploded German parachute mine on 11 May 1941", "Royal Navy bomb disposal team"),
         "1210130", "hit and restored"),
        ("British Museum", "Q6373",
         "A bomb in 1940 hit the new Duveen Gallery, built for the Elgin Marbles, which stayed semi-derelict for "
         "22 years. Incendiaries on 10–11 May 1941 destroyed 150,000 books.",
         "en:British Museum",
         ("Duveen Gallery", "semi-derelict for 22 years", "10 to 11 May 1941", "150,000 books"),
         "1130404", "hit and restored"),
        ("St Mark's Church, Regent's Park", "Q27084451",
         "An incendiary bomb on 21 September 1940 burned out the roof and interior, and a second bomb five days "
         "later destroyed the chancel. The church was reconsecrated in October 1957.",
         "en:St Mark's Church, Regent's Park",
         ("21st September 1940", "Five days later a second bomb destroyed the chancel",
          "reconsecrated in October 1957"),
         "1329909", "hit and restored"),
        ("Gray's Inn", "Q157412",
         "Bombs in 1941 almost destroyed the Inn's Hall, chapel and Library. The Library lost a large part of its "
         "collection, though the rare manuscripts had been moved elsewhere.",
         "en:Gray's Inn",
         ("badly damaged during the Blitz in 1941", "the Hall, the chapel, the Library",
          "completely destroyed the Library", "rare manuscripts, which had been moved elsewhere"),
         "1000351", "hit and restored"),
        ("Southwark Cathedral", "Q922967",
         "Southwark took 1,651 high explosive bombs between October 1940 and June 1941. News that the cathedral "
         "itself had been hit was released on 20 February 1941.",
         "en:Southwark Cathedral",
         ("1,651 High Explosive Bombs", "20 February 1941"),
         "1378460", "hit and restored"),
        ("St John's Church, Waterloo", "Q7593564",
         "A bomb in 1940 destroyed the roof and much of the interior, and services moved to the crypt. Restored "
         "by Thomas Ford, it was rededicated in 1951 as the Festival of Britain Church.",
         "en:St John's Church, Waterloo",
         ("struck by a bomb in 1940", "St John's-in-the-crypt", "Thomas Ford", "Festival of Britain Church"),
         "1357954", "hit and restored"),
        ("St John the Divine, Kennington", "Q7593761",
         "Bombs in 1941 wrecked George Edmund Street's church and most of its fittings and stained glass. It "
         "reopened in September 1958 after years of restoration under H. S. Goodhart-Rendel.",
         "en:St John the Divine, Kennington",
         ("George Edmund Street", "severe bomb damage in 1941", "most of the original interior fittings were lost",
          "Goodhart-Rendel, St John the Divine re-opened in September 1958"),
         "1357964", "hit and restored"),
        ("The Old Vic", "Q868806",
         "Air raids damaged the theatre in 1940, and the company spent the war touring from Burnley. It reopened"
         " after the war and was listed Grade II* in 1951.",
         "en:The Old Vic",
         ("damaged in 1940 during air raids", "Burnley", "Grade II* listed building in 1951"),
         "1068710", "hit and restored"),
        ("Waterloo station", "Q795691",
         "Waterloo was bombed several times; a bomb on 7 September 1940 cut the viaduct outside and stopped "
         "trains for 12 days. A 2,000-pound bomb lay undiscovered under York Road until 1959.",
         "en:London Waterloo station",
         ("7 September 1940", "for 12 days", "2,000-pound (910 kg) bomb", "1959"),
         None, "hit and restored"),
        ("Church of Our Most Holy Redeemer", "Q19872024",
         "A bomb hit this Chelsea Catholic church in September 1940 and killed nineteen people. It was repaired "
         "after the war.",
         "en:Church of Our Most Holy Redeemer and St Thomas More, Chelsea",
         ("In September 1940", "killed nineteen people"),
         "1265563", "hit and restored"),
        ("All Saints Notting Hill", "Q4729590",
         "The first bombs fell on the church on 26 September 1940, and it was hit again in March and June 1944. "
         "Neighbouring buildings such as Pinehurst Court were damaged too.",
         "en:All Saints Notting Hill",
         ("26 September 1940", "March and June 1944", "Pinehurst Court"),
         "1080701", "hit and restored"),
        ("Sloane Square station", "Q1530578",
         "A bomb in November 1940 hit a train in the station, killing 37 people and destroying the ticket hall, "
         "escalators and glazed roof.",
         "en:Sloane Square tube station",
         ("November 1940", "killed 37", "destroyed the ticket hall, escalators and the glazed roof"),
         None, "hit and restored"),
        ("Bow Church", "Q4950623",
         "The medieval church was badly bombed in the Blitz. Queen Elizabeth visited in"
         " 1951 to launch its restoration, led by H S Goodhart-Rendel.",
         "en:Bow Church",
         ("considerable bomb damage during the London Blitz", "1951", "Goodhart-Rendel"),
         "1065273", "hit and restored"),
        ("Trinity Green Almshouses", "Q17528170",
         "The 1695 almshouses for retired sailors on Mile End Road were damaged in the war, and those north of the"
         " chapel were destroyed. The London County Council restored them in the 1950s.",
         "en:Trinity Green Almshouses",
         ("those almshouses north of the chapel being destroyed", "restored in the 1950s by London County Council"),
         "1241071", "hit and restored"),

        # ---- rebuilt after ----
        ("Golden Lane Estate", "Q5579624",
         "Council housing of the 1950s on a bomb site north of Cripplegate. In 1950 only about 500 people "
         "still lived in the City.",
         "en:Golden Lane Estate", ("1950s", "Cripplegate", "500 residents"),
         None, "rebuilt after"),
        ("Lansbury Estate", "Q6487332",
         "Laid out from 1949 on a bombed site in Poplar, the estate was begun as the Live Architecture "
         "Exhibition of the 1951 Festival of Britain.",
         "en:Lansbury Estate", ("1949", "Live Architecture Exhibition", "Festival of Britain"),
         None, "rebuilt after"),
        ("Dutch Church, Austin Friars", "Q5317258",
         "German bombs destroyed the medieval church of the Protestant refugees on the night of 15–16 October 1940. "
         "Princess Irene laid the foundation stone of the new church in 1950, and it was finished in 1954.",
         "en:Dutch Church, Austin Friars",
         ("15–16 October 1940", "Princess Irene of the Netherlands", "completed in 1954"),
         "1376620", "rebuilt after"),
        ("City Temple", "Q5123459",
         "The Nonconformist church on Holborn Viaduct was gutted by incendiary bombs in the Blitz. It was rebuilt"
         " and reopened in 1958.",
         "en:City Temple, London",
         ("gutted by fire from incendiary bombs", "reopened in 1958"),
         "1064642", "rebuilt after"),
        ("Guildhall Art Gallery", "Q4968030",
         "The gallery of 1885 was destroyed in 1941 with 164 paintings and drawings in it. The new building opened "
         "in 1999, and the Roman amphitheatre found under the site is shown in its basement.",
         "en:Guildhall Art Gallery",
         ("destroyed in The Blitz in 1941", "164 paintings", "completed in 1999", "Roman amphitheatre"),
         None, "rebuilt after"),
        ("St Anne's Church, Soho", "Q7592480",
         "The church burned out on 24 September 1940 apart from its tower. The tower was kept, and a new church "
         "and community centre were built around it in 1990–91.",
         "en:St Anne's Church, Soho",
         ("24 September 1940", "apart from the tower", "1990–91 rebuilding of the whole church"),
         "1357340", "rebuilt after"),
        ("Notre Dame de France", "Q20713125",
         "The French church off Leicester Square was badly bombed in 1940 and rebuilt in 1953–55 by Hector "
         "Corfiato. Jean Cocteau painted the murals in its Lady Chapel in 1960.",
         "en:Notre Dame de France",
         ("badly damaged by bombing", "1953-55", "Hector Corfiato", "Jean Cocteau (1960)"),
         "1376623", "rebuilt after"),
        ("Central Synagogue", "Q23891205",
         "The synagogue of 1870 on Great Portland Street was destroyed on 10 May 1941. The congregation prayed in "
         "the basement until 1956, and the new building went up on the same site in 1958.",
         "en:Central Synagogue (Great Portland Street)",
         ("10 May 1941", "temporary synagogue was built in the basement", "constructed in 1958 on the same site"),
         None, "rebuilt after"),
        ("Jack Straw's Castle", "Q18358503",
         "The old building on Hampstead Heath was badly damaged in the Blitz. Raymond Erith's replacement dates "
         "from 1964; John Betjeman called it \"a delight\".",
         "en:Jack Straw's Castle, Hampstead",
         ("badly damaged in The Blitz", "Raymond Erith", "dates to 1964", "a delight"),
         "1113189", "rebuilt after"),
        ("St Mary's Church, Islington", "Q7594355",
         "On the third night of the Blitz, 9 September 1940, a bomb destroyed most of the church but left the "
         "tower and spire. The rebuilt church was dedicated in 1956.",
         "en:St Mary's Church, Islington",
         ("9 September 1940", "leaving only the tower and spire intact", "dedicated in 1956"),
         "1195776", "rebuilt after"),
        ("All Hallows, Bow", "Q15059606",
         "Bombs damaged the church in the Second World War. A P Robinson rebuilt it in 1954–1955, keeping only "
         "the core of the old building.",
         "en:All Hallows, Bow",
         ("rebuilt in 1954–1955 by A P Robinson", "retained only the core of the original building"),
         None, "rebuilt after"),
        ("St Paul's, Bow Common", "Q7595106",
         "The Victorian church was largely destroyed in the war. Robert Maguire and Keith Murray's replacement "
         "of 1958–60 is rated one of the best post-war buildings in Britain.",
         "en:St Paul's, Bow Common",
         ("largely destroyed in the Second World War", "1958–60", "Robert Maguire and Keith Murray",
          "one of the best post-war buildings in Britain"),
         "1241881", "rebuilt after"),
        ("St Boniface's German Church", "Q54006848",
         "The German Catholic church in Whitechapel, already damaged by a Zeppelin in 1917, was destroyed in "
         "September 1940. The present Modernist church was built in 1959–60.",
         "en:St Boniface's German Church, Whitechapel",
         ("Zeppelin raid in 1917", "September 1940", "built in 1959–60"),
         "1445649", "rebuilt after"),
        ("St Matthew's, Bethnal Green", "Q7594708",
         "The church was bombed on the first night of the Blitz, and a temporary church was put up inside the "
         "shell. It was rebuilt from 1958 to 1961.",
         "en:St Matthew's, Bethnal Green",
         ("bombed on the first night of the Blitz", "temporary church erected within its bombed-out shell",
          "from 1958 to 1961"),
         "1065051", "rebuilt after"),
        ("St George's Cathedral, Southwark", "Q1451262",
         "Pugin's Catholic cathedral of 1848 was badly bombed; only two chantries and a chapel survived. It "
         "reopened in 1958.",
         "en:St George's Cathedral, Southwark",
         ("erected in 1848", "reopened after extensive war damage in 1958", "two chantries"),
         "1385643", "rebuilt after"),
        ("Christ Church, Southwark", "Q5108713",
         "The church on Blackfriars Road was destroyed by bombing in 1941. The present church was built in 1958.",
         "en:Christ Church, Southwark",
         ("total destruction of the previous building in 1941", "built in 1958"),
         "1395086", "rebuilt after"),
        ("Holy Trinity Church, Rotherhithe", "Q28803238",
         "Incendiaries burned the church on 7 September 1940, and it is called the first British church "
         "destroyed in the war. The new church of the late 1950s has a mural by Hans Feibusch.",
         "en:Holy Trinity Church, Rotherhithe",
         ("7 September 1940", "first British Church to be destroyed in the Second World War", "Hans Feibusch"),
         None, "rebuilt after"),
        ("Church of the Sacred Heart, Camberwell", "Q26676955",
         "The first church on the site was destroyed in a raid on 8–9 October 1941. The Moderne replacement was "
         "built between 1952 and 1958.",
         "en:Church of the Sacred Heart, Camberwell",
         ("8–9 October 1941", "between 1952 and 1958", "Moderne"),
         "1422505", "rebuilt after"),
        ("Christ Church, Lambeth", "Q5108695",
         "The Victorian church on Westminster Bridge Road was bombed, leaving only the Lincoln Memorial Tower. A "
         "smaller church was built beside it; its foundation stone records 1959.",
         "en:Christ Church, Lambeth",
         ("only the adjoining Lincoln Memorial Tower remains", "rebuilding in 1959"),
         None, "rebuilt after"),
        ("Morley College", "Q6912519",
         "The college's Victorian building was destroyed in 1940, while Maufe's 1930s extension survived. A new "
         "building opened in 1958.",
         "en:Morley College",
         ("destroyed in the Blitz in 1940", "Maufe's 1930s extension survived", "completed in 1958"),
         None, "rebuilt after"),
        ("Minet Library", "Q29914103",
         "An incendiary bomb on 8 December 1940 partly destroyed the octagonal library of 1890. It was rebuilt "
         "in 1956 and now holds the Lambeth Archives.",
         "en:Minet Library",
         ("8 December 1940", "rebuilt in 1956", "Lambeth Archives"),
         None, "rebuilt after"),
        ("Chelsea Old Church", "Q5090115",
         "A parachute mine on 14 April 1941 destroyed most of the church and tower. It was rebuilt on the old "
         "foundations and reconsecrated in May 1958.",
         "en:Chelsea Old Church",
         ("14 April 1941", "parachute mine", "In May 1958", "on its old foundations"),
         "1189649", "rebuilt after"),
        ("Our Lady of Victories, Kensington", "Q7110978",
         "Four incendiary bombs fell on the church roof on 13 September 1940 and it burned down. Adrian Gilbert "
         "Scott's new church opened on 16 April 1959.",
         "en:Our Lady of Victories, Kensington",
         ("13 September 1940", "four German incendiary bombs", "Adrian Gilbert Scott", "16 April 1959"),
         "1429916", "rebuilt after"),
        ("St Columba's Church, Pont Street", "Q7592860",
         "The Church of Scotland's London church was destroyed in the raid of 10 May 1941. Edward Maufe rebuilt it "
         "on the same site in 1955.",
         "en:St Columba's Church, Pont Street",
         ("10 May 1941", "rebuilt on the same site in 1955", "Edward Maufe"),
         "1227408", "rebuilt after"),

        # ---- war rooms and shelters ----
        ("Churchill War Rooms", "Q1024854",
         "The government's underground command centre beneath the Treasury building became fully operational "
         "on 27 August 1939 and was abandoned in August 1945.",
         "en:Churchill War Rooms", ("Treasury building", "27 August 1939", "August 1945"),
         None, "war rooms and shelters"),
        ("Admiralty Citadel", "Q26319560",
         "A bomb-proof operations centre for the Admiralty built in 1939 on Horse Guards Parade, with a concrete "
         "roof 20 feet thick. Churchill called it a \"vast monstrosity\"; creeper was planted to hide it.",
         "en:Military citadels under London",
         ("constructed in 1939", "bomb-proof operations centre", "20-foot (6 m) thick concrete roof",
          "vast monstrosity which weighs upon the Horse Guards Parade", "Virginia creeper"),
         "1066638", "war rooms and shelters"),
        ("Brompton Road station", "Q926936",
         "Closed as a station in 1934, its street building was sold to the War Office for £22,000 just before "
         "the war. It became the command centre of the 26th (London) Anti-Aircraft Brigade.",
         "en:Brompton Road tube station",
         ("closed in 1934", "£22,000", "26th (London) Anti-Aircraft Brigade", "command centre"),
         None, "war rooms and shelters"),
        ("Goodge Street station", "Q746880",
         "One of eight deep-level shelters dug under Northern line stations. From 1943 the Supreme "
         "Headquarters Allied Expeditionary Force used it as a reserve headquarters; one entrance is on Chenies "
         "Street.",
         "en:Goodge Street tube station",
         ("deep-level air-raid shelter", "Supreme Headquarters Allied Expeditionary Force", "Chenies Street"),
         None, "war rooms and shelters"),
        ("Belsize Park station", "Q604060",
         "A deep-level shelter was dug beneath the station in the war. Its entrances stand at Haverstock Hill and "
         "Downside Crescent.",
         "en:Belsize Park tube station",
         ("deep-level air-raid shelters", "Haverstock Hill and Downside Crescent"),
         "1401089", "war rooms and shelters"),
        ("Camden Town station", "Q1028430",
         "A bomb damaged the station on 14 October 1940. Soon after, it was picked as one of eight Northern line "
         "stations to get a deep shelter, with entrances on Buck Street and Underhill Street.",
         "en:Camden Town tube station",
         ("14 October 1940", "one of eight stations", "Buck Street"),
         None, "war rooms and shelters"),
        ("Chancery Lane station", "Q1061682",
         "A deep-level shelter was dug under the station in the war, reached from the old station building and "
         "from Furnival Street. Afterwards it became the Kingsway telephone exchange.",
         "en:Chancery Lane tube station",
         ("deep-level air-raid shelter", "Kingsway telephone exchange", "Furnival Street"),
         None, "war rooms and shelters"),
        ("Stockwell station", "Q1549562",
         "The deep shelter beneath the station, two tunnels for about 4,000 people, was finished in September 1942."
         " The government used it until 1944, when it opened to the public.",
         "en:Stockwell tube station",
         ("completed in September 1942", "around 4,000 people", "used by the Government until 1944"),
         None, "war rooms and shelters"),
        ("Clapham Common station", "Q1095075",
         "One of the eight stations with a deep-level shelter beneath them. Both shelter entrances are on "
         "Clapham High Street.",
         "en:Clapham Common tube station",
         ("deep-level air-raid shelter", "Clapham High Street"),
         "1065005", "war rooms and shelters"),
        ("Bethnal Green station", "Q831397",
         "The unfinished station was used as a shelter. On 3 March 1943, 173 people, 62 of them children, died in "
         "a crush on the stairs, the worst civilian loss of the war in Britain.",
         "en:Bethnal Green tube station",
         ("3 March 1943", "173 people, including 62 children", "largest loss of civilian life"),
         None, "war rooms and shelters"),
        ("St Peter's Church, Walworth", "Q7595299",
         "Between 600 and 900 people sheltered in Soane's crypt every night. A bomb on 29 October 1940 killed more "
         "than 30 of them outright; 67 died in the end.",
         "en:St Peter's Church, Walworth",
         ("between 600 and 900 people", "29 October 1940", "67 eventually died"),
         "1385662", "war rooms and shelters"),
        ("St Pancras New Church", "Q7595040",
         "The Greek Revival church's crypt was an air-raid shelter in both world wars. It is now used as an art "
         "gallery.",
         "en:St Pancras New Church",
         ("air-raid shelter in both world wars", "art gallery"),
         "1379062", "war rooms and shelters"),
        ("St James's Church, Paddington", "Q16684477",
         "Its crypt served as an air-raid shelter in 1940, while the church above was badly damaged. It reopened "
         "in July 1958.",
         "en:St James's Church, Paddington",
         ("church crypt was used as an air-raid shelter", "reopened in July 1958"),
         "1237437", "war rooms and shelters"),
        ("Finsbury Town Hall", "Q60790762",
         "An air-raid shelter and control centre was built under Garnault Place, entered from the town hall. In "
         "the Cold War it was kept as a nuclear fall-out shelter.",
         "en:Finsbury Town Hall",
         ("air raid shelter and control centre", "Garnault Place", "nuclear fall-out shelter"),
         "1293112", "war rooms and shelters"),
        ("Stoke Newington Town Hall", "Q26545214",
         "The town hall was the local civil defence headquarters in the war. It was heavily camouflaged so that "
         "bombers could not pick it out.",
         "en:Stoke Newington Town Hall",
         ("civil defence headquarters", "heavily camouflaged"),
         "1253465", "war rooms and shelters"),
        ("Electra House, Moorgate", "Q15216419",
         "The telegraph company's building was the base of Department EH, one of three bodies merged to form the "
         "Special Operations Executive. It was bombed but still stands.",
         "en:Electra House",
         ("Department EH", "Special Operations Executive", "Both Electra House buildings were bombed"),
         "1251605", "war rooms and shelters"),
        ("The Dorchester", "Q2749941",
         "Opened in 1931 and billed as bomb-proof, the hotel lost only some windows to the Luftwaffe. Its Turkish "
         "baths became a private shelter for well-off guests.",
         "en:The Dorchester",
         ("18 April 1931", "bomb-proof, earthquake-proof and fireproof", "several broken windows", "Turkish baths"),
         "1225963", "war rooms and shelters"),

        # ---- V-weapons ----
        ("Guards' Chapel", "Q5614129",
         "A V-1 flying bomb hit the chapel during the Sunday service on 18 June 1944. The roof fell on the "
         "congregation and killed 121 people; a new chapel was built in 1963.",
         "en:Guards' Chapel, Wellington Barracks",
         ("18 June 1944", "V-1 flying bomb", "121 people killed", "Modernist style in 1963"),
         "1066441", "V-weapons"),
        ("St Michael Paternoster Royal", "Q3583162",
         "A V-1 flying bomb on 23 July 1944 left only the walls and tower of Wren's church. It was restored in "
         "1966–68, the latest City church to be restored, as the Mission to Seamen's headquarters.",
         "en:St Michael Paternoster Royal",
         ("23 July 1944", "V-1 flying bomb", "between 1966 and 1968", "latest City church to be restored",
          "Mission to Seamen"),
         "1286707", "V-weapons"),
        ("Bush House", "Q852282",
         "The BBC European Service moved in after Broadcasting House was bombed on 8 December 1940. In 1944 a "
         "V-1 flying bomb damaged the building's exterior.",
         "en:Bush House",
         ("BBC European Service", "8 December 1940", "V-1 flying bomb"),
         "1066492", "V-weapons"),
        ("Victoria station", "Q985210",
         "The station was bombed several times in 1940 and 1941 and a plane crashed into it on 15 September 1940. "
         "A flying bomb damaged part of it on 27 June 1944.",
         "en:London Victoria station",
         ("15 September 1940", "a flying bomb caused partial damage on 27 June 1944"),
         "1266689", "V-weapons"),
        ("Dulwich Picture Gallery", "Q1241163",
         "A V-1 on 12 July 1944 wrecked Soane's mausoleum and west galleries and scattered bones across the "
         "lawn. The restored gallery reopened on 27 April 1953.",
         "en:Dulwich Picture Gallery",
         ("12 July 1944", "bones were scattered across the lawn", "27 April 1953"),
         "1385543", "V-weapons"),
        ("St Cuthbert's, Earls Court", "Q15139002",
         "A V-1 that fell opposite the east end on 2 August 1944 killed three people and blew out the Lady "
         "Chapel windows. Glass from the blast was found embedded in the church in the early 2000s.",
         "en:St Cuthbert's, Earls Court",
         ("2 August 1944", "killed three people", "glass was found embedded", "Lady Chapel windows were blown out"),
         "1266119", "V-weapons"),
        ("All Saints Church, West Dulwich", "Q4729538",
         "A V-1 flying bomb exploded near the church in June 1944, shattering its stained glass and damaging the "
         "roof.",
         "en:All Saints Church, West Dulwich",
         ("In June 1944 a V-1 flying bomb exploded near the church", "shattering the stained glass windows"),
         "1064976", "V-weapons"),
        ("Odeon Holloway", "Q26664794",
         "A V-1 hit the cinema on 8 November 1944. The outer walls and foyers survived, but the interior was "
         "destroyed.",
         "en:Odeon Cinema, Holloway",
         ("8 November 1944", "V-1 flying bomb", "the external walls and foyers survived"),
         "1384986", "V-weapons"),
        ("All Saints Church, Poplar", "Q4729513",
         "Hundreds of people sheltered in the crypt through the Blitz. Late in the war a V-2 rocket destroyed the "
         "east end and brought down the roof.",
         "en:All Saints Church, Poplar",
         ("crypt as an air-raid shelter", "V-2 rocket devastated the building", "bringing down the roof"),
         "1240311", "V-weapons"),
        ("St Dunstan's, Stepney", "Q7592980",
         "The streets around the church were flattened, but it escaped lightly until a V-2 landed in the "
         "churchyard in January 1945, damaging the tower and the stained glass.",
         "en:St Dunstan's, Stepney",
         ("V2 ballistic missile", "January 1945", "damaging the tower"),
         "1065065", "V-weapons"),
        ("St Michael and All Angels, London Fields", "Q26670899",
         "A V-2 rocket on 5 February 1945 left the Victorian church a partial ruin. N. F. Cachemaille-Day "
         "designed the replacement, built in 1959–61.",
         "en:Church of St Michael and All Angels, London Fields",
         ("5 February 1945", "V-2 rocket", "between 1959 and 1961", "Cachemaille-Day"),
         "1391543", "V-weapons"),
        ("American International Church", "Q19587074",
         "Whitefield's Tabernacle on Tottenham Court Road was destroyed by a V-2 rocket on Palm Sunday 1945, one "
         "of the last to fall on London. A new chapel was built in 1957.",
         "en:American International Church",
         ("Palm Sunday 1945", "last V-2 rocket to fall on London", "A new chapel was built in 1957"),
         None, "V-weapons"),

        # ---- memorials: buildings that keep their war damage ----
        ("Victoria and Albert Museum", "Q213322",
         "Two bombs fell on Exhibition Road in November 1940. The pockmarks they left in the stonework are still "
         "visible on that side of the museum.",
         "en:Victoria and Albert Museum",
         ("In November 1940, two bombs landed in Exhibition Road",
          "pockmarks in the stonework visible on Exhibition Road"),
         None, "memorials"),
        ("Selfridges", "Q7448348",
         "The store was hit in 1940, 1941 and 1944; a V-2 struck the Red Lion pub next door on 6 December 1944. "
         "Its building still bears the scars of war damage.",
         "en:Selfridges flagship store",
         ("17 April 1941", "6 December 1944", "Red Lion pub", "still bears the scars of war damage"),
         "1357436", "memorials"),
        ("St Matthias Old Church", "Q7594715",
         "Poplar was heavily bombed, but the 1654 East India Company chapel survived. Shards of shrapnel are "
         "still buried in some of its walls.",
         "en:St Matthias Old Church",
         ("Poplar was heavily bombed", "shards of shrapnel buried in some of the walls", "1654"),
         "1065793", "memorials"),
        ("Westminster Abbey", "Q5933",
         "Incendiaries hit the roof on the night of 10–11 May 1941 and a bomb destroyed the lantern over the "
         "crossing, restored in 1958. A small hole made by a bomb can still be seen in the RAF Chapel.",
         "en:Westminster Abbey",
         ("In 1941, on the night of 10 May", "roof lantern which was destroyed by a bomb in 1941",
          "small hole in the wall", "RAF Chapel"),
         "1291494", "memorials"),
        ("Palace of Westminster", "Q62408",
         "Bombs hit the palace fourteen times, and the Commons chamber was destroyed in 1941; Giles Gilbert Scott's"
         " new chamber opened in 1950. The arch into it was left unrepaired as the Churchill Arch.",
         "en:Palace of Westminster",
         ("fourteen separate occasions", "destroyed in 1941", "Giles Gilbert Scott", "Churchill Arch",
          "left unrepaired as a reminder of the evils of war"),
         "1226284", "memorials"),
    ],
)
