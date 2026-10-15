"""DRAFT hand-curated context layers for inner London: buildings standing today, grouped by theme, each with a short
story and a source.

Scope: City of London, Westminster, Camden, Islington, Kensington and Chelsea, Southwark, Lambeth, Tower Hamlets,
Hackney. Buildings are placed by the coordinates (P625) of their Wikidata item, not by address.

Entry format: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE number (P1216) or None, group).
The 7th element, group, is optional (a sub-group within the layer). Every string in `checks` appears (case-sensitive)
in the plain-text extract of the en.wikipedia article (API prop=extracts, explaintext=1, redirects=1); all checks were
run on 2026-10-15. Each QID was checked via Special:EntityData: it has P625, and the nearest postcode to that point
(postcodes.io) lies in one of the nine boroughs. NHLE numbers are copied from P1216 where the item has one.

Dropped during research:
- Katharine Buildings (East Smithfield, 1885, Beatrice Potter as rent collector): demolished in the 1970s.
- Trident Studios (17 St Anne's Court): the article covers the studio of 1968-1981 only; unclear what survives.
- Royal Institution (Faraday): the Wikidata item is the organisation; no separate item for 21 Albemarle Street.
- Chinese Legation, 49 Portland Place (Sun Yat-sen held there in 1896): Wikidata has only the embassy as an
  institution, no building item.
- 4 Carlton Gardens (de Gaulle's Free French HQ), 8 Royal College Street (Rimbaud and Verlaine), 28 Dean Street
  (Marx), 46 Gordon Square (Bloomsbury Group): no Wikidata building items; the articles found are streets/squares.
- Ho Chi Minh (Carlton Hotel, demolished), Lenin's home in Holford Square (bombed; Bevin Court stands on it, used in
  'housing'), Herzen: no surviving building with an item found.
- Peabody's first block (Commercial Street, 1864), Millbank Estate, Ivory House (St Katharine Docks), Old Curiosity
  Shop, Cadogan Hotel (Wilde's arrest), Leinster Gardens false fronts: no Wikidata building item.
- Ronnie Scott's, Smithfield Market: Wikidata items without usable coordinates.
- Prince Albert's Model Cottage (Kennington Park): its Wikidata coordinate falls in East Hertfordshire.
- Spaniards Inn (Barnet), Battersea Power Station (Wandsworth), Pitzhanger Manor and Hoover Building (Ealing), Old
  Royal Naval College (Greenwich), Bethlem Royal Hospital (Bromley): outside the nine boroughs.
- Bedford Square, Fitzroy Square, Carlton House Terrace, St Katharine Docks, Smithfield, World's End: Wikidata items
  are squares, streets, a marina or areas rather than buildings.
- Lincoln's Inn, Gray's Inn, Inner Temple, Middle Temple: items are the institutions; Middle Temple Hall (Q17526789)
  is used instead.
- Thames Tunnel (a tunnel): the Brunel Engine House is used instead.
- Highgate Cemetery, Bunhill Fields, Abney Park: burial grounds, not buildings.
- London Mithraeum: a reconstructed Roman temple inside the Bloomberg building; not a building of its own.
- Verified but cut for length: Hayward Gallery, Economist Building (modern), Elizabeth Tower/Big Ben (power; kept as
  a 'Did you know' fact instead).

Doubts to check before publishing:
- Several QIDs are institution-type items that carry the building's coordinates (most also have an NHLE number):
  Marx Memorial Library, Toynbee Hall, Whitechapel Gallery, Wigmore Hall, Royal Hospital Chelsea, Great Ormond Street
  Hospital, St Mary's Hospital, Science Museum, Wellcome Collection, Foundling Museum, Freud Museum, Fortnum & Mason,
  Borough Market, London Museum Docklands (for the West India Quay warehouses), Brunel Museum (for the Engine House),
  Churchill War Rooms, Imperial War Museum, Hatchards, 100 Club, Café de Paris, Electric Ballroom, Whitechapel Bell
  Foundry, Twinings (Q7858373 is the Strand shop, not the company). If the map needs strict building items, these
  are the first to re-check.
- Estates are single Wikidata points over many blocks (Boundary, Bourne, Ossulston, Churchill Gardens, Hallfield,
  Lillington Gardens, Dawson's Heights, Alexandra Road, Golden Lane, Lansbury, Barbican, Sutton Dwellings): the map
  will highlight whichever building the point falls on.
- P576 (end date) is set on St Helen's Bishopsgate, Temple Church, the Charterhouse, St Bartholomew-the-Great,
  Christ Church Greyfriars and St Dunstan-in-the-East. It records a dissolution or wartime destruction; the churches
  stand, and the two ruins are kept deliberately in 'blitz'.
- The borough test uses the nearest postcode, not a boundary polygon. The Imperial War Museum came back as Southwark
  (it is in Lambeth); every point is inside the nine boroughs either way, but a polygon test is better.
- Kensington Roof Gardens closed to the public in 2018; the garden still exists on the Derry & Toms building.
- Café de Paris reopened in 2023 as Lío London; Whitechapel Bell Foundry closed as a business in 2017 (building
  stands); 19 Princelet Street opens only for group visits and is on the Buildings at Risk register.
- St Mary's Hospital: the story is about Fleming's laboratory, but the QID is the whole hospital.
- Burlington House story rests on the Linnean Society article, not on Burlington House's own.
- Three layers share the 'Discover' section (exiles, pubs, secrets); 'exiles' could move to another section.
- 16 layers (the top of the 12-16 target), 213 entries; 'secrets' or 'exiles' are the easiest to fold if fewer
  are wanted.
"""

CURATED = [
    dict(
        id="fire", section="War and disaster", title="After the Great Fire", era="1666–1710",
        intro=("The fire that started in a baker's shop in Pudding Lane on 2 September 1666 burned for four days "
               "and destroyed most of the medieval City. Christopher Wren's office rebuilt St Paul's and more "
               "than fifty parish churches. A few buildings that the flames missed still stand beside them."),
        entries=[
            ("The Monument", "Q607700",
             "A Doric column designed by Robert Hooke and built between 1671 and 1677. It is 202 feet tall and "
             "stands 202 feet from the spot in Pudding Lane where the fire began.",
             "en:Monument to the Great Fire of London", ("Robert Hooke", "1671 and 1677", "202 feet", "Pudding Lane"),
             "1193901", "rebuilt"),
            ("St Paul's Cathedral", "Q173882",
             "Wren's cathedral replaced the medieval church lost in the fire and was completed in 1710. At 365 "
             "feet it was the tallest building in London until 1963.",
             "en:St Paul's Cathedral", ("completed in 1710", "365 ft", "from 1710 to 1963"),
             "1079157", "rebuilt"),
            ("St Mary-le-Bow", "Q2301992",
             "Wren's rebuilding of this Cheapside church cost over £15,000, more than any of his parish churches."
             " Traditionally, anyone born within earshot of its bells was a Cockney.",
             "en:St Mary-le-Bow", ("£15,000", "Cockney"),
             "1064696", "rebuilt"),
            ("St Bride's Church", "Q1112579",
             "Wren designed the church in 1672; its 226-foot steeple is the second highest he built. Tiered "
             "wedding cakes are said to date from 1703, when a baker's apprentice on Ludgate Hill drew on its "
             "design.",
             "en:St Bride's Church", ("1672", "226 feet", "wedding cakes", "1703", "Ludgate Hill"),
             "1064657", "rebuilt"),
            ("St Stephen Walbrook", "Q952386",
             "Wren gave this church, next to the Mansion House, a dome. In 1953 its rector Chad Varah founded the"
             " Samaritans here, and a telephone is kept in a glass box in the church.",
             "en:St Stephen Walbrook", ("Mansion House", "1953", "Chad Varah", "glass box"),
             "1285320", "rebuilt"),
            ("St Vedast Foster Lane", "Q7595600",
             "The fire left the church badly damaged. Wren rebuilt it on the old walls between 1670 and 1673 for "
             "£1,853, the cheapest of all his City commissions.",
             "en:St Vedast Foster Lane", ("1670–1673", "£1,853", "cheapest"),
             "1064666", "rebuilt"),
            ("St Mary Aldermary", "Q916327",
             "Rebuilding of the medieval church was finished only in 1632, 33 years before the fire. Wren's "
             "office rebuilt it again, unusually in the Gothic style.",
             "en:St Mary Aldermary", ("1632", "33 years", "Gothic"),
             "1079145", "rebuilt"),
            ("St James Garlickhythe", "Q7593494",
             "Rebuilt by Wren's office after the fire, the church has so many windows that it is nicknamed "
             "\"Wren's lantern\". Garlic was once landed and sold at the nearby hythe.",
             "en:St James Garlickhythe", ("Wren's lantern", "garlic"),
             "1064669", "rebuilt"),
            ("St Lawrence Jewry", "Q11704046",
             "Wren rebuilt the church next to the Guildhall after the fire. It is the official church of the Lord"
             " Mayor, and its weathervane is a gridiron, the instrument of St Lawrence's martyrdom.",
             "en:St Lawrence Jewry", ("Lord Mayor", "gridiron"),
             "1064673", "rebuilt"),
            ("Temple Bar", "Q1256932",
             "Wren's gateway once stood where Fleet Street meets the Strand. Taken down in 1878, it spent over a "
             "century in a Hertfordshire park and was re-erected by Paternoster Square in 2004.",
             "en:Temple Bar, London", ("Theobalds Park", "Paternoster Square", "2004"),
             "1393844", "rebuilt"),
            ("St Olave Hart Street", "Q2688896",
             "One of the few medieval City churches the fire missed. Samuel Pepys, who lived on Seething Lane, "
             "called it \"our own church\" and was buried here in 1703.",
             "en:St Olave's Church, Hart Street", ("Great Fire of London in 1666", "Seething Lane", "our own church", "1703"),
             "1064676", "survived"),
            ("St Helen's Bishopsgate", "Q7593309",
             "The largest surviving parish church in the City escaped both the fire and the Blitz. Shakespeare "
             "was a parishioner when he lived nearby in the 1590s.",
             "en:St Helen's Church, Bishopsgate", ("largest surviving parish church", "Shakespeare", "1590s", "Blitz"),
             "1286458", "survived"),
            ("Prince Henry's Room", "Q7244068",
             "The house at 17 Fleet Street was rebuilt in 1610 as a tavern and is one of the few City buildings "
             "older than the fire. Pepys drank there in 1661.",
             "en:Prince Henry's Room", ("17 Fleet Street", "1610", "Pepys", "1661"),
             None, "survived"),
            ("Middle Temple Hall", "Q17526789",
             "The hall survived the fire of 1666. The first recorded performance of Shakespeare's Twelfth Night "
             "took place here on 2 February 1602.",
             "en:Middle Temple", ("survived the Great Fire", "Twelfth Night", "2 February 1602"),
             "1064609", "survived"),
        ]),
    dict(
        id="blitz", section="War and disaster", title="The Blitz", era="1940–1941",
        intro=("German bombing between September 1940 and May 1941 burned out much of the City and hit every "
               "inner borough. Some buildings were restored, some were left as ruins and gardens, and the worst-"
               "hit areas were rebuilt as new estates."),
        entries=[
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
            ("Churchill War Rooms", "Q1024854",
             "The government's underground command centre beneath the Treasury building became fully operational "
             "on 27 August 1939 and was abandoned in August 1945.",
             "en:Churchill War Rooms", ("Treasury building", "27 August 1939", "August 1945"),
             None, "command"),
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
        ]),
    dict(
        id="power", section="Power and the crown", title="Crown, parliament and courts", era="1080s–1902",
        intro=("For nine centuries the monarch, parliament and the law courts have sat within a few miles of each"
               " other on the Thames. Palaces were burned, replaced and handed over to new uses, and some of "
               "their oldest parts are still in use."),
        entries=[
            ("White Tower", "Q1528473",
             "William the Conqueror built the keep of the Tower of London in the early 1080s. Henry III had it "
             "whitewashed in 1240, which gave it its name.",
             "en:White Tower (Tower of London)", ("William the Conqueror", "early 1080s", "whitewashed in 1240"),
             "1260258", "palaces"),
            ("Westminster Abbey", "Q5933",
             "Every coronation since 1066 has taken place here: 40 monarchs so far. The present church was begun "
             "in 1245 on the orders of Henry III.",
             "en:Westminster Abbey", ("Since 1066", "coronations of 40", "1245", "Henry III"),
             "1291494", "church and crown"),
            ("Westminster Hall", "Q114004148",
             "Built in 1097 for William II, it got its hammerbeam roof in 1393. The hall survived the fire of "
             "1834 that destroyed most of the old palace.",
             "en:Westminster Hall", ("1097", "William II", "1393", "fire of 1834"),
             None, "parliament"),
            ("Palace of Westminster", "Q62408",
             "A fire in 1834 destroyed most of the medieval palace. The Gothic building that replaced it houses "
             "both the House of Commons and the House of Lords.",
             "en:Palace of Westminster", ("In 1834", "House of Commons", "House of Lords"),
             "1226284", "parliament"),
            ("Jewel Tower", "Q1568148",
             "Built in 1365–1366 to hold the personal treasure of Edward III, this is one of the few parts of the"
             " medieval palace to survive. It once stood behind a moat linked to the Thames.",
             "en:Jewel Tower", ("1365 and 1366", "Edward III", "moat"),
             "1225529", "parliament"),
            ("Banqueting House", "Q642039",
             "Inigo Jones's building of 1619–1622 is the only large surviving part of the Palace of Whitehall, "
             "which burned in 1698. Charles I was executed outside it.",
             "en:Banqueting House", ("1619", "1622", "Inigo Jones", "execution outside Banqueting House", "1698"),
             "1357353", "palaces"),
            ("St James's Palace", "Q272162",
             "Henry VIII built the palace in the 1530s on the site of a leper hospital. Foreign ambassadors are "
             "still accredited to the Court of St James's.",
             "en:St James's Palace", ("Henry VIII", "1530s", "leper hospital", "Court of St James's"),
             "1264851", "palaces"),
            ("Buckingham Palace", "Q42182",
             "The core is a townhouse built for the Duke of Buckingham in 1703. George III bought it in 1761 for "
             "Queen Charlotte.",
             "en:Buckingham Palace", ("1703", "George III", "1761", "Queen Charlotte"),
             "1239087", "palaces"),
            ("Kensington Palace", "Q207385",
             "The future Queen Victoria was born here on 24 May 1819 and christened in the Cupola Room. Its state"
             " rooms are now open to the public.",
             "en:Kensington Palace", ("24 May 1819", "Cupola Room"),
             "1223861", "palaces"),
            ("Clarence House", "Q565521",
             "Built in 1825–1827 to designs by John Nash for the future William IV. It was heavily damaged in the"
             " Blitz, and little of Nash's work remains.",
             "en:Clarence House", ("1825–1827", "William IV", "John Nash", "Blitz"),
             "1236580", "palaces"),
            ("Marlborough House", "Q565532",
             "Built in 1711 for Sarah Churchill, Duchess of Marlborough, a confidante of Queen Anne. It is now "
             "the headquarters of the Commonwealth.",
             "en:Marlborough House", ("1711", "Sarah Churchill", "Queen Anne", "Commonwealth of Nations"),
             "1331701", "palaces"),
            ("10 Downing Street", "Q169101",
             "George II offered the house to Robert Walpole, who moved in on 22 September 1735. It has about 100 "
             "rooms.",
             "en:10 Downing Street", ("George II", "Robert Walpole", "London Daily Post", "100 rooms"),
             "1210759", "parliament"),
            ("Lambeth Palace", "Q1130266",
             "The London home of the Archbishop of Canterbury since about 1200. Its brick gatehouse, Morton's "
             "Tower, was completed in 1495.",
             "en:Lambeth Palace", ("Archbishop of Canterbury", "1200", "Morton's Tower", "1495"),
             "1000818", "church and crown"),
            ("Royal Courts of Justice", "Q609835",
             "George Edmund Street designed the Gothic law courts but died before they were finished. Queen "
             "Victoria opened them in 1882.",
             "en:Royal Courts of Justice", ("George Edmund Street", "died before it was completed", "1882"),
             "1264258", "courts"),
            ("Old Bailey", "Q1194829",
             "The Central Criminal Court stands on the site of Newgate Prison. Its main building by Edward "
             "Mountford was completed in 1902.",
             "en:Old Bailey", ("Newgate Prison", "1902", "Mountford"),
             "1359218", "courts"),
        ]),
    dict(
        id="georgian", section="Architecture", title="Georgian town houses and terraces", era="1704–1833",
        intro=("In the eighteenth century the aristocracy built grand houses in the new West End, and architects "
               "such as Robert Adam and William Chambers brought classical design to London. After 1811 John Nash"
               " laid out Regent Street and the stucco terraces of Regent's Park for the Prince Regent."),
        entries=[
            ("Burgh House", "Q4998622",
             "Built in 1704, in the reign of Queen Anne, when Hampstead's spa was flourishing. The spa's "
             "physician moved in in 1720.",
             "en:Burgh House", ("1704", "Queen Anne", "1720"),
             "1113163", "houses"),
            ("Spencer House", "Q2505545",
             "Commissioned in 1756 by John Spencer, later the first Earl Spencer. James \"Athenian\" Stuart gave it"
             " Greek interiors, making it one of the first neoclassical buildings in London.",
             "en:Spencer House, Westminster", ("1756", "first Earl Spencer", "Athenian", "neoclassical"),
             "1264952", "houses"),
            ("Mansion House", "Q1786933",
             "George Dance designed the Lord Mayor's official residence in the Palladian style; it was built "
             "between 1739 and 1752.",
             "en:Mansion House, London", ("George Dance", "Palladian", "between 1739 and 1752"),
             "1064604", "houses"),
            ("Chandos House", "Q5071247",
             "Robert Adam's house at 2 Queen Anne Street was built speculatively in 1769–1771. Its front is of "
             "Craigleith stone from near Edinburgh.",
             "en:Chandos House", ("Robert Adam", "1769", "1771", "Craigleith stone"),
             "1227332", "houses"),
            ("Albany", "Q2637274",
             "William Chambers built it in 1771–1776 as Melbourne House. In 1802 the mansion was divided into "
             "apartments.",
             "en:Albany (London)", ("1771–1776", "Melbourne House", "1802"),
             "1209755", "houses"),
            ("Home House", "Q5888425",
             "The Countess of Home hired James Wyatt for her house at 20 Portman Square in 1776, then replaced "
             "him with Robert Adam. It is now a private members' club.",
             "en:Home House", ("20 Portman Square", "1776", "James Wyatt", "Robert Adam"),
             "1227105", "houses"),
            ("Apsley House", "Q622206",
             "Robert Adam built it for Lord Apsley in the 1770s. The Duke of Wellington owned it from 1817, and "
             "it was known as Number One, London.",
             "en:Apsley House", ("Robert Adam", "1770s", "1817", "Number One, London"),
             "1226873", "houses"),
            ("Kenwood House", "Q764804",
             "Robert Adam remodelled the house for the Earl of Mansfield. Edward Guinness, Earl of Iveagh, bought"
             " it in 1925 and gave it to the nation in 1927.",
             "en:Kenwood House", ("Robert Adam", "Earl of Mansfield", "1925", "1927"),
             "1379242", "houses"),
            ("Somerset House", "Q1344889",
             "William Chambers's building, begun in 1776, was built to house government offices and learned "
             "societies. The building stood directly on the Thames until the Victoria Embankment was built in the"
             " late 1860s.",
             "en:Somerset House", ("William Chambers", "1776", "Victoria Embankment"),
             "1237041", "public buildings"),
            ("Sir John Soane's Museum", "Q2060860",
             "The architect John Soane had an Act of Parliament passed in 1833 so that his house and collection "
             "would be kept as they were at his death, partly to disinherit his son.",
             "en:Sir John Soane's Museum", ("1833", "disinherit his son", "1837"),
             "1379327", "houses"),
            ("All Souls, Langham Place", "Q4729656",
             "John Nash designed the church, consecrated in 1824, with a round spired porch to mark the bend "
             "where Regent Street turns west.",
             "en:All Souls Church, Langham Place", ("John Nash", "1824", "Regent Street"),
             "1221802", "Nash"),
            ("Park Crescent", "Q7137707",
             "Nash's stuccoed semicircle at the top of Portland Place was first planned as a full circus called "
             "Regent's Circus.",
             "en:Park Crescent, London", ("John Nash", "Portland Place", "Regent's Circus"),
             "1225959", "Nash"),
            ("Chester Terrace", "Q3639277",
             "Its facade of about 280 metres is the longest unbroken one in Regent's Park. Nash so disliked "
             "Decimus Burton's changes that he wanted it demolished and rebuilt.",
             "en:Chester Terrace", ("280 metres", "Decimus Burton", "demolition"),
             "1271885", "Nash"),
            ("Cumberland Terrace", "Q3007519",
             "Completed in 1826, the terrace was meant to face a palace the Prince Regent planned in Regent's "
             "Park, which was never built.",
             "en:Cumberland Terrace", ("1826", "John Nash", "proposed palace"),
             "1067386", "Nash"),
            ("Wellington Arch", "Q526804",
             "Decimus Burton's arch at Hyde Park Corner was built in 1826–1830 as an approach to Buckingham "
             "Palace. In 1882–1883 it was taken down and rebuilt a short distance away.",
             "en:Wellington Arch", ("Decimus Burton", "1826 and 1830", "1882–1883"),
             "1278092", "public buildings"),
        ]),
    dict(
        id="housing", section="The modern city", title="Housing the city", era="1865–1978",
        intro=("Victorian philanthropists built the first model dwellings for the poor, and from 1890 the London "
               "County Council began to build its own estates. After the Second World War the boroughs cleared "
               "slums and bomb sites and put up modernist estates, several of them now listed."),
        entries=[
            ("Holly Village", "Q17548853",
             "Twelve Gothic cottages around a private garden in Highgate, completed in 1865 and funded by the "
             "philanthropist Angela Burdett-Coutts. Her name is carved over the gate.",
             "en:Holly Village", ("12 cottages", "1865", "Burdett-Coutts", "Holly Village erected by AGB Coutts"),
             "1379116", "philanthropy"),
            ("Boundary Estate", "Q4949934",
             "One of the first council housing schemes, built from 1890 on the site of the Old Nichol slum. Soil "
             "from the foundations was heaped into the mound at Arnold Circus.",
             "en:Boundary Estate", ("1890", "Old Nichol", "Arnold Circus"),
             None, "London County Council"),
            ("Bourne Estate", "Q4950237",
             "London County Council tenements built in 1905–1909 in Holborn, around courtyards planted with plane"
             " trees.",
             "en:Bourne Estate", ("1905–1909", "London County Council", "London planes"),
             None, "London County Council"),
            ("Sutton Dwellings", "Q24022959",
             "The William Sutton Trust bought a block of overcrowded houses in Chelsea in 1908 and replaced them "
             "with 14 red-brick buildings, finished in 1913, for 2,200 people.",
             "en:Sutton Dwellings", ("1908", "William Sutton Trust", "14 red-brick", "1913", "2,200 people"),
             None, "philanthropy"),
            ("Ossulston Estate", "Q7107545",
             "Built by the LCC between 1927 and 1931 on the site of the Somers Town slum, between Euston and St "
             "Pancras. Its modernist design was unusual for council housing at the time.",
             "en:Ossulston Estate", ("1927 and 1931", "Somers Town", "Euston and St Pancras"),
             None, "London County Council"),
            ("Kensal House", "Q17552433",
             "Maxwell Fry designed these two curved blocks, completed in 1937 for the Gas Light and Coke Company."
             " It was the first modernist block in Britain designed for working-class tenants.",
             "en:Kensal House", ("Maxwell Fry", "1937", "Gas Light and Coke Company", "first modernist block"),
             "1225244", "philanthropy"),
            ("Spa Green Estate", "Q7572145",
             "Berthold Lubetkin's estate in Clerkenwell was completed in 1949. A restoration in 2008 brought back"
             " its original colour scheme.",
             "en:Spa Green Estate", ("Lubetkin", "1949", "2008"),
             None, "post-war"),
            ("Bevin Court", "Q4899667",
             "Built on bomb-destroyed Holford Square, where Lenin lived in 1902–03, and planned as Lenin Court. "
             "By the time it was finished in 1954 the Cold War had begun, and it was named after Ernest Bevin "
             "instead.",
             "en:Bevin Court", ("Holford Square", "1902–03", "Lenin Court", "1954", "Cold War", "Ernest Bevin"),
             "1246687", "post-war"),
            ("Churchill Gardens", "Q5118180",
             "Powell and Moya's estate of 1,600 homes in Pimlico, built between 1946 and 1962 on blitzed "
             "terraces, is the only housing project completed under the Abercrombie Plan.",
             "en:Churchill Gardens", ("1,600 homes", "1946 and 1962", "Abercrombie Plan"),
             None, "post-war"),
            ("Hallfield Estate", "Q5642944",
             "Designed by Lubetkin's Tecton practice and built by Denys Lasdun and Lindsay Drake in 1951–58: 15 "
             "blocks over about 17 acres of Bayswater.",
             "en:Hallfield Estate", ("Tecton", "Lindsay Drake", "15 blocks", "17 acres"),
             "1402283", "post-war"),
            ("Keeling House", "Q6382807",
             "Denys Lasdun's 16-storey cluster block in Bethnal Green was completed in 1957. Tower Hamlets could "
             "not afford to repair it and sold it in 1999; it was turned into private flats.",
             "en:Keeling House", ("16-storey", "1957", "1999"),
             "1242108", "post-war"),
            ("Lillington Gardens", "Q6548293",
             "Built in Pimlico between 1961 and 1971 to a plan by Darbourne & Darke, it reached high density with"
             " medium-rise blocks, roof streets and private gardens.",
             "en:Lillington Gardens", ("1961 and 1971", "Darbourne & Darke", "roof streets"),
             None, "post-war"),
            ("Dawson's Heights", "Q60742636",
             "Kate Macintosh designed the two blocks, built between 1964 and 1972 on a spoil tip left by a "
             "railway line in East Dulwich.",
             "en:Dawson's Heights", ("Kate Macintosh", "1964 and 1972", "spoil tip"),
             None, "post-war"),
            ("Alexandra Road Estate", "Q4720740",
             "Neave Brown of Camden's architects' department designed it in 1968; the 520 flats in white board-"
             "marked concrete were completed in 1978.",
             "en:Alexandra Road Estate", ("Neave Brown", "1968", "520 apartments", "1978"),
             "1130403", "post-war"),
        ]),
    dict(
        id="modern", section="Architecture", title="Concrete, glass and steel", era="1932–2014",
        intro=("London's twentieth-century buildings range from 1930s experiments in modern living to the "
               "Brutalist concrete of the 1960s and 1970s and the City towers of the last thirty years. Several "
               "were disliked when new and are now listed."),
        entries=[
            ("Daily Express Building", "Q5209252",
             "Designed in 1932 for the Daily Express, with a black front of vitrolite and glass on Fleet Street. "
             "Its art deco lobby was designed by Robert Atkinson.",
             "en:Daily Express Building, London", ("1932", "vitrolite", "Robert Atkinson"),
             "1064659", "between the wars"),
            ("Isokon building", "Q3296317",
             "Wells Coates's concrete block of small flats with a communal kitchen opened in 1934. Walter "
             "Gropius, Marcel Breuer and Agatha Christie lived here.",
             "en:Isokon Flats", ("Wells Coates", "9 July 1934", "Walter Gropius", "Agatha Christie"),
             "1379280", "between the wars"),
            ("2 Willow Road", "Q222881",
             "Ernő Goldfinger completed this terrace of three houses in Hampstead in 1939 and lived at number 2 "
             "until his death in 1987. The National Trust has run it since 1995.",
             "en:2 Willow Road", ("Goldfinger", "1939", "1987", "1995"),
             "1379196", "between the wars"),
            ("Royal Festival Hall", "Q647390",
             "Built for the Festival of Britain and opened on 3 May 1951. In 1981 it became the first post-war "
             "building to be listed Grade I.",
             "en:Royal Festival Hall", ("Festival of Britain", "3 May 1951", "first post-war building", "1981"),
             "1249756", "South Bank"),
            ("Commonwealth Institute", "Q42041837",
             "A 1960s landmark by Robert Matthew, Johnson-Marshall and Partners. After standing empty for over a "
             "decade it became the Design Museum in 2016.",
             "en:Design Museum", ("Commonwealth Institute", "Grade II* listed", "2016", "vacant for over a dec"),
             "1227441", "Brutalism"),
            ("BT Tower", "Q797085",
             "Built in 1964, it was London's tallest structure until 1980. Its existence was an official secret, "
             "and a judge in 1978 ordered it be called only \"Location 23\".",
             "en:BT Tower", ("1964", "until 1980", "official secret", "Location 23"),
             "1350342", "towers"),
            ("Centre Point", "Q2339039",
             "The 34-storey tower was built from 1963 to 1966 and stood empty until 1975. In 2015 it was "
             "converted to flats.",
             "en:Centre Point", ("34-storey", "1963 to 1966", "empty from the time of its completion until 1975", "2015"),
             "1113172", "towers"),
            ("National Theatre", "Q113531980",
             "Denys Lasdun and Peter Softley designed the building with three stages, which opened between 1976 "
             "and 1977. Until then the company played at the Old Vic.",
             "en:Royal National Theatre", ("Lasdun", "three stages", "between 1976 and 1977", "Old Vic"),
             "1272324", "South Bank"),
            ("Barbican Estate", "Q2319878",
             "Chamberlin, Powell and Bon built the estate of about 2,000 homes between 1965 and 1976 on a bombed "
             "site. The Metropolitan line was moved to make room for it.",
             "en:Barbican Estate", ("Chamberlin, Powell and Bon", "between 1965 and 1976", "Metropolitan line"),
             "1352667", "Brutalism"),
            ("Balfron Tower", "Q804926",
             "Ernő Goldfinger's 27-storey block in Poplar was built in 1965–67. Its lifts stop only on every "
             "third floor.",
             "en:Balfron Tower", ("27-storey", "Goldfinger", "1965–67", "every third floor"),
             "1334931", "Brutalism"),
            ("Trellick Tower", "Q1571416",
             "Goldfinger's tower in Kensal Town opened in 1972 as an improved version of Balfron Tower. It has "
             "been listed Grade II* since 1998.",
             "en:Trellick Tower", ("1972", "Balfron Tower", "1998"),
             "1246688", "Brutalism"),
            ("Lloyd's building", "Q1814818",
             "Richard Rogers's building puts its ducts and lifts on the outside. Completed in 1986, it was listed"
             " Grade I in 2011, the youngest building ever to receive that status.",
             "en:Lloyd's building", ("ducts and lifts", "1986", "2011", "youngest structure"),
             "1405493", "towers"),
            ("30 St Mary Axe", "Q191161",
             "Foster + Partners' tower opened in 2004 on the site of the Baltic Exchange, which an IRA bomb badly"
             " damaged in 1992.",
             "en:The Gherkin", ("Foster + Partners", "April 2004", "Baltic Exchange", "1992"),
             None, "towers"),
            ("20 Fenchurch Street", "Q212834",
             "The concave glass of the \"Walkie-Talkie\" focused sunlight onto the street while it was being built "
             "and melted parts of a parked car; the developers paid the owner £946.",
             "en:20 Fenchurch Street", ("Walkie-Talkie", "£946", "melted bodywork"),
             None, "towers"),
            ("The Shard", "Q18536",
             "Renzo Piano's 309.6-metre tower, inaugurated in July 2012, is the tallest building in the United "
             "Kingdom.",
             "en:The Shard", ("Renzo Piano", "309.6 metres", "5 July 2012", "tallest building in the United Kingdom"),
             None, "towers"),
        ]),
    dict(
        id="railways", section="The modern city", title="Railways and engineering", era="1825–1899",
        intro=("London's railway companies each built their own terminus at the edge of the old city, so the "
               "capital ended up with a ring of them. Beneath the streets and the river, engineers dug the first "
               "underwater tunnel and the first underground railway."),
        entries=[
            ("Brunel Engine House", "Q12053739",
             "Marc Brunel designed this engine house for the Thames Tunnel, the first tunnel built under a "
             "navigable river, which opened in 1843. His son Isambard became resident engineer in 1827, aged 20.",
             "en:Brunel Museum", ("Engine House", "1843", "January 1827", "age of 20"),
             None, "engineering"),
            ("London Bridge station", "Q801125",
             "Opened in 1836 by the London and Greenwich Railway, it is the oldest railway station in London fare"
             " zone 1 and one of the oldest in the world.",
             "en:London Bridge station", ("1836", "London and Greenwich Railway", "oldest railway station"),
             None, "termini"),
            ("Fenchurch Street station", "Q800753",
             "The City's small terminus opened in 1841 for the London and Blackwall Railway and was rebuilt in "
             "1854.",
             "en:Fenchurch Street railway station", ("1841", "London and Blackwall Railway", "1854"),
             None, "termini"),
            ("King's Cross station", "Q219867",
             "Lewis Cubitt designed the Great Northern Railway's terminus, opened in 1852. An extension built in "
             "1972 as a temporary structure hid its front for 40 years, until it was demolished in late 2012.",
             "en:London King's Cross railway station", ("1852", "Lewis Cubitt", "in 1972", "intended to be temporary", "late 2012"),
             "1078328", "termini"),
            ("Paddington station", "Q214788",
             "Isambard Kingdom Brunel designed the Great Western Railway's main station, which opened in 1854. "
             "His design is still recognisable after many rebuildings.",
             "en:London Paddington station", ("1854", "Isambard Kingdom Brunel", "Brunel's original design is still recognisable"),
             "1066881", "termini"),
            ("Baker Street station", "Q616218",
             "One of the original stations of the Metropolitan Railway, the world's first underground railway, "
             "which opened on 10 January 1863.",
             "en:Baker Street tube station", ("Metropolitan Railway", "world's first underground railway", "10 January 1863"),
             "1239815", "engineering"),
            ("Charing Cross station", "Q801128",
             "Opened by the South Eastern Railway in 1864. The Eleanor Cross in the forecourt is a Victorian "
             "replica by Edward Middleton Barry.",
             "en:Charing Cross railway station", ("1864", "Eleanor Cross", "Edward Middleton Barry"),
             None, "termini"),
            ("Cannon Street station", "Q800615",
             "Built on the site of the Steelyard, the trading base of the Hanseatic merchants, and opened in "
             "1866. Its two towers facing the Thames are 135 feet high.",
             "en:Cannon Street station", ("Steelyard", "Hanseatic", "1866", "135 ft"),
             None, "termini"),
            ("St Pancras station", "Q720102",
             "William Henry Barlow's single-span roof made the train shed the largest enclosed space in the "
             "world. The undercroft was laid out for storing beer, measured in beer barrels.",
             "en:St Pancras railway station", ("William Henry Barlow", "largest enclosed space in the world", "beer barrel"),
             None, "termini"),
            ("St Pancras hotel", "Q7590892",
             "George Gilbert Scott's Midland Grand Hotel opened in 1873 and closed in 1935. After decades as "
             "railway offices it reopened as a hotel in 2011.",
             "en:St Pancras London Hotel", ("Midland Grand Hotel", "George Gilbert Scott", "1873", "1935", "2011"),
             None, "termini"),
            ("Liverpool Street station", "Q801124",
             "The Great Eastern Railway's terminus opened in 1874. Before the Second World War thousands of child"
             " refugees of the Kindertransport arrived here.",
             "en:Liverpool Street station", ("1874", "Great Eastern Railway", "Kindertransport"),
             None, "termini"),
            ("Euston station", "Q800751",
             "London's first inter-city station opened in 1837. It was rebuilt in the 1960s, and the Euston Arch "
             "and Great Hall were demolished, a loss still argued over.",
             "en:Euston railway station", ("20 July 1837", "Euston Arch", "Great Hall were demolished"),
             None, "termini"),
            ("Tower Bridge", "Q83125",
             "Horace Jones and John Wolfe Barry's bridge was built in 1886–1894. Its central span is two bascules"
             " that lift to let ships into the Pool of London.",
             "en:Tower Bridge", ("Horace Jones", "John Wolfe Barry", "between 1886 and 1894", "bascules", "Pool of London"),
             "1357515", "engineering"),
            ("Marylebone station", "Q649419",
             "Opened on 15 March 1899, it was the last of London's main line termini to be built, for the last "
             "major railway to open in Britain for 100 years.",
             "en:Marylebone station", ("15 March 1899", "last of London's main line termini", "100 years"),
             "1267906", "termini"),
            ("Roundhouse", "Q1780197",
             "Built in 1846–1847 as an engine shed with a turntable, it served that purpose for only about a "
             "decade. It has been a performing arts venue since 1964.",
             "en:Roundhouse (venue)", ("1846–1847", "turntable", "about a decade", "1964"),
             "1258103", "engineering"),
        ]),
    dict(
        id="port", section="Trade and empire", title="The port and the markets", era="1802–1981",
        intro=("Until the 1960s the Pool of London and the docks downstream handled goods from all over the "
               "empire, stored in miles of warehouses. The London and St Katharine Docks had closed by 1969 and "
               "the rest followed; many of the warehouses and market halls survive with new uses."),
        entries=[
            ("West India Quay warehouses", "Q2904846",
             "Sugar warehouses built in 1802 on the north side of the West India Docks. Since 2003 they have "
             "housed a museum of the port and its links to the Atlantic slave trade.",
             "en:London Museum Docklands", ("1802", "West India Docks", "2003", "Atlantic slave trade"),
             None, "docks"),
            ("Tobacco Dock", "Q1671266",
             "John Rennie's warehouse in Wapping was completed in 1812 to store imported tobacco. It reopened as "
             "a shopping centre in 1989 and closed two years later.",
             "en:Tobacco Dock", ("John Rennie", "1812", "tobacco", "1989"),
             "1065827", "docks"),
            ("Custom House", "Q1146205",
             "Customs duties were collected on this stretch of the Thames from the Middle Ages. The building of "
             "1814 partly collapsed in 1825 when its timber piles gave way.",
             "en:Custom House, City of London", ("1814", "In 1825", "timber pilings"),
             "1359193", "trade"),
            ("Borough Market", "Q894072",
             "A market has stood at the southern end of London Bridge since at least the 12th century. The "
             "present buildings date from the 1850s.",
             "en:Borough Market", ("12th century", "1850s"),
             None, "markets"),
            ("Hop Exchange", "Q5898926",
             "Opened in 1867 as the single trading floor for hops from Kent, which arrived at London Bridge by "
             "rail or up the Thames by boat.",
             "en:Hop Exchange", ("1867", "Kent", "London Bridge Station"),
             "1385923", "markets"),
            ("Butler's Wharf", "Q5002549",
             "A warehouse complex completed in 1873 for goods unloaded at the port. The main building was "
             "converted to flats to a design by Conran Roche in 1989.",
             "en:Butler's Wharf", ("1873", "Conran Roche", "1989"),
             "1385896", "docks"),
            ("Old Billingsgate Market", "Q15263739",
             "Horace Jones's arcaded fish market of 1875 on Lower Thames Street, when Billingsgate was the "
             "world's largest fish market. It is now an events venue.",
             "en:Old Billingsgate", ("Horace Jones", "1875", "world's largest fish market"),
             "1358911", "markets"),
            ("Hay's Galleria", "Q5685733",
             "William Cubitt turned an old brewhouse into an enclosed dock, Hay's Wharf, in 1856. It was "
             "redeveloped in the 1980s as shops, offices and flats.",
             "en:Hay's Galleria", ("William Cubitt", "1856", "Hay's Wharf", "1980s"),
             "1385450", "docks"),
            ("Leadenhall Market", "Q961148",
             "A market has stood here since the 14th century. The present roof and cobbled halls were designed by"
             " Horace Jones in 1881.",
             "en:Leadenhall Market", ("14th century", "1881", "Horace Jones"),
             "1286182", "markets"),
            ("Wapping Hydraulic Power Station", "Q7968287",
             "Built in 1890, it pumped water under pressure through pipes to work lifts and machinery across "
             "London. It closed on 30 June 1977.",
             "en:Wapping Hydraulic Power Station", ("1890", "lifts", "30 June 1977"),
             "1242419", "docks"),
            ("Bankside Power Station", "Q806832",
             "Electricity was generated at Bankside from 1891 to 1981. Giles Gilbert Scott designed the present "
             "building, which has housed Tate Modern since 2000.",
             "en:Bankside Power Station", ("from 1891 to 1981", "Giles Gilbert Scott", "Since 2000", "Tate Modern"),
             None, "trade"),
            ("Oxo Tower", "Q2911715",
             "When the makers of Oxo were refused permission for illuminated advertising on their tower, they "
             "built windows that happened to spell the brand's name.",
             "en:Oxo Tower", ("Lemco", "permission for the advertisements was refused", "coincidentally"),
             None, "trade"),
        ]),
    dict(
        id="city", section="Trade and empire", title="Livery halls and the City", era="1339–1844",
        intro=("The City of London has governed itself since the Middle Ages, through its Lord Mayor and the "
               "livery companies that grew out of the medieval trade guilds. About forty companies still have "
               "their own halls, most of them rebuilt after the Great Fire, close to the Bank and the Royal "
               "Exchange."),
        entries=[
            ("Royal Exchange", "Q1241240",
             "Thomas Gresham founded the exchange in the 16th century and Elizabeth I gave it the title \"Royal\". "
             "The present building, the third, was opened by Queen Victoria on 28 October 1844.",
             "en:Royal Exchange, London", ("Thomas Gresham", "Elizabeth I", "28 October 1844", "fire of 1838"),
             "1064713", "institutions"),
            ("Bank of England", "Q63637740",
             "The bank has been on Threadneedle Street since 1734. Its nickname, the Old Lady of Threadneedle "
             "Street, comes from a cartoon by James Gillray of 1797.",
             "en:Bank of England", ("Threadneedle Street since 1734", "Old Lady of Threadneedle Street", "James Gillray", "1797"),
             "1079134", "institutions"),
            ("College of Arms", "Q1109101",
             "The heralds have been on this site since 1555, when Mary I granted them Derby Place. The house "
             "burned in the Great Fire, but the library was saved.",
             "en:College of Arms", ("1555", "Derby Place", "library was, however, saved"),
             "1079147", "institutions"),
            ("Trinity House", "Q90804634",
             "Trinity House, founded by royal charter in 1514, runs the lighthouses of England and Wales. A small"
             " headquarters staff still works at Tower Hill.",
             "en:Trinity House", ("1514", "lighthouse authority", "Tower Hill"),
             "1079137", "institutions"),
            ("Goldsmiths' Hall", "Q16707732",
             "The goldsmiths have been on this site since 1339, and the hall still houses an assay office. The "
             "present building, their third, was designed by Philip Hardwick and opened in 1835.",
             "en:Goldsmiths' Hall", ("1339", "assay office", "Philip Hardwick", "1835"),
             "1286469", "halls"),
            ("Merchant Taylors' Hall", "Q6818403",
             "The company has occupied this site between Threadneedle Street and Cornhill since 1347. In 1607 it "
             "gave a banquet here for James I.",
             "en:Merchant Taylors' Hall, London", ("since 1347", "1607", "King James I"),
             "1358898", "halls"),
            ("Skinners' Hall", "Q17526851",
             "Since a ruling of 1484 the Skinners and the Merchant Taylors swap sixth and seventh place among the"
             " livery companies every year. The two companies borrowed Chaucer's phrase \"at sixes and sevens\" for"
             " their rivalry.",
             "en:Worshipful Company of Skinners", ("1484", "sixes and sevens", "Merchant Taylors", "alternating annually"),
             "1064686", "halls"),
            ("Drapers' Hall", "Q25818870",
             "The Drapers bought this site from Henry VIII in 1543. It had been the London house of Thomas "
             "Cromwell, who had been attainted and executed.",
             "en:Worshipful Company of Drapers", ("1543", "Thomas Cromwell", "Henry VIII", "attainted"),
             "1358902", "halls"),
            ("Apothecaries' Hall", "Q16707714",
             "Rebuilt in 1672 after the Great Fire, the hall had an \"Elaboratory\" for the first large-scale "
             "manufacture of drugs. The society made medicines here until 1922.",
             "en:Apothecaries' Hall, London", ("1672", "Elaboratory", "first-ever large-scale manufacture of drugs", "1922"),
             "1359133", "halls"),
            ("Vintners' Hall", "Q17526875",
             "The hall on Upper Thames Street dates from 1671. The wine merchants' company received its rights to"
             " keep swans on the Thames from Edward IV.",
             "en:Worshipful Company of Vintners", ("1671", "swan rights", "Edward IV"),
             "1180690", "halls"),
            ("Fishmongers' Hall", "Q17645554",
             "The company's fourth hall beside London Bridge opened in 1834; the young George Gilbert Scott made "
             "its drawings. Bombed in the Blitz, it reopened in 1951.",
             "en:Fishmongers' Hall", ("1834", "Gilbert Scott", "1951"),
             "1002058", "halls"),
            ("Stationers' Hall", "Q17526857",
             "The Stationers' Company, chartered in 1557, controlled printing and publishing until the Copyright "
             "Act of 1710.",
             "en:Worshipful Company of Stationers and Newspaper Makers", ("1557", "Statute of Anne", "Copyright Act 1710"),
             "1064742", "halls"),
            ("Watermen's Hall", "Q17645392",
             "The meeting rooms of the Company of Watermen and Lightermen, who ferried passengers and goods on "
             "the Thames. Winners of Doggett's Coat and Badge, the old rowing race, receive their badges here.",
             "en:Company of Watermen and Lightermen", ("St Mary at Hill", "lightermen", "Doggett's Badge"),
             "1002034", "halls"),
        ]),
    dict(
        id="eastend", section="Faith and community", title="Huguenots, Jews and Bangladeshis", era="1701–1985",
        intro=("Just outside the City walls, Spitalfields and Whitechapel took in one wave of newcomers after "
               "another: French Protestant silk weavers after 1685, Jews from Eastern Europe in the 1880s, "
               "Bangladeshis from Sylhet in the 1970s. Several buildings have served each group in turn."),
        entries=[
            ("Bevis Marks Synagogue", "Q851924",
             "Built in 1701 by London's Spanish and Portuguese Jews, it is the oldest synagogue in the United "
             "Kingdom in continuous use.",
             "en:Bevis Marks Synagogue", ("1701", "Spanish and Portuguese", "oldest synagogue in the United Kingdom in continuous use"),
             "1064745", "Jewish"),
            ("Christ Church Spitalfields", "Q5108714",
             "Nicholas Hawksmoor's church was built between 1714 and 1729 in a parish then dominated by "
             "Huguenots, as a show of Anglican authority.",
             "en:Christ Church, Spitalfields", ("1714 and 1729", "Nicholas Hawksmoor", "Huguenots", "Anglican authority"),
             "1357795", "Huguenot"),
            ("19 Princelet Street", "Q6940881",
             "Built in 1719 for the Huguenot silk merchant Peter Abraham Ogier, the house became a synagogue in "
             "1869. It is now a museum of immigration.",
             "en:Museum of Immigration and Diversity", ("1719", "Peter Abraham Ogier", "synagogue in 1869"),
             "1260421", "Huguenot"),
            ("Dennis Severs' House", "Q3313296",
             "From 1979 to 1999 Dennis Severs lived at 18 Folgate Street and turned its rooms into an imagined "
             "home of a family of Huguenot silk weavers.",
             "en:Dennis Severs' House", ("18 Folgate Street", "1979 to 1999", "Huguenot silk weavers"),
             "1357829", "Huguenot"),
            ("Brick Lane Mosque", "Q4965928",
             "Built in 1743 as a Huguenot chapel, it became a Methodist chapel in 1819, the Spitalfields Great "
             "Synagogue in 1891 and a mosque in 1976.",
             "en:Brick Lane Mosque", ("1743", "1819", "Methodist chapel", "In 1891", "Spitalfields Great Synagogue", "In 1976"),
             "1240697", "Bangladeshi"),
            ("Sandys Row Synagogue", "Q7417544",
             "Huguenot refugees built it as a church in 1766; a Jewish congregation bought it in 1867. It is the "
             "oldest surviving Ashkenazi synagogue in London.",
             "en:Sandys Row Synagogue", ("1766", "1867", "oldest surviving Ashkenazi synagogue in London"),
             "1260323", "Jewish"),
            ("St George in the East", "Q7593238",
             "One of Hawksmoor's six London churches, built from 1714 to 1729. A bomb in May 1941 burned out the "
             "interior, but the walls and pepper-pot towers stayed up.",
             "en:St George in the East", ("six Hawksmoor churches", "1714 to 1729", "May 1941", "pepper-pot"),
             "1357779", "Huguenot"),
            ("Old Spitalfields Market", "Q43470",
             "Charles I licensed a market here in 1638. In 1991 the wholesale fruit and vegetable trade moved to "
             "Leyton.",
             "en:Old Spitalfields Market", ("1638", "Charles I", "1991", "Leyton"),
             "1065750", "trades"),
            ("Black Eagle Brewery", "Q4920712",
             "Truman's brewery off Brick Lane was the largest in the world by 1853, making 400,000 barrels a "
             "year. It is now the Old Truman Brewery, home to some 250 businesses.",
             "en:Black Eagle Brewery", ("1853", "400,000 barrels", "Old Truman Brewery", "250 businesses"),
             "1252365", "trades"),
            ("Whitechapel Bell Foundry", "Q174855",
             "The foundry cast the Liberty Bell and recast Big Ben. It closed on 12 June 2017, after about 250 "
             "years on this site.",
             "en:Whitechapel Bell Foundry", ("Liberty Bell", "Big Ben", "12 June 2017", "250 years"),
             "1357529", "trades"),
            ("Toynbee Hall", "Q1164207",
             "Henrietta and Samuel Barnett founded it in 1884 to bring rich and poor to live side by side. It was"
             " the first university-linked house of the worldwide settlement movement.",
             "en:Toynbee Hall", ("1884", "Henrietta and Samuel Barnett", "first university-affiliated institution"),
             "1065201", "community"),
            ("Whitechapel Gallery", "Q1814654",
             "Charles Harrison Townsend's gallery opened in 1901. In 1938 it showed Picasso's Guernica in protest"
             " against the Spanish Civil War.",
             "en:Whitechapel Gallery", ("Charles Harrison Townsend", "1901", "Guernica in 1938"),
             "1065820", "community"),
            ("East London Mosque", "Q3352688",
             "Built in 1982–1985 on land left empty by wartime bombing, it was one of the first mosques in "
             "Britain allowed to broadcast the call to prayer by loudspeaker.",
             "en:East London Mosque", ("1982", "1985", "loudspeakers"),
             None, "Bangladeshi"),
        ]),
    dict(
        id="exiles", section="Discover", title="Exiles and radicals", era="1757–1945",
        intro=("London gave refuge to revolutionaries and outcasts from across Europe and the empire, and bred "
               "its own campaigners. Many of the rooms where they read, met and organised are still standing."),
        entries=[
            ("Benjamin Franklin House", "Q4888645",
             "Benjamin Franklin lived and worked at 36 Craven Street from 1757 to 1774. It is the last of his "
             "homes still standing.",
             "en:Benjamin Franklin House", ("36 Craven Street", "1757 to 1774", "last-standing former residence"),
             "1066930", "visitors"),
            ("British Museum Reading Room", "Q2152532",
             "Sydney Smirke's domed reading room opened in 1857. Karl Marx, Sun Yat-sen, Gandhi and Lenin, under "
             "the name Jacob Richter, all read here.",
             "en:British Museum Reading Room", ("Sydney Smirke", "1857", "Karl Marx", "Sun Yat-sen", "Jacob Richter"),
             None, "exiles"),
            ("St Peter's Italian Church", "Q16900510",
             "Built for London's Italian immigrants with help from the exiled nationalist Giuseppe Mazzini, it "
             "was consecrated in 1863 as the only basilica-style church in Britain.",
             "en:St Peter's Italian Church", ("Giuseppe Mazzini", "16 April 1863", "only basilica-style church"),
             "1356763", "exiles"),
            ("Caxton Hall", "Q5055269",
             "Opened as Westminster Town Hall in 1883, it hosted political meetings of every kind. In 1940 Udham "
             "Singh, a survivor of the Jallianwala Bagh massacre, shot Michael O'Dwyer here.",
             "en:Caxton Hall", ("1883", "Udham Singh", "Michael O'Dwyer", "In 1940", "Jallianwala Bagh massacre"),
             "1357266", "radicals"),
            ("Bow Quarter", "Q4950648",
             "The matchgirls' strike of 1888 began in this Bryant and May factory, over fourteen-hour days, fines"
             " and poisoning by white phosphorus. It led to the first British trade union for women.",
             "en:Bow Quarter", ("1888", "Bryant and May", "white phosphorus", "first British trade union for women"),
             "1065761", "radicals"),
            ("Marx Memorial Library", "Q93844",
             "Built in 1738 as the Welsh Charity School. In 1902–1903 Lenin worked here, publishing seventeen "
             "issues of Iskra; the library opened in 1933.",
             "en:Marx Memorial Library", ("1738", "Welsh Charity School", "1902–1903", "seventeen issues", "Iskra", "1933"),
             "1279541", "exiles"),
            ("Kingsley Hall", "Q6413308",
             "Doris and Muriel Lester's community centre in Bow sheltered and fed workers during the General "
             "Strike of 1926. Gandhi stayed here in 1931.",
             "en:Kingsley Hall", ("Doris and Muriel Lester", "General Strike of 1926", "Gandhi stayed in Kingsley Hall in 1931"),
             "1357884", "radicals"),
            ("Conway Hall", "Q26267067",
             "The South Place Ethical Society opened its Art Deco hall in Red Lion Square in 1929. George Orwell "
             "spoke here for freedom of the press in 1945.",
             "en:Conway Hall", ("23 September 1929", "Art Deco", "George Orwell", "November 1945"),
             "1392343", "radicals"),
            ("St George's Town Hall", "Q27081829",
             "A mural painted on its side in the early 1980s shows October 1936, when anti-fascists clashed with "
             "the police sent to protect a march by Oswald Mosley's British Union of Fascists.",
             "en:St George's Town Hall", ("1936", "Oswald Mosley", "British Union of Fascists", "mural", "early 1980s"),
             "1242346", "radicals"),
            ("Freud Museum", "Q1455777",
             "Sigmund Freud escaped the Nazi annexation of Austria in 1938 and spent the last year of his life at"
             " 20 Maresfield Gardens. His analyst's couch came with him from Vienna.",
             "en:Freud Museum", ("1938", "20 Maresfield Gardens", "couch", "Berggasse 19"),
             "1113113", "exiles"),
        ]),
    dict(
        id="writers", section="Art and letters", title="Writers' London", era="1599–1949",
        intro=("London has been home to its writers for four hundred years, and a handful of their houses, "
               "taverns and haunts survive. Some are kept as museums, with the rooms where the books were "
               "written."),
        entries=[
            ("Shakespeare's Globe", "Q7725501",
             "A reconstruction of the playhouse of 1599 for which Shakespeare wrote his plays, completed in 1997 "
             "about 230 metres from the original site.",
             "en:Shakespeare's Globe", ("1599", "completed in 1997", "about 230 metres", "original site"),
             None, "places"),
            ("Ye Olde Cheshire Cheese", "Q1771680",
             "Rebuilt shortly after the Great Fire, the Fleet Street pub counted Dickens, Chesterton and Mark "
             "Twain among its regulars. For about 40 years a swearing grey parrot called Polly lived in the bar.",
             "en:Ye Olde Cheshire Cheese", ("Great Fire of 1666", "G. K. Chesterton", "Mark Twain", "Polly", "40 years"),
             "1064662", "places"),
            ("Dr Johnson's House", "Q5304210",
             "Samuel Johnson lived at 17 Gough Square from 1748 to 1759 and compiled his Dictionary of the "
             "English Language here. It is the only one of his 18 City homes to survive.",
             "en:Dr Johnson's House", ("1748 to 1759", "A Dictionary of the English Language", "18 residences"),
             "1192738", "houses"),
            ("Keats House", "Q6382345",
             "John Keats lodged here from December 1818 to May 1820 and, by his friend's account, wrote \"Ode to a"
             " Nightingale\" under a plum tree in the garden. He fell in love with Fanny Brawne next door.",
             "en:Keats House", ("December 1818 to May 1820", "Ode to a Nightingale", "plum tree", "Fanny Brawne"),
             "1379221", "houses"),
            ("Carlyle's House", "Q5043126",
             "Thomas and Jane Carlyle lived in this house of 1708 in Cheyne Row from 1834 until his death in "
             "1881. He wrote most of his work here, from The French Revolution onward.",
             "en:The Carlyles' House", ("1708", "Cheyne Row", "from 1834 until his death in 1881", "The French Revolution"),
             "1358142", "houses"),
            ("Charles Dickens Museum", "Q2723633",
             "Dickens lived at 48 Doughty Street from 1837 to 1839, his only London house still standing. Here he"
             " wrote all of Oliver Twist and Nicholas Nickleby.",
             "en:Charles Dickens Museum", ("48 Doughty Street", "1837", "only surviving London house", "Oliver Twist", "Nicholas Nickleby"),
             "1356735", "houses"),
            ("Hatchards", "Q5681055",
             "John Hatchard opened his bookshop on Piccadilly in 1797; it has traded from its present address "
             "since 1801. It claims to be the oldest bookshop in the United Kingdom.",
             "en:Hatchards", ("1797", "since 1801", "oldest bookshop"),
             None, "places"),
            ("The Langham", "Q768935",
             "When it opened in 1865 it was the largest hotel in London, with the first hydraulic lifts in "
             "England. Arthur Conan Doyle set parts of two Sherlock Holmes stories here.",
             "en:Langham Hotel, London", ("1865", "first hydraulic lifts in England", "A Scandal in Bohemia", "The Sign of Four"),
             "1227056", "places"),
            ("Sherlock Holmes Museum", "Q1990172",
             "The house of 1815 bears the number 221B by permission of Westminster council, although it stands "
             "between 237 and 241 Baker Street.",
             "en:Sherlock Holmes Museum", ("1815", "221B", "between numbers 237 and 241"),
             None, "places"),
            ("Leighton House", "Q6519762",
             "The painter Frederic Leighton, President of the Royal Academy, had George Aitchison build this "
             "house and studio between 1866 and 1895, with an Arab Hall lined with tiles from the Near East.",
             "en:Leighton House", ("Frederic Leighton", "George Aitchison", "1866 and 1895", "Arab Hall"),
             "1191541", "houses"),
            ("Senate House", "Q3478501",
             "Charles Holden's tower was built in 1932–1937. In the war it housed the Ministry of Information, "
             "where Orwell's wife Eileen worked; his description of the Ministry of Truth in Nineteen Eighty-Four"
             " evokes the building.",
             "en:Senate House, London", ("Charles Holden", "1932 and 1937", "Ministry of Information", "Ministry of Truth", "Eileen"),
             "1113107", "places"),
        ]),
    dict(
        id="music", section="Art and letters", title="Music London", era="1723–1983",
        intro=("Handel and Mozart wrote music in Mayfair and Belgravia, the Victorians built concert halls and "
               "music halls, and in the 1960s and 1970s the city's studios and clubs launched the Beatles and "
               "punk."),
        entries=[
            ("Handel Hendrix House", "Q2920095",
             "Handel lived at 25 Brook Street from 1723 until his death in 1759 and composed most of his later "
             "works here. Jimi Hendrix lived next door at number 23 in 1968–1969.",
             "en:Handel Hendrix House", ("25 Brook Street", "from 1723 until his death there in 1759", "23 Brook Street", "1968–1969"),
             "1066382", "classical"),
            ("180 Ebury Street", "Q17527066",
             "The young Mozart and his family lived here from 5 August to 24 September 1764, and he composed his "
             "first symphony in the house.",
             "en:180 Ebury Street", ("5 August 1764", "24 September 1764", "first symphony"),
             "1211215", "classical"),
            ("Wilton's Music Hall", "Q8023341",
             "John Wilton replaced a concert room behind his pub with his \"Magnificent New Music Hall\" in 1859. "
             "It is one of the very few music halls of the East End to survive.",
             "en:Wilton's Music Hall", ("John Wilton", "Magnificent New Music Hall", "1859", "very few surviving music halls"),
             "1065173", "music hall"),
            ("Hoxton Hall", "Q15226190",
             "Built in 1863 as MacDonald's Music Hall, it lost its licence in 1871 after police complaints. Long "
             "use as a Quaker meeting house kept the galleried auditorium largely unaltered.",
             "en:Hoxton Hall", ("1863", "MacDonald's Music Hall", "1871", "Quaker meeting house"),
             "1226830", "music hall"),
            ("Royal Albert Hall", "Q193639",
             "Queen Victoria opened the hall in 1871. The BBC Proms have been held here every summer since 1941.",
             "en:Royal Albert Hall", ("Queen Victoria in 1871", "every summer since 1941"),
             "1217742", "classical"),
            ("Union Chapel", "Q7885481",
             "James Cubitt's Gothic church was built in 1874–1877 and is still a working Congregational chapel. "
             "Its acoustics have made it a favourite music venue; Time Out readers have voted it London's best.",
             "en:Union Chapel, Islington", ("James Cubitt", "between 1874 and 1877", "Congregational", "excellent acoustics", "Best Live Music Venue"),
             "1208365", "venues"),
            ("Wigmore Hall", "Q781834",
             "The German piano maker Bechstein built it next to its showroom; it opened in 1901 as the Bechstein "
             "Hall. It is known for its acoustics and its chamber music.",
             "en:Wigmore Hall", ("Bechstein Hall", "1901", "chamber music"),
             "1357377", "classical"),
            ("Hackney Empire", "Q5637363",
             "Frank Matcham built it in 1901 as a music hall. Pevsner called it among the best-surviving "
             "Edwardian suburban variety theatres.",
             "en:Hackney Empire", ("Frank Matcham", "1901", "best-surviving Edwardian suburban variety theatres"),
             "1226960", "music hall"),
            ("Koko", "Q1028419",
             "Opened in 1900 as the Camden Theatre, it later became a cinema and after the war was taken over by "
             "the BBC. It reopened in 1977 as the Music Machine and was the Camden Palace from 1982.",
             "en:Koko (music venue)", ("1900", "Camden Theatre", "BBC", "1977", "Music Machine", "Camden Palace in 1982"),
             "1272425", "venues"),
            ("Abbey Road Studios", "Q209651",
             "The Gramophone Company opened the studios in November 1931. The Beatles named their 1969 album "
             "after the road, and fans still come to the zebra crossing outside.",
             "en:Abbey Road Studios", ("November 1931", "1969 album Abbey Road", "zebra crossing"),
             "1393688", "pop"),
            ("100 Club", "Q8535",
             "Live music has played at 100 Oxford Street since 24 October 1942, first as a jazz club. In "
             "September 1976 it held the first international punk festival.",
             "en:100 Club", ("100 Oxford Street", "24 October 1942", "September 1976", "first international punk festival"),
             None, "pop"),
            ("3 Savile Row", "Q17550035",
             "A townhouse of about 1733 that became the headquarters of the Beatles' company Apple. The band "
             "played their last live performance on its roof on 30 January 1969.",
             "en:3 Savile Row", ("1733", "Apple Corps", "rooftop concert", "30 January 1969"),
             "1236103", "pop"),
            ("Electric Ballroom", "Q5357303",
             "The hall on Camden High Street began as an Irish ballroom in the 1930s and took the name Electric "
             "Ballroom in 1978.",
             "en:Electric Ballroom", ("184 Camden High Street", "Irish ballroom in the 1930s", "1978"),
             None, "pop"),
            ("Brixton Academy", "Q2239788",
             "Opened in 1929 as the Astoria cinema and a concert hall since 1983. The Smiths played their last "
             "gig here in December 1986.",
             "en:Brixton Academy", ("1929", "1983", "The Smiths' last gig (December 1986)"),
             "1064934", "pop"),
        ]),
    dict(
        id="science", section="Science and learning", title="Science and medicine", era="1123–1938",
        intro=("London's hospitals are among the oldest in Europe, and its learned societies and museums brought "
               "the new sciences to a wide public. Some of the great discoveries were made in rooms that can "
               "still be visited."),
        entries=[
            ("St Bartholomew's Hospital", "Q164946",
             "Founded in 1123 by Rahere, a courtier of Henry I, Barts is the oldest hospital in Britain still on "
             "its original site. Henry VIII refounded it in December 1546.",
             "en:St Bartholomew's Hospital", ("1123", "Rahere", "Henry I", "December 1546", "oldest hospital in Britain"),
             "1079116", "hospitals"),
            ("Royal Hospital Chelsea", "Q1628509",
             "Charles II founded the home for army veterans in 1682, and Christopher Wren designed it. The first "
             "Chelsea Pensioners moved in in 1692.",
             "en:Royal Hospital Chelsea", ("Charles II", "1682", "Christopher Wren", "1692", "Chelsea Pensioners"),
             "1000353", "hospitals"),
            ("Foundling Museum", "Q5474645",
             "Thomas Coram set up the Foundling Hospital for abandoned children in 1739 after 17 years of "
             "campaigning. Hogarth and Handel supported it, and its story is told here.",
             "en:Foundling Museum", ("Thomas Coram", "1739", "17 years", "Hogarth", "Handel"),
             "1272392", "hospitals"),
            ("Old Operating Theatre", "Q7084660",
             "In 1822 part of the herb garret of St Thomas's Church was turned into an operating theatre. It is "
             "the oldest surviving one in Britain, from the days before anaesthetics.",
             "en:Old Operating Theatre Museum and Herb Garret", ("In 1822", "oldest surviving operating theatre in the UK", "before anaesthetics"),
             None, "hospitals"),
            ("UCL Main Building", "Q7864083",
             "Construction began in 1827, a year after the university was founded. William Wilkins, architect of "
             "the National Gallery, designed the Octagon and its dome.",
             "en:UCL Main Building", ("In 1827", "William Wilkins", "National Gallery", "Octagon"),
             "1113056", "learning"),
            ("Great Ormond Street Hospital", "Q1349705",
             "The Hospital for Sick Children opened on 14 February 1852. In 1929 J. M. Barrie gave it the "
             "copyright of Peter Pan.",
             "en:Great Ormond Street Hospital", ("14 February 1852", "1929", "J. M. Barrie", "Peter Pan"),
             None, "hospitals"),
            ("John Snow pub", "Q123244004",
             "The pub is named after the physician John Snow, who traced the cholera outbreak of 1854 to a nearby"
             " water pump. The John Snow Society meets here.",
             "en:John Snow (public house)", ("John Snow", "cholera outbreak in 1854", "water pump", "John Snow Society"),
             None, "discoveries"),
            ("Burlington House", "Q225471",
             "The Linnean Society moved here in 1857. At its meeting on 1 July 1858 papers by Charles Darwin and "
             "Alfred Russel Wallace first presented the theory of evolution by natural selection.",
             "en:Linnean Society of London", ("Since 1857", "Burlington House", "1 July 1858", "Charles Darwin and Alfred Russel Wallace"),
             None, "discoveries"),
            ("Natural History Museum", "Q309388",
             "Alfred Waterhouse's building opened in 1881 to house natural history collections from the British "
             "Museum. The museum holds some 80 million specimens.",
             "en:Natural History Museum, London", ("Alfred Waterhouse", "1881", "80 million"),
             "1080675", "learning"),
            ("Science Museum", "Q674773",
             "Founded in 1857, the Science Museum became an independent institution on 26 June 1909.",
             "en:Science Museum, London", ("1857", "26 June 1909"),
             None, "learning"),
            ("St Mary's Hospital", "Q3495342",
             "Alexander Fleming discovered penicillin here in 1928. His laboratory has been restored as a museum.",
             "en:St Mary's Hospital, London", ("Alexander Fleming", "penicillin in 1928", "Fleming's laboratory has been restored"),
             None, "discoveries"),
            ("Finsbury Health Centre", "Q5450923",
             "Berthold Lubetkin and Tecton designed this health centre for the borough of Finsbury; it was built "
             "in 1935–38. Today it houses a general practice and a centre for stammering.",
             "en:Finsbury Health Centre", ("1935–38", "Lubetkin", "Tecton", "Stammering"),
             "1297993", "hospitals"),
            ("Florence Nightingale Museum", "Q5460739",
             "The museum at St Thomas' Hospital, opposite Parliament, tells the life of Florence Nightingale, "
             "regarded as the founder of modern nursing in Britain.",
             "en:Florence Nightingale Museum", ("St Thomas' Hospital", "Palace of Westminster", "founder of modern nursing"),
             None, "hospitals"),
            ("Wellcome Collection", "Q7981191",
             "A museum and library at 183 Euston Road, opened in 2007 to show the collection of Henry Wellcome on"
             " medicine, life and art.",
             "en:Wellcome Collection", ("183 Euston Road", "2007", "Henry Solomon Wellcome"),
             None, "learning"),
        ]),
    dict(
        id="pubs", section="Discover", title="Taverns, coffee and old shops", era="1652–1905",
        intro=("Old London did its business and its drinking in taverns, coffee houses and small specialist "
               "shops. A few have traded in the same buildings for centuries; others are Victorian gin palaces "
               "with their glass and woodwork intact."),
        entries=[
            ("Jamaica Wine House", "Q6127350",
             "A plaque marks the site of London's first coffee house, opened in 1652 by Pasqua Rosée. Samuel "
             "Pepys visited in 1660; the present pub stands in the alleys off Cornhill.",
             "en:Jamaica Wine House", ("first London Coffee house", "1652", "Pasqua Rosée", "1660"),
             "1079156", "coffee and tea"),
            ("The George Inn", "Q12058464",
             "The only galleried coaching inn left in London, rebuilt in 1677 after a fire destroyed most of "
             "Southwark. Dickens mentioned it in Little Dorrit.",
             "en:The George Inn, Southwark", ("only surviving galleried London coaching inn", "1677", "Little Dorrit"),
             "1378357", "pubs"),
            ("Lamb and Flag", "Q18353351",
             "A pub since 1772, it hosted bare-knuckle fights upstairs and was nicknamed \"The Bucket of Blood\". A"
             " plaque recalls the attack on John Dryden in a nearby alley in 1679.",
             "en:Lamb and Flag, Covent Garden", ("1772", "Bucket of Blood", "John Dryden", "1679"),
             "1265122", "pubs"),
            ("Twinings", "Q7858373",
             "Thomas Twining opened Britain's first known tea room at 216 Strand in 1706, and the firm has traded"
             " from the same premises ever since. Its logo of 1787 is the oldest in continuous use.",
             "en:Twinings", ("No. 216 Strand", "1706", "1787", "oldest in continuous use"),
             "1236754", "coffee and tea"),
            ("Fortnum & Mason", "Q498563",
             "William Fortnum and Hugh Mason founded the grocery at 181 Piccadilly in 1707. It is known for its "
             "food hampers.",
             "en:Fortnum & Mason", ("181 Piccadilly", "1707", "William Fortnum and Hugh Mason", "hampers"),
             None, "shops"),
            ("Town of Ramsgate", "Q16707776",
             "A watermen's tavern in Wapping by Wapping Old Stairs. The present building dates from 1758.",
             "en:Town of Ramsgate", ("waterman's tavern", "1758", "Wapping Old Stairs"),
             "1065804", "pubs"),
            ("Prospect of Whitby", "Q3924088",
             "The pub claims the site of the oldest riverside tavern, from about 1520, once known as the Devil's "
             "Tavern. Sir Hugh Willoughby sailed from here in 1553 to look for the Northeast Passage.",
             "en:Prospect of Whitby", ("1520", "Devil’s Tavern", "Hugh Willoughby", "1553"),
             "1357505", "pubs"),
            ("The Grapes", "Q15059596",
             "The present building dates from the 1720s, on the site of a pub of 1583. Dickens, who knew "
             "Limehouse well, put it barely disguised into the opening of Our Mutual Friend.",
             "en:The Grapes, Limehouse", ("1720s", "1583", "Our Mutual Friend"),
             "1260573", "pubs"),
            ("Lock & Co. Hatters", "Q6138148",
             "Founded in 1676, the hatter has been at 6 St James's Street since 1765, which makes it the oldest "
             "hat shop in the world.",
             "en:James Lock & Co.", ("1676", "6 St James's Street", "since 1765", "world's oldest hat shop"),
             "1264869", "shops"),
            ("Rules", "Q7379013",
             "Thomas Rule opened it as an oyster bar on Maiden Lane in 1798. It calls itself London's oldest "
             "restaurant.",
             "en:Rules (restaurant)", ("1798", "Thomas Rule", "oyster bar", "London's oldest restaurant"),
             "1238981", "shops"),
            ("Princess Louise", "Q7244677",
             "Built in 1872, the Holborn pub keeps its Victorian interior of 1891, with booths around an island "
             "bar. Even the marble urinals are mentioned in its listing.",
             "en:Princess Louise, Holborn", ("1872", "1891", "island bar", "marble urinals"),
             "1378884", "pubs"),
            ("The Salisbury", "Q15991477",
             "Built in about 1899, it keeps a late Victorian interior of etched glass and carved wood. The \"SS\" "
             "in the glass stands for its first name, the Salisbury Stores.",
             "en:The Salisbury, Covent Garden", ("1899", "etched and polished glass", "Salisbury Stores"),
             "1236050", "pubs"),
            ("The Black Friar", "Q15979550",
             "Built in about 1875 on the site of a Dominican friary and remodelled around 1905 by Herbert Fuller-"
             "Clark. John Betjeman led the campaign that saved it from demolition in the 1960s.",
             "en:The Black Friar, Blackfriars", ("1875", "Dominican friary", "Herbert Fuller-Clark", "John Betjeman"),
             "1285723", "pubs"),
        ]),
    dict(
        id="secrets", section="Discover", title="Hidden London", era="1136–1997",
        intro=("Small surprises in well-known buildings: a police station inside a triumphal arch, a spies' "
               "letterbox at a church door, flamingos on a department store roof and a nose on Admiralty Arch."),
        entries=[
            ("Winchester Palace", "Q203035",
             "Only part of the great hall and its rose window remain of the London house of the Bishops of "
             "Winchester, built in about 1136 on what is now Clink Street.",
             "en:Winchester Palace", ("Bishops of Winchester", "Clink Street", "rose window", "about 1136"),
             "1378484", "survivals"),
            ("St Etheldreda's Church", "Q4505176",
             "Built around the 1280s as the chapel of the London residence of the Bishops of Ely. The Catholic "
             "Church bought it back in 1874, making it one of the oldest churches in England in Catholic use.",
             "en:St Etheldreda's Church, London", ("1280s", "Bishops of Ely", "1874", "oldest churches in England to be in current use by the Catholic Church"),
             "1078287", "survivals"),
            ("St Bartholomew-the-Great", "Q1093271",
             "Founded as an Augustinian priory church in 1123, it has appeared in many films, including the "
             "fourth wedding in Four Weddings and a Funeral and scenes of Shakespeare in Love.",
             "en:St Bartholomew-the-Great", ("1123", "Four Weddings and a Funeral", "Shakespeare in Love"),
             "1180873", "survivals"),
            ("Marble Arch", "Q845529",
             "Nash designed it in 1827 as the state entrance to Buckingham Palace; it was moved here in 1851. "
             "Three small rooms in its attic were used as a police station until at least 1968.",
             "en:Marble Arch", ("1827", "Buckingham Palace", "1851", "police station", "1968"),
             "1239534", "hidden rooms"),
            ("Imperial War Museum", "Q749808",
             "The museum, founded in 1917 to record the First World War, moved in 1936 into the building of the "
             "former Bethlem Royal Hospital, the psychiatric hospital.",
             "en:Imperial War Museum", ("1917", "in 1936", "former Bethlem Royal Hospital"),
             "1385640", "hidden rooms"),
            ("Aldwych station", "Q990658",
             "Opened in 1907 as Strand, it closed in 1994. In both world wars its disused tunnels sheltered art "
             "from London's museums, and in the Second the Elgin Marbles were stored there.",
             "en:Aldwych tube station", ("1907", "Strand", "1994", "both world wars", "Elgin Marbles"),
             "1401034", "hidden rooms"),
            ("Down Street station", "Q450893",
             "The Mayfair station closed in 1932 for lack of passengers. In the Second World War Churchill and "
             "the war cabinet used it as a bunker; the station building still stands.",
             "en:Down Street tube station", ("1932", "Winston Churchill", "war cabinet", "The station building survives"),
             None, "hidden rooms"),
            ("Michelin House", "Q6836880",
             "The tyre company's first permanent British headquarters opened on 20 January 1911. Its stained-"
             "glass windows show the Michelin Man, Bibendum.",
             "en:Michelin House", ("20 January 1911", "stained-glass", "Bibendum"),
             "1080656", "odd details"),
            ("Brompton Oratory", "Q1769288",
             "During the Cold War, Soviet spies used the gap between the pillars and the wall at the front of the"
             " church as a dead drop.",
             "en:Brompton Oratory", ("Cold War", "dead drop", "Soviet spies"),
             "1358123", "odd details"),
            ("Kensington Roof Gardens", "Q6391481",
             "A private garden of 6,000 square metres opened in 1938 on top of the Derry & Toms department store."
             " Four flamingos live by its pond.",
             "en:Kensington Roof Gardens", ("6,000 square metres", "Derry & Toms", "1938", "four flamingos"),
             None, "odd details"),
            ("Admiralty Arch", "Q359256",
             "On the inside wall of the northernmost arch is a small human nose. The artist Rick Buckley put it "
             "there in 1997 in a protest against \"Big Brother\" surveillance.",
             "en:Admiralty Arch", ("nose", "Rick Buckley", "1997", "Big Brother"),
             "1238982", "odd details"),
        ]),
]


# ---------- deeper layers, researched separately (pipeline/drafts/) ----------
# blitz.py replaces the layer above; harrypotter.py and streetart.py are new layers; expand_a.py and expand_b.py add
# entries to existing layers; world_a.py and world_b.py are the country groups of 'The world in London'.
import importlib.util as _ilu
from pathlib import Path as _Path


def _draft(name):
    f = _Path(__file__).parent / "drafts" / f"{name}.py"
    if not f.exists():
        return None
    spec = _ilu.spec_from_file_location(f"drafts.{name}", f)
    m = _ilu.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


for _name in ("blitz", "harrypotter", "streetart"):
    _m = _draft(_name)
    if _m:
        CURATED[:] = [L for L in CURATED if L["id"] != _m.LAYER["id"]] + [_m.LAYER]

for _name in ("expand_a", "expand_b"):
    _m = _draft(_name)
    if _m:
        for _L in CURATED:
            # OVERLAPS: buildings another layer also claims, with a story of this layer's own; a building may sit in
            # several layers, each telling its part
            _L["entries"] = (list(_L["entries"]) + list(_m.LAYERS.get(_L["id"], []))
                             + list(getattr(_m, "OVERLAPS", {}).get(_L["id"], [])))

_groups = {}
for _name in ("world_a", "world_b"):
    _m = _draft(_name)
    if _m:
        _groups.update(_m.GROUPS)
# Eight colours a layer: Europe and the rest of the world are two layers.
_EUROPE = ["russia", "france", "germany", "italy", "ireland", "poland", "greece"]
for _id, _title, _keys, _intro in [
    ("world-europe", "The world in London: Europe", [k for k in _EUROPE if k in _groups],
     "Exiles, revolutionaries, refugees and traders from the rest of Europe, and the churches, clubs and embassies "
     "they left. Each colour is a country; every building carries its own story and source."),
    ("world", "The world in London: Asia, Africa, the Americas", [k for k in _groups if k not in _EUROPE],
     "Students, sailors, campaigners and whole communities from across the empire and beyond. Each colour is a "
     "country or a region; every building carries its own story and source."),
]:
    if _keys:
        CURATED.append(dict(id=_id, section="Faith and community", title=_title, era="1600s–today", intro=_intro,
                            groups=[(k, _groups[k][0]) for k in _keys],
                            entries=[tuple(e[:6]) + (k,) for k in _keys for e in _groups[k][2]]))
