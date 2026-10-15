"""DRAFT expansion A of eight existing context layers in pipeline/curated.py: fire, power, georgian, city, port,
eastend, pubs, railways. LAYERS holds NEW entries only; the existing entries stay as they are in curated.py.

Same entry format as curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or None,
group). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia article
(API prop=extracts, explaintext=1, redirects=1); all checks were run on 2026-10-15. Each QID was read from
Special:EntityData: it has P625, and that point falls inside one of the nine borough polygons in
data/raw/boundary.json (point-in-polygon). The NHLE number is the item's P1216, or None when it has none. No QID in
LAYERS appears in any layer of curated.py (as of 12:50, which already includes blitz, potter, streetart and world) or
in pipeline/drafts/*.py, and none appears twice here.

Counts (new + existing = total):
  fire      22 + 14 = 36   rebuilt 15, survived 7
  power     26 + 15 = 41   palaces 8, church and crown 1, parliament 11, courts 5, London government 1 (new group)
  georgian  29 + 15 = 44   churches 17 (new), houses 3, clubs 3 (new), Nash 6
  city      29 + 13 = 42   halls 10, institutions 7, press 2 (new), headquarters 10 (new)
  port      24 + 12 = 36   markets 9, trade 6, docks 7, sailors 2 (new)
  eastend   23 + 13 = 36   Jewish 2, Huguenot 5, Bangladeshi 1, community 12, trades 3
  pubs      40 + 13 = 53   pubs 26, coffee and tea 7, shops 7
  railways  30 + 15 = 45   termini 6, goods 2 (new), underground 21 (new), engineering 1
  223 new entries.

OVERLAPS (below LAYERS) holds 46 more entries that passed every check but whose QID is already used by 'blitz' (23)
or 'world' (23) in curated.py: Wren churches (St Magnus, St Mary Abchurch, St Michael Paternoster Royal, St
Andrew-by-the-Wardrobe, St Nicholas Cole Abbey, St Anne and St Agnes, St Augustine Watling Street, St James's
Piccadilly), Georgian churches and theatres, Lancaster House, Queen's Chapel, the two prisons, Waterloo and Victoria
stations, Liberty, Harrods and others. They are not in LAYERS. If the fire layer should own the Wren churches (it is
thin on them now), swap them in and drop them from 'blitz'.

Dropped during research:
- Not a building item, or no item with coordinates: Tower of London's St Thomas's Tower (only Traitors' Gate, an
  'entrance'), Chapter House and Pyx Chamber of Westminster Abbey, Lincoln's Inn Old Hall, FCDO Main Building,
  70 Whitehall (items are departments), Admiralty buildings Q114459664 (a complex that includes Admiralty Arch, already
  in 'secrets'), United Service Club and White's (no coordinates), RSA House (item is the society), Royal Opera Arcade
  (redirects to His Majesty's Theatre), York Terrace (street item), Lloyd's Register, Lloyd's of London, Sion College,
  City of London School, Guildhall School, Glaziers' Hall (all organisation items), Covent Garden, Shad Thames, Jacob's
  Island, Limehouse Basin (areas or a canal basin), Millwall Iron Works and Royal Doulton (companies), Royal Foundation
  of St Katharine (P576, moved), Flower and Dean Street (Rothschild Buildings arch), Jews' Temporary Shelter (charity),
  Fashion Street, Whitechapel Road market, Cable Street Mural, Camden Market stables (Q27082592 is a 'siding'),
  Bishopsgate Goodsyard (item is the old station), King's Cross gasholders, Charing Cross Hotel.
  Shops whose items are companies without coordinates: Berry Bros. & Rudd, Floris, John Lobb, Penhaligon's,
  Selfridges, Harvey Nichols, Gieves & Hawkes, Henry Poole, Smythson, Hamleys, Foyles, Daunt Books, Turnbull & Asser,
  Swaine, Purdey.
- Livery halls rebuilt after the war with no Wikidata building item: Mercers', Grocers', Haberdashers', Clothworkers',
  Barber-Surgeons', Saddlers', Pewterers', Girdlers', Bakers', Butchers', Plaisterers', Leathersellers', Wax
  Chandlers'. Cordwainers' and Broderers' halls are gone.
- Listed building items exist, but no English article names the building, so there is nothing to check against:
  Tallow Chandlers' Hall (company article silent), Soup Kitchen for the Jewish Poor (Q27084928), 2, 4 and 27 Fournier
  Street (the street article names only Nos 14 and 23), Hanbury Street, Elder Street, Folgate Street and Wilkes Street
  houses, Truman's Vat House, New Concordia Wharf, Hope Sufferance Wharf, Thames Tunnel Mills, Cardinal's Wharf,
  Winchester Wharf, Gun, Metropolitan and New Crane Wharves, St Katharine Docks Dockmaster's Office and Warehouse C,
  West India Docks Quadrangle Stores and guard house, Granary Building at King's Cross, Gilbey House (Camden).
- No article or no item found: Peterborough Court (Daily Telegraph), Montefiore Centre, Kobi Nazrul Centre,
  Congregation of Jacob Synagogue, Mayflower (Rotherhithe), Jerusalem Tavern, Lamb Tavern (Leadenhall), Wiltons,
  D. R. Harris, Garrard, Thomas Goode, Dickens Inn, Cannon Workshops, Ledger Building, Dockmaster's House (West India
  Quay), Cutler Street warehouses, Sailors' Home.
- Gone or not standing as a building: City Hall, Southwark (110 The Queen's Walk, under partial demolition), Pavilion
  Theatre, Whitechapel (closed 1935, demolished), City Road station (P576), St Mary Aldermanbury (moved to Missouri).
- Off theme or outside the period: Schomberg House (1694), Fenton House (1680s), Lauderdale House (16th c.),
  Dartmouth House (Victorian remodel), Reform Club (1837-41), St Paul's Covent Garden (1633), Lindsey House (1640,
  outside the fire), St Botolph's Aldgate (rebuilt 1744), St Anne's Soho (tower only), Westminster and Southwark
  cathedrals (not crown buildings), Guy's Hospital (QID covers Guy's Tower), Bromley Hall (Tudor, no migrant link),
  Greenwich foot tunnel entrance and Rotherhithe Tunnel portal (not railway), Southwark station (1999).
- Verified but cut for length (pubs and railways would pass 60): Ship Tavern Lime Street (now a Nando's), Simpson's
  Tavern (closed 2022), Star Tavern, The Harp, Hand and Shears, Rising Sun, Nell Gwynne, Argyll Arms, Windsor Castle,
  King's Head and Eight Bells, The Tipperary, Wenlock Arms, Old Red Lion Islington, Holly Bush, Churchill Arms, Golden
  Heart, Two Chairmen, Crocker's Folly, Fox and Anchor, Red Lion Duke of York Street, Quo Vadis, Princes Arcade, Bon
  Marché Brixton, Truefitt & Hill, Ede & Ravenscroft, Heal's, Asprey; Tufnell Park, Bayswater, High Street Kensington,
  Leicester Square, Wapping and St James's Park (inside 55 Broadway) stations.

Doubts to check before publishing:
- Items whose type is an institution, business or museum but that carry the building's point (as in curated.py):
  Royal Mews, Wesley's Chapel, Brooks's, Boodle's, Travellers Club, Bishopsgate Institute, Barnard's Inn, St Bride
  Library, Kirkaldy Testing Museum, Young V&A, Museum of the Home, Ragged School Museum, Limehouse Town Hall, London
  Canal Museum, London Transport Museum (the 1871 Flower Market), Royal Vauxhall Tavern, Peter Jones, Paxton &
  Whitfield, James Smith & Sons, L. Cornelissen & Son, Bar Italia, Regency Café, Kettner's, Sweetings, the pubs.
- P576 is set on St Mary Somerset (body demolished 1871; the tower stands) and Bow Street Magistrates' Court (closed
  2006; the building is now a hotel).
- Bloody, Wakefield and Beauchamp towers and Waterloo Barracks cite the Tower of London article; they sit inside the
  same walls as the White Tower ('power'). Byward Tower has its own article.
- Ivory House: used Q27085107, the NHLE item 'Warehouse I' at St Katharine Docks; I take it to be Ivory House from its
  position, but the label does not say so.
- Neighbours of existing entries that may land on the same footprint: Whitechapel Library (now part of the Whitechapel
  Gallery), Neuve Eglise school and vestry (beside Brick Lane Mosque), Truman's Director's House (inside the Black
  Eagle Brewery), Euston entrance lodges (in front of Euston station), Great Northern Hotel (beside King's Cross),
  Tower Bridge accumulator tower.
- Several entries cite an area or street article with a listed-building QID: Wapping (Pier Head, police station),
  Bermondsey (Leather Market, Leather, Hide and Wool Exchange), Fournier Street, Spitalfields (2 Princelet Street),
  Covent Garden (market building), Smithfield, Chiswell Street (Whitbread; the article puts the street in Islington,
  the item's point is in the City), London Docks, St Katharine Docks, Tower Bridge, Coal Drops Yard, Euston, King's
  Cross, Whitechapel Road, Whitechapel Gallery, Black Eagle Brewery, Brick Lane Mosque.
- A few story facts go beyond the checks and rest on general knowledge: Wapping Pier Head as late Georgian houses at
  the old London Docks entrance; 41-42 Cloth Fair built before 1666 in a precinct the fire did not reach.
- Current state: Smithfield General Market is being fitted out for the London Museum; East London Central Synagogue
  closed in 2020 and is for sale; Fieldgate Street Great Synagogue is now a mosque; Old War Office and 55 Broadway are
  hotels or being converted; Cambridge House is being converted; Simpson's-in-the-Strand reopened in 2026; Jack Straw's
  Castle (in OVERLAPS) is flats.
- New groups added: power 'London government' (only County Hall now), georgian 'churches' and 'clubs', city 'press'
  and 'headquarters', port 'sailors', railways 'goods' and 'underground'. 'London government' and 'goods' are small and
  could be folded into 'parliament' and 'termini'.
"""

LAYERS = {
    "fire": [
        ("St Mary-at-Hill", "Q7594548",
         "The fire came up from nearby Pudding Lane and badly damaged the church. Wren rebuilt the interior "
         "and east end and kept the medieval walls on the other three sides.",
         "en:St Mary-at-Hill", ("Pudding Lane", "retain its medieval walls on the other three sides"),
         "1064600", "rebuilt"),
        ("St Margaret Lothbury", "Q12067886",
         "Recorded since the 12th century, burned in 1666 and rebuilt by Wren's office behind the Bank of "
         "England. It is the official church of five livery companies.",
         "en:St Margaret Lothbury", ("rebuilt by the office of Sir Christopher Wren", "five Livery Companies"),
         "1064634", "rebuilt"),
        ("St Margaret Pattens", "Q7594134",
         "Rebuilt by Wren in 1687 after the fire, it is one of the few City churches that came through the "
         "Second World War without serious damage.",
         "en:St Margaret Pattens", ("built by Sir Christopher Wren in 1687", "escaped significant damage"),
         "1286593", "rebuilt"),
        ("St Michael, Cornhill", "Q7594823",
         "Only the medieval tower survived the fire. The church was begun again in 1672, and the upper parts "
         "of the tower were finished by Nicholas Hawksmoor.",
         "en:St Michael, Cornhill", ("begun in 1672", "The upper parts of the tower are by Nicholas Hawksmoor"),
         "1286688", "rebuilt"),
        ("St Peter upon Cornhill", "Q7595372",
         "It stands on the highest point of the City, over the foundations of the Roman basilica. Wren rebuilt "
         "it after the fire.",
         "en:St Peter upon Cornhill", ("highest point of the City of London", "rebuilt to the designs of Sir Christopher Wren"),
         "1192245", "rebuilt"),
        ("St Clement Eastcheap", "Q7592845",
         "Rebuilt in the 1680s; the parish accounts for 1685 record wine given to Sir Christopher Wren. It is "
         "one of two churches that claim the 'Clements' of 'Oranges and Lemons'.",
         "en:St Clement's, Eastcheap", ("rebuilt in the 1680s", "given to Sir Christopher Wren", "Oranges and Lemons"),
         "1064699", "rebuilt"),
        ("St Edmund, King and Martyr", "Q3495311",
         "Built in 1670–1679 to designs by Robert Hooke, signed off by Wren. The flaming urns on the tower "
         "refer to the Great Fire.",
         "en:St Edmund, King and Martyr", ("Robert Hooke", "1670–1679", "flaming urns"),
         "1064631", "rebuilt"),
        ("St Martin, Ludgate", "Q7594206",
         "Built from 1677 to 1684 to Wren's design on Ludgate Hill. Seen from Fleet Street, its thin spire "
         "stands in front of the dome of St Paul's.",
         "en:St Martin, Ludgate", ("1677 to 1684", "designed by Sir Christopher Wren", "the steeple stands between the viewer and the dome of St Paul's Cathedral"),
         "1359194", "rebuilt"),
        ("St Benet's, Paul's Wharf", "Q1116552",
         "Wren's brick church replaced one lost in the fire. It has been the church of the College of Arms "
         "since 1556 and is now a Welsh church.",
         "en:St Benet's, Paul's Wharf", ("College of Arms", "Welsh Anglican church", "designed by Sir Christopher Wren"),
         "1180700", "rebuilt"),
        ("St Mary Woolnoth", "Q7594608",
         "The fire-damaged church was patched up and later replaced by Nicholas Hawksmoor's design, built from "
         "1716 and reopened on Easter Day 1727.",
         "en:St Mary Woolnoth", ("Nicholas Hawksmoor", "Work began in 1716", "Easter Day 1727"),
         "1064620", "rebuilt"),
        ("St Sepulchre-without-Newgate", "Q3495354",
         "The fire left only the outer walls, tower and porch. Rebuilt in 1667–1679, it is the largest parish "
         "church in the City; its bells are the 'bells of Old Bailey' in the nursery rhyme.",
         "en:St Sepulchre-without-Newgate", ("Rebuilt between 1667 and 1679", "the largest parish church in the City", "bells of Old Bailey"),
         "1064640", "rebuilt"),
        ("St Andrew Holborn", "Q7592413",
         "The medieval church survived the fire after a late change of wind, but it was in poor repair, and "
         "Wren rebuilt it anyway as his largest parish church.",
         "en:St Andrew Holborn (church)", ("last minute change in wind direction", "his largest parish church"),
         "1064643", "rebuilt"),
        ("St Mary Somerset", "Q7594603",
         "One of the 51 churches rebuilt by Wren's office. The body of the church was pulled down in 1871; the "
         "tower still stands on Upper Thames Street.",
         "en:St Mary Somerset", ("51 churches", "demolished in 1871", "Upper Thames Street"),
         "1358904", "rebuilt"),
        ("St Olave Old Jewry", "Q7594994",
         "Rebuilt by Wren's office after the fire in the street of the medieval Jewish quarter. The church was "
         "demolished in 1887 except for the tower and west wall.",
         "en:St Olave's Church, Old Jewry", ("rebuilt by the office of Sir Christopher Wren", "demolished in 1887", "tower and west wall"),
         "1359180", "rebuilt"),
        ("St Paul's Deanery", "Q17526843",
         "The dean's house was rebuilt around 1670 after the fire; whether Wren designed it is not documented. "
         "Since 1996 it has been the Bishop of London's palace.",
         "en:St Paul's Deanery", ("around 1670", "not well documented", "Bishop of London's palace"),
         "1064683", "rebuilt"),
        ("St Andrew Undershaft", "Q7592425",
         "Built in 1532 and one of the few City churches to survive both the Great Fire and the Blitz. It is "
         "named after a maypole that once stood beside it.",
         "en:St Andrew Undershaft", ("survived both the Great Fire of London and the Blitz", "constructed in 1532", "maypole"),
         "1079155", "survived"),
        ("St Katharine Cree", "Q3736898",
         "Built in 1628–1630 and consecrated by William Laud, whose ceremony was later used against him at his "
         "trial. It escaped the fire in 1666.",
         "en:St Katharine Cree", ("1628 to 1630", "William Laud", "escaped the Great Fire of London in 1666"),
         "1064627", "survived"),
        ("All Hallows Staining", "Q4728804",
         "The church survived the fire but collapsed five years later in 1671. Only its tower of around 1320 "
         "still stands.",
         "en:All Hallows Staining", ("survived the Great Fire of London in 1666 but collapsed five years later", "built around AD 1320"),
         "1064605", "survived"),
        ("St Bartholomew-the-Less", "Q7592618",
         "The hospital church at Barts. Its 15th-century tower and west front were outside the area the fire "
         "burned; two of its bells date from 1380 and 1420.",
         "en:St Bartholomew-the-Less", ("15th century", "1380 and 1420", "St Bartholomew's Hospital"),
         "1180946", "survived"),
        ("Staple Inn", "Q7600449",
         "A timber-framed building of 1585, once the wool staple where wool was weighed and taxed. It survived "
         "the fire, and a bomb in 1944.",
         "en:Staple Inn", ("Staple Inn dates from 1585", "survived the Great Fire of London", "weighed and taxed"),
         "1246103", "survived"),
        ("St Dunstan-in-the-West", "Q277004",
         "In 1666 forty Westminster School boys put out the flames with buckets and saved the old church. The "
         "present octagonal church dates from the 1830s.",
         "en:St Dunstan-in-the-West", ("40 scholars from Westminster School", "narrowly escaped the Great Fire", "constructed in the 1830s"),
         "1064663", "survived"),
        ("41-42 Cloth Fair", "Q46995380",
         "Numbers 41 and 42 Cloth Fair, beside St Bartholomew-the-Great, are described as the oldest house in "
         "the City. They were built before 1666 in the former priory precinct, which the fire did not reach.",
         "en:Cloth Fair", ("numbers 41 and 42", "oldest residential dwelling in London"),
         "1064703", "survived"),
    ],
    "power": [
        ("Byward Tower", "Q1018727",
         "Henry III's 13th-century gatehouse guarding the south-west entrance to the Tower, with a drawbridge, "
         "two portcullises and murder holes.",
         "en:Byward Tower", ("built in the 13th century by Henry III", "two portcullises", "murder holes"),
         None, "palaces"),
        ("Chapel Royal of St Peter ad Vincula", "Q1938714",
         "The Tower's parish church, rebuilt in 1520. It is a royal peculiar under the monarch's own "
         "jurisdiction.",
         "en:Church of St Peter ad Vincula", ("dates from 1520", "royal peculiar"),
         "1357540", "palaces"),
        ("Waterloo Barracks", "Q2552591",
         "The Duke of Wellington laid the foundation stone in 1845. Built for 1,000 soldiers, the block now "
         "holds the Crown Jewels on its ground floor.",
         "en:Tower of London", ("Waterloo Barracks", "the Duke of Wellington laid the foundation stone", "housing the Crown Jewels on the ground floor"),
         "1242210", "palaces"),
        ("Bloody Tower", "Q885290",
         "Built as a water-gate into the inner ward. It took its name in the 16th century, when it was "
         "believed to be where the Princes in the Tower were murdered.",
         "en:Tower of London", ("the Bloody Tower", "acquired its name in the 16th century", "Princes in the Tower"),
         None, "palaces"),
        ("Wakefield Tower", "Q2540867",
         "One of Henry III's towers on the river side of the inner ward, next to the king's private "
         "apartments.",
         "en:Tower of London", ("Wakefield Tower", "the king's apartments"),
         None, "palaces"),
        ("Beauchamp Tower", "Q813349",
         "Built under Edward I in the 13th century, it was the first large-scale use of brick in Britain since "
         "the Romans left.",
         "en:Tower of London", ("13th-century Beauchamp Tower", "first large-scale use of brick"),
         None, "palaces"),
        ("Royal Mews", "Q2903817",
         "The royal stables moved from Charing Cross to the grounds of Buckingham Palace in the 1820s. Horses, "
         "carriages and cars for state occasions are still kept there.",
         "en:Royal Mews", ("since the 1820s", "north side of Charing Cross", "royal carriages"),
         "1066364", "palaces"),
        ("Wellington Barracks", "Q3567182",
         "Opened in 1833 about 300 yards from Buckingham Palace, so the Foot Guards can reach the palace "
         "quickly.",
         "en:Wellington Barracks", ("opened in 1833", "300 yards", "Foot Guards"),
         None, "palaces"),
        ("Church House", "Q2967665",
         "Headquarters of the Church of England on Dean's Yard. Parliament met here during the Second World "
         "War, and the UN Security Council held its first meeting here.",
         "en:Church House, Westminster", ("Dean's Yard", "first meeting of the United Nations Security Council", "during the Second World War"),
         "1264037", "church and crown"),
        ("Horse Guards", "Q492350",
         "Built in the mid-18th century as barracks and stables for the Household Cavalry, it was the main "
         "military headquarters of the British Empire until 1858.",
         "en:Horse Guards (building)", ("mid-18th century", "Household Cavalry", "main military headquarters"),
         "1066100", "parliament"),
        ("Admiralty House", "Q779754",
         "Built beside the old Admiralty on Whitehall and connected to it; it now holds government rooms and "
         "ministerial flats.",
         "en:Admiralty House, London", ("ministerial flats", "Ripley Building"),
         "1267114", "parliament"),
        ("Old War Office", "Q58454576",
         "Home of the War Office, which ran the British Army from 1857 to 1964. The government sold it in 2016 "
         "for more than £350 million and it became a hotel.",
         "en:War Office", ("between 1857 and 1964", "sold on 1 March 2016", "luxury hotel"),
         "1224143", "parliament"),
        ("Government Offices Great George Street", "Q5589008",
         "John Brydon won the competition in 1898 with a design derived from Inigo Jones's plans for a new "
         "Whitehall Palace. HM Treasury occupies it.",
         "en:Government Offices Great George Street", ("John Brydon", "1898", "Inigo Jones"),
         "1066103", "parliament"),
        ("Dover House", "Q1031925",
         "James Paine built it as a private house in the 1750s; Henry Holland remodelled it for the Duke of "
         "York. It is now the London office of the Scotland Office.",
         "en:Dover House", ("James Paine", "Henry Holland", "Scotland Office"),
         "1066101", "parliament"),
        ("Gwydyr House", "Q5623756",
         "Built in 1772 for Peter Burrell and used for official purposes since 1871. It is the London "
         "headquarters of the Wales Office.",
         "en:Gwydyr House", ("in 1772", "Since 1871", "Wales Office"),
         "1066107", "parliament"),
        ("Ministry of Defence Main Building", "Q43303652",
         "Designed by E. Vincent Harris in 1915 but built only between 1939 and 1959, on part of the site of "
         "the Palace of Whitehall.",
         "en:Ministry of Defence Main Building (United Kingdom)", ("E. Vincent Harris", "between 1939 and 1959", "Palace of Whitehall"),
         "1278223", "parliament"),
        ("Portcullis House", "Q1757027",
         "Offices for 213 MPs, opened in 2001 above the rebuilt Westminster tube station. Michael Hopkins and "
         "Partners designed it.",
         "en:Portcullis House", ("opened in 2001", "213 members", "Michael Hopkins and Partners"),
         None, "parliament"),
        ("Norman Shaw Buildings", "Q7052782",
         "Richard Norman Shaw's red-and-white buildings on the Embankment were New Scotland Yard, the "
         "Metropolitan Police headquarters, from 1890 to 1967. MPs use them as offices now.",
         "en:Norman Shaw Buildings", ("New Scotland Yard", "between 1890 and 1967", "parliamentary offices"),
         None, "parliament"),
        ("11 Downing Street", "Q2403633",
         "Built alongside Number 10 in 1682 and the chancellor of the exchequer's official residence since "
         "1828.",
         "en:11 Downing Street", ("in 1682", "until 1828", "chancellor of the exchequer"),
         "1356989", "parliament"),
        ("Methodist Central Hall", "Q81473",
         "A Methodist church and conference hall opposite Westminster Abbey. The first session of the United "
         "Nations General Assembly was held in its Great Hall in 1946.",
         "en:Methodist Central Hall, Westminster", ("first session of the United Nations General Assembly in 1946", "Great Hall"),
         "1264457", "parliament"),
        ("Middlesex Guildhall", "Q1164504",
         "Built in the early 20th century for Middlesex County Council and its courts, it has housed the "
         "Supreme Court of the United Kingdom since 2009.",
         "en:Middlesex Guildhall", ("Supreme Court of the United Kingdom", "Middlesex County Council", "J. S. Gibson"),
         "1226369", "courts"),
        ("Bow Street Magistrates' Court", "Q4950658",
         "London's best-known magistrates' court and police station. The building of 1881 closed in 2006 after "
         "the court's 266 years on the street.",
         "en:Bow Street Magistrates' Court and Police Station", ("opened in 1881", "closed in 2006", "266-year existence"),
         "1066393", "courts"),
        ("Middlesex Sessions House", "Q6841945",
         "Built on Clerkenwell Green between 1780 and 1782 as the courthouse of the Middlesex Quarter "
         "Sessions, replacing Hicks Hall.",
         "en:Middlesex Sessions House", ("built in 1780", "Middlesex Quarter Sessions", "Hicks Hall"),
         "1298072", "courts"),
        ("Inner London Sessions House", "Q15228705",
         "A courthouse has stood here since George Gwilt's Surrey County Sessions House of 1791, next to "
         "Horsemonger Lane Gaol. It is still a Crown Court.",
         "en:Inner London Crown Court", ("George Gwilt the Elder", "Surrey County Sessions House in 1791", "Horsemonger Lane Gaol"),
         "1385732", "courts"),
        ("Public Record Office", "Q1167115",
         "Built from 1851 on Chancery Lane as the Public Record Office, the 'strong-box of the Empire'. King's "
         "College London bought it in 2001 and made it the Maughan Library.",
         "en:Maughan Library", ("strong-box of the Empire", "built in 1851", "acquired by the university in 2001"),
         "1359155", "courts"),
        ("County Hall", "Q2916209",
         "Ralph Knott's headquarters for the London County Council, opened by George V in 1922. It lost its "
         "role as the seat of London's government when the GLC was abolished in 1986.",
         "en:County Hall, London", ("Ralph Knott", "opened by King George V in 1922", "London County Council", "abolished the GLC in 1986"),
         "1358192", "London government"),
    ],
    "georgian": [
        ("St Martin-in-the-Fields", "Q1335201",
         "James Gibbs's church of 1722–1726, with a temple portico and a steeple rising behind it. The design "
         "was copied widely, particularly in the United States.",
         "en:St Martin-in-the-Fields", ("James Gibbs in 1722–1726", "Trafalgar Square", "copied particularly widely in the United States"),
         "1217661", "churches"),
        ("St Mary le Strand", "Q536866",
         "The first of the churches built by the Commission for Building Fifty New Churches. James Gibbs began "
         "it in 1714, his first major work after returning from Italy.",
         "en:St Mary le Strand", ("Commission for Building Fifty New Churches", "February 1714", "James Gibbs"),
         "1236753", "churches"),
        ("St George's, Bloomsbury", "Q7588083",
         "Nicholas Hawksmoor's church for the new Bloomsbury district, consecrated in 1730. Its crypt holds "
         "the Museum of Comedy.",
         "en:St George's, Bloomsbury", ("Nicholas Hawksmoor", "consecrated in 1730", "Museum of Comedy"),
         "1272341", "churches"),
        ("St James's, Clerkenwell", "Q7593465",
         "Built from 1788 to replace the old church of the dissolved nunnery of St Mary, which the parish had "
         "used since 1540.",
         "en:St James's Church, Clerkenwell", ("1540–1788", "1792–present", "nunnery"),
         "1207786", "churches"),
        ("St Peter, Vere Street", "Q7595345",
         "James Gibbs designed this chapel off Oxford Street in 1722 for Edward Harley, Earl of Oxford. It was "
         "called the Oxford Chapel until 1832.",
         "en:St Peter, Vere Street", ("designed by James Gibbs in 1722", "Oxford Chapel", "Edward Harley"),
         "1357345", "churches"),
        ("St Leonard's, Shoreditch", "Q7593974",
         "The present church dates from about 1740. Its bells are the 'bells of Shoreditch' in 'Oranges and "
         "Lemons', and Tudor actors are buried in the crypt.",
         "en:St Leonard's, Shoreditch", ("dates from about 1740", "say the bells of Shoreditch", "actors from the Tudor period"),
         "1235382", "churches"),
        ("St John-at-Hackney", "Q5117438",
         "Built in 1792 for about 2,000 people to replace Hackney's medieval church; the old tower of St "
         "Augustine still stands in the churchyard.",
         "en:Church of St John-at-Hackney", ("built in 1792", "St Augustine's Tower", "around 2,000"),
         "1226959", "churches"),
        ("St John-at-Hampstead", "Q7593635",
         "Hampstead's parish church on Church Row, consecrated in 1747. John Constable is buried in the "
         "churchyard.",
         "en:St John-at-Hampstead", ("consecrated on 8 October 1747", "John Constable", "Church Row"),
         "1271918", "churches"),
        ("St George the Martyr, Southwark", "Q545935",
         "The Borough church beside the wall of the Marshalsea prison, where Dickens's father was held for "
         "debt. Dickens set scenes of Little Dorrit in and around it.",
         "en:St George the Martyr, Southwark", ("Marshalsea", "Little Dorrit", "imprisoned for debt"),
         "1378366", "churches"),
        ("St Luke Old Street", "Q7594071",
         "Designed by John James and Nicholas Hawksmoor and used as a parish church from 1733 to 1959. Left "
         "roofless for 40 years, it reopened in 2003 as LSO St Luke's.",
         "en:St Luke Old Street", ("John James and Nicholas Hawksmoor", "from 1733 to 1959", "LSO St Luke's"),
         "1195700", "churches"),
        ("Wesley's Chapel", "Q7983825",
         "Opened in 1778 under John Wesley, who lived in the house next door. It is called 'the Mother Church "
         "of World Methodism'.",
         "en:Wesley's Chapel", ("Opened in 1778", "John Wesley's House", "The Mother Church of World Methodism"),
         "1195538", "churches"),
        ("St Anne's Limehouse", "Q2150581",
         "Hawksmoor's church for the riverside parish of Limehouse, consecrated in 1730. It was one of twelve "
         "churches built under the 1711 Act.",
         "en:St Anne's Limehouse", ("consecrated in 1730", "1711 Act of Parliament", "Hawksmoor"),
         "1357808", "churches"),
        ("St Mary on Paddington Green", "Q7594636",
         "John Plaw's Greek-cross church in yellow brick, consecrated in 1791. Hogarth was married in the "
         "church that stood here before it.",
         "en:St Mary on Paddington Green Church", ("consecrated in 1791", "John Plaw", "William Hogarth was married"),
         "1065972", "churches"),
        ("St John's Downshire Hill", "Q17526548",
         "A proprietary chapel built for the new houses of Downshire Hill in Hampstead and completed in 1823.",
         "en:St John's Downshire Hill", ("proprietary chapel", "completed in 1823"),
         "1078270", "churches"),
        ("St Mary's, Bryanston Square", "Q7594231",
         "Robert Smirke's Commissioners' church of 1823–1824, placed to close the view up Bryanston Square, "
         "with a round portico and tower.",
         "en:St Mary's, Bryanston Square", ("1823–1824", "Robert Smirke", "Commissioners' churches"),
         "1224993", "churches"),
        ("Holy Trinity, Marylebone", "Q14993437",
         "John Soane's church of 1828, one of the 'Waterloo churches' paid for from the million pounds "
         "Parliament voted after the defeat of Napoleon.",
         "en:Holy Trinity Church, Marylebone", ("built in 1828", "John Soane", "Waterloo churches"),
         "1267658", "churches"),
        ("St John on Bethnal Green", "Q15059608",
         "John Soane's church on the green at Bethnal Green, built in 1826–1828.",
         "en:St John on Bethnal Green", ("1826–1828", "Sir John Soane"),
         "1065245", "churches"),
        ("Lansdowne House", "Q6487389",
         "Robert Adam designed it for the Earl of Bute, who sold it in 1763 to the Earl of Shelburne. In the "
         "1930s the garden rooms were demolished for a new road; one drawing room went to the Philadelphia "
         "Museum of Art.",
         "en:Lansdowne House", ("Robert Adam", "Earl of Bute", "in 1763", "garden front rooms", "Philadelphia Museum of Art"),
         "1066795", "houses"),
        ("Bourdon House", "Q17549567",
         "A Mayfair house built between 1723 and 1725, extended around 1737 and raised by a storey around "
         "1760.",
         "en:Bourdon House", ("between 1723 and 1725", "around 1737", "around 1760"),
         "1210196", "houses"),
        ("Cambridge House", "Q5025454",
         "A Piccadilly mansion named after the Duke of Cambridge, a son of George III. Lord Palmerston leased "
         "it while Prime Minister; later it was the Naval and Military Club.",
         "en:Cambridge House", ("Duke of Cambridge", "Palmerston", "Naval and Military Club"),
         "1226748", "houses"),
        ("Brooks's", "Q929928",
         "A Whig club founded in 1764. Henry Holland built its clubhouse on St James's Street, finished in "
         "October 1778.",
         "en:Brooks's", ("March 1764", "Henry Holland", "October 1778"),
         "1264849", "clubs"),
        ("Boodle's", "Q14996889",
         "Founded in 1762 by Lord Shelburne. Since 1782 the club has occupied 28 St James's Street, designed "
         "by John Crunden in 1775.",
         "en:Boodle's", ("January 1762", "John Crunden in 1775", "28 St James's Street"),
         None, "clubs"),
        ("Travellers Club", "Q492221",
         "Founded in 1819 for gentlemen who had travelled abroad. Charles Barry designed its Pall Mall "
         "clubhouse as a Renaissance palace, before he designed the Houses of Parliament.",
         "en:Travellers Club", ("established in 1819", "Sir Charles Barry", "Renaissance palace"),
         "1266151", "clubs"),
        ("Hanover Terrace", "Q5649434",
         "Designed by John Nash in 1822 facing Regent's Park, with a pediment filled with terracotta figures.",
         "en:Hanover Terrace", ("designed by John Nash in 1822", "terracotta"),
         "1279085", "Nash"),
        ("Sussex Place", "Q96407050",
         "Nash's terrace of 1823 with ten pointed cupolas, built as 26 houses. The London Business School "
         "occupies it.",
         "en:Sussex Place", ("completed in 1823", "ten pointed cupolas", "London Business School"),
         "1264092", "Nash"),
        ("Cornwall Terrace", "Q5172013",
         "One of the first terraces built in Regent's Park for the Prince Regent's scheme, at the park's "
         "south-west corner near Baker Street.",
         "en:Cornwall Terrace", ("one of the earliest buildings constructed", "Prince Regent"),
         "1356971", "Nash"),
        ("Gloucester Gate", "Q17526561",
         "Nash's terrace of eleven houses, finished in 1827. Henry Wellcome lived at No. 6.",
         "en:Gloucester Gate", ("completed in 1827", "eleven terraced houses", "Sir Henry Wellcome"),
         "1078322", "Nash"),
        ("Clarence Terrace", "Q5126771",
         "The smallest terrace in Regent's Park, designed by Decimus Burton and named after William IV.",
         "en:Clarence Terrace", ("smallest in the park", "Decimus Burton", "named after William IV"),
         "1357311", "Nash"),
        ("Cambridge Terrace", "Q5025552",
         "Nash's terrace of 1825, named after the Duke of Cambridge and smaller than its neighbour Chester "
         "Terrace.",
         "en:Cambridge Terrace", ("completed in 1825", "Chester Terrace"),
         "1244296", "Nash"),
    ],
    "city": [
        ("Innholders' Hall", "Q17548989",
         "Hall of the innkeepers' company in College Street, between Cannon Street and Upper Thames Street. "
         "The company ranks 32nd among the livery companies.",
         "en:Worshipful Company of Innholders", ("Innholders' Hall in College Street", "32nd"),
         "1064708", "halls"),
        ("Painter-Stainers' Hall", "Q17645371",
         "The painters' and decorators' company has its hall between Huggin Hill and Little Trinity Lane, in "
         "Queenhithe ward. It ranks 28th in precedence.",
         "en:Worshipful Company of Painter-Stainers", ("between Huggin Hill and Little Trinity Lane", "twenty-eighth"),
         "1002030", "halls"),
        ("Cutlers' Hall", "Q26350798",
         "Opened in 1888 on Warwick Lane, on a site once used by the Royal College of Physicians. A terracotta "
         "frieze on the brick front shows the stages of knife-making.",
         "en:Worshipful Company of Cutlers", ("Cutlers' Hall opened in 1888", "Royal College of Physicians", "Warwick Lane", "terracotta frieze depicting the processes of knife-making"),
         "1079113", "halls"),
        ("Carpenters' Hall", "Q26350872",
         "The carpenters' hall on Throgmorton Avenue. The Carpenters' Company of Philadelphia, founded in "
         "1724, was modelled on this company.",
         "en:Worshipful Company of Carpenters", ("Carpenters Hall, is at Throgmorton Avenue", "Carpenters' Company of the City and County of Philadelphia"),
         "1079135", "halls"),
        ("Armourers' Hall", "Q17645539",
         "The company has held this corner of Coleman Street and London Wall since 1346. Its hall escaped the "
         "Great Fire; it was rebuilt in 1839, and the lantern added in 1872.",
         "en:Worshipful Company of Armourers and Brasiers", ("since 1346", "escape destruction in the Great Fire", "rebuild it completely", "added in 1872"),
         "1002056", "halls"),
        ("Dyers' Hall", "Q17645546",
         "The dyers' first hall, west of London Bridge, burned in 1666. The present hall on Dowgate Hill was "
         "designed by Charles Dyer and built in 1839–40.",
         "en:Worshipful Company of Dyers", ("designed by Charles Dyer and constructed in 1839–40", "Dowgate Hill"),
         "1002057", "halls"),
        ("Salters' Hall", "Q27087426",
         "Basil Spence's concrete hall on Fore Street, built in 1976 after the company's old hall in St "
         "Swithin's Lane was bombed in 1941.",
         "en:Worshipful Company of Salters", ("dates from 1976", "Sir Basil Spence", "bombed in 1941"),
         "1396374", "halls"),
        ("Founders' Hall", "Q66479347",
         "The metal founders' hall in Cloth Fair, built between 1985 and 1987 and listed Grade II*.",
         "en:Worshipful Company of Founders", ("Livery Hall in Cloth Fair", "built between 1985 and 1987"),
         "1452864", "halls"),
        ("Ironmongers' Hall", "Q122214094",
         "The ironmongers' hall in Fenchurch Street was hit by a bomb in 1917. The company built a new hall in "
         "Aldersgate Street, opened on 17 June 1925.",
         "en:Worshipful Company of Ironmongers", ("Aldersgate Street", "opened on 17 June 1925", "7 July 1917"),
         "1485812", "halls"),
        ("Brewers' Hall", "Q114308609",
         "The brewers lost their first hall in the Great Fire and the second in the Blitz. The present hall in "
         "Aldermanbury Square was rebuilt in 1960.",
         "en:Worshipful Company of Brewers", ("Rebuilt in 1960", "Aldermanbury Square", "bombed during the Blitz in 1940"),
         None, "halls"),
        ("Chartered Accountants' Hall", "Q17548947",
         "John Belcher's Baroque Revival headquarters for the Institute of Chartered Accountants, with "
         "sculpture worked into the facade. It made Belcher's name.",
         "en:Chartered Accountants' Hall", ("John Belcher", "Baroque Revival", "Institute of Chartered Accountants"),
         "1064586", "institutions"),
        ("Gibson Hall", "Q16992820",
         "Built as head office of the National Provincial Bank of England and completed in 1865, with statues "
         "along the parapet. The banking hall was used as such until 1982.",
         "en:Gibson Hall, London", ("National Provincial Bank of England", "completed in 1865", "John Gibson", "served its original purpose until 1982"),
         "1191569", "institutions"),
        ("Midland Bank, Poultry", "Q17526784",
         "Edwin Lutyens's headquarters for the Midland Bank, built in 1924–1929, when it was the largest bank "
         "in the world. It is now The Ned hotel.",
         "en:Midland Bank, Poultry", ("between 1924 and 1929", "Edwin Lutyens", "largest bank in the world", "The Ned"),
         "1064598", "institutions"),
        ("Bishopsgate Institute", "Q2904689",
         "A library and adult education institute founded in 1895, in a building by Charles Harrison Townsend, "
         "who also designed the Whitechapel Gallery.",
         "en:Bishopsgate Institute", ("established in 1895", "Charles Harrison Townsend", "Whitechapel Gallery"),
         "1191674", "institutions"),
        ("Barnard's Inn", "Q4861410",
         "A former Inn of Chancery with a hall that keeps 15th-century timbers. The Mercers' School used it "
         "until 1959; Gresham College gives free public lectures there now.",
         "en:Barnard's Inn", ("former Inn of Chancery", "Mercers' School premises until 1959", "Gresham College"),
         None, "institutions"),
        ("St Bride Foundation", "Q7592712",
         "An institute off Fleet Street that houses the St Bride Library of printing, typography and graphic "
         "design.",
         "en:St Bride Library", ("St Bride Foundation Institute", "printing, book arts, typography"),
         "1251908", "institutions"),
        ("Freemasons' Hall", "Q1453586",
         "Headquarters of the United Grand Lodge of England on Great Queen Street, a Masonic meeting place "
         "since 1775. The present Art Deco building, the third on the site, was built from 1927.",
         "en:Freemasons' Hall, London", ("United Grand Lodge of England", "since 1775", "Art Deco", "The current building, the third on this site, was built between 1927"),
         "1113218", "institutions"),
        ("85 Fleet Street", "Q26317812",
         "Lutyens designed this building for the Reuters news agency on the former site of Punch magazine; it "
         "was completed in 1935.",
         "en:85 Fleet Street", ("Reuters", "Punch magazine", "completed in 1935"),
         "1064656", "press"),
        ("Carmelite House", "Q26317860",
         "A printing house built in 1897–1899 for newspapers and publishers. It is the oldest surviving "
         "combined office and newspaper factory in the Fleet Street area.",
         "en:Carmelite House", ("between 1897 and 1899", "the oldest survivor of its kind"),
         "1064727", "press"),
        ("Unilever House", "Q2494434",
         "Lever Brothers' London headquarters on the site of Henry VIII's Bridewell Palace, with a curved "
         "front facing Blackfriars Bridge.",
         "en:Unilever House", ("Bridewell Palace", "Lever Brothers", "Blackfriars Bridge"),
         "1079095", "headquarters"),
        ("Britannic House", "Q17548972",
         "Lutyens's office block of 1921–1925 for the Anglo-Persian Oil Company, later BP. At 38 metres it "
         "needed special consent to exceed the height limit.",
         "en:Britannic House, Finsbury Circus", ("between 1921 and 1925", "Anglo-Persian Oil Company", "38 metres"),
         "1064691", "headquarters"),
        ("Adelaide House", "Q4681735",
         "An Art Deco office block of the 1920s by John Burnet and Thomas Tait at the north end of London "
         "Bridge, with Egyptian details inspired by the find of Tutankhamun's tomb.",
         "en:Adelaide House", ("Sir John Burnet and Thomas S. Tait", "Tutankhamen's tomb", "London Bridge"),
         "1064621", "headquarters"),
        ("King Edward Building", "Q17549146",
         "London's main post office and sorting office for most of the 20th century. Henry Tanner designed it; "
         "it opened in 1910 and closed in the 1990s.",
         "en:King Edward Building", ("Sir Henry Tanner", "opened in 1910", "largest public post office in the UK"),
         "1286242", "headquarters"),
        ("Salisbury House", "Q27086024",
         "Built in 1899–1901 as a speculative office block, the first of the large blocks that replaced the "
         "houses around Finsbury Circus.",
         "en:Salisbury House, London", ("between 1899 and 1901", "speculative development", "Finsbury Circus"),
         "1375270", "headquarters"),
        ("Ibex House", "Q27082437",
         "An eleven-storey Streamline Moderne office block of 1935–1937 near the Minories, with curved corners "
         "and bands of faience.",
         "en:Ibex House", ("Streamline Moderne", "completed in 1937", "faience"),
         "1252467", "headquarters"),
        ("Telephone House", "Q26350845",
         "Built in 1898–1902 for the National Telephone Company, which had merged many small telephone "
         "networks.",
         "en:Telephone House, London", ("between 1898 and 1902", "National Telephone Company"),
         "1079128", "headquarters"),
        ("Hamilton House", "Q26350780",
         "Offices on the Victoria Embankment built in 1898–1901 for the Employers Liability Corporation, "
         "designed by William Emerson.",
         "en:Hamilton House, London", ("between 1898 and 1901", "Employers Liability Corporation", "Sir William Emerson"),
         "1079106", "headquarters"),
        ("Britannia House", "Q27082400",
         "Edwardian Baroque offices on Old Bailey built for the London, Chatham and Dover Railway, with "
         "sculptures of rail and sea travel over the door.",
         "en:Britannia House", ("London, Chatham and Dover Railway", "rail and sea travel"),
         "1251982", "headquarters"),
        ("Five Kings House", "Q27085754",
         "Built in 1911 by Thomas Collcutt and Stanley Hamp for Liebig's Extract of Meat Company, with "
         "sculpture by Richard Garbe.",
         "en:Five Kings House", ("built in 1911", "Liebig's Extract of Meat Company", "Richard Garbe"),
         "1358918", "headquarters"),
    ],
    "port": [
        ("Smithfield Poultry Market", "Q18161799",
         "Built in 1961–1963 after fire destroyed the Victorian poultry market in 1958. Its concrete shell "
         "roof is claimed as the largest clear-spanning dome in Europe.",
         "en:Smithfield Poultry Market", ("1961–1963", "destroyed by fire in 1958", "largest clear spanning dome roof in Europe"),
         "1381209", "markets"),
        ("Smithfield Central Market", "Q17549122",
         "Horace Jones's meat market building, part of the covered market that replaced the live cattle market "
         "at Smithfield in the second half of the 19th century.",
         "en:Smithfield, London", ("Sir Horace Jones", "covered market building"),
         "1285241", "markets"),
        ("Caledonian Park Clock Tower", "Q108907464",
         "The main survivor of the Metropolitan Cattle Market, opened by the City in 1855 to replace the live "
         "market at Smithfield. It had four pubs, one at each corner.",
         "en:Caledonian Park Clock Tower", ("Metropolitan Cattle Market", "opened in 1855", "four public houses"),
         "1298021", "markets"),
        ("Covent Garden Market Building", "Q17549514",
         "Charles Fowler's neo-classical building of 1830 put a roof over the fruit and vegetable market. The "
         "market moved to Nine Elms in 1974.",
         "en:Covent Garden", ("Charles Fowler's neo-classical building was erected in 1830", "Nine Elms"),
         "1066949", "markets"),
        ("Jubilee Market Hall", "Q21027173",
         "Built in 1904 on the south side of the Covent Garden piazza. It is the only London market wholly "
         "owned by its traders.",
         "en:Jubilee Market", ("built in 1904", "wholly owned by traders"),
         "1356973", "markets"),
        ("Leather, Hide and Wool Exchange", "Q26665803",
         "Built in 1878 for Bermondsey's tanning trade, next to the Leather Market of 1833. Like most of the "
         "area's warehouses it is now flats and offices.",
         "en:Bermondsey", ("Leather, Hide and Wool Exchange of 1878", "Leather Market of 1833"),
         "1386047", "markets"),
        ("Leather Market", "Q26665802",
         "The huge market hall of 1833 at the centre of Bermondsey's leather trade, when tanneries filled the "
         "streets around it.",
         "en:Bermondsey", ("Leather Market of 1833", "processing and trading of leather and hides"),
         "1386046", "markets"),
        ("Smithfield General Market", "Q30512346",
         "One of Horace Jones's five Smithfield market buildings. Damaged in the Second World War and later "
         "disused, it is being converted for the Museum of London.",
         "en:Smithfield General Market", ("designed by Horace Jones", "damaged during the Second World War", "General Market Building"),
         None, "markets"),
        ("London Canal Museum", "Q6670203",
         "A warehouse built in 1862–1863 for Carlo Gatti to store ice shipped from Norway and brought up the "
         "Regent's Canal. It has been a canal museum since 1992.",
         "en:London Canal Museum", ("former ice warehouse that was used by Carlo Gatti", "between 1862 and 1863", "imported from Norway", "opened in 1992"),
         None, "trade"),
        ("Billingsgate Fish Market", "Q2911699",
         "Britain's largest inland fish market, moved in 1982 from the old riverside hall in the City to a "
         "shed at the end of the West India Docks' North Dock.",
         "en:Billingsgate Fish Market", ("largest inland fish market", "moved from Old Billingsgate in 1982", "North Dock of the West India Docks"),
         None, "markets"),
        ("St Olaf House", "Q17531484",
         "Art Deco headquarters of the Hay's Wharf Company, built in 1928–1932 by H. S. Goodhart-Rendel on the "
         "site of St Olave's Church. Its front has 39 terracotta panels by Frank Dobson.",
         "en:St Olaf House", ("between 1928 and 1932", "Hay's Wharf Company", "Goodhart-Rendel", "39 terracotta panels designed by Frank Dobson"),
         "1385977", "trade"),
        ("Anchor Brewhouse", "Q4752667",
         "John Courage bought the brewhouse by Tower Bridge in 1787. The building was restored in 1985–1989 "
         "and converted into flats.",
         "en:Anchor Brewhouse", ("December 1787", "John Courage", "converted into luxury residential flats"),
         None, "trade"),
        ("Menier Chocolate Factory", "Q6817045",
         "A five-storey factory and warehouse built in the 1870s by the French Menier chocolate company. Part "
         "of it is now a 180-seat theatre.",
         "en:Menier Chocolate Factory", ("Menier Chocolate Company", "180-seat", "five-storey factory"),
         "1385925", "trade"),
        ("Kirkaldy Testing Works", "Q6415564",
         "David Kirkaldy tested the strength of materials here for engineers. His huge testing machine is "
         "still inside.",
         "en:Kirkaldy Testing Museum", ("David Kirkaldy", "huge testing machine", "99 Southwark Street"),
         "1385928", "trade"),
        ("Whitbread Brewery", "Q27082433",
         "Samuel Whitbread brought his brewing together on Chiswell Street in 1750. Beer was brewed here for "
         "225 years until 1976.",
         "en:Chiswell Street", ("In 1750, Samuel Whitbread", "brewed here for 225 years", "closed in 1976"),
         "1252353", "trade"),
        ("Wapping Pier Head", "Q27082760",
         "Late Georgian houses at the old entrance to the London Docks, once the local headquarters of the "
         "Customs and Excise.",
         "en:Wapping", ("Wapping Pier Head", "headquarters of the Customs and Excise"),
         "1260059", "docks"),
        ("Wapping Police Station", "Q27081836",
         "Base of the Marine Police Force, set up in 1798 to stop theft from ships in the Pool of London. The "
         "river police still work from Wapping High Street.",
         "en:Wapping", ("Marine Police Force was formed in 1798", "Wapping High Street", "Thames Police Museum"),
         "1242394", "docks"),
        ("Oliver's Wharf", "Q26318839",
         "A tea warehouse of 1870 for 60,000 packages. In 1972 it became the first Wapping warehouse converted "
         "into flats.",
         "en:Oliver's Wharf", ("built in 1870", "60,000 packages", "In 1972"),
         "1065806", "docks"),
        ("Burrells Wharf", "Q5000413",
         "Part of the Millwall Iron Works, where John Scott Russell built Brunel's SS Great Eastern, the "
         "largest ship in the world, launched in 1858. The buildings are now flats.",
         "en:Burrells Wharf", ("Millwall Iron Works", "John Scott Russell", "SS Great Eastern"),
         None, "docks"),
        ("Pennington Street warehouses", "Q26318858",
         "Surviving warehouses and vaults of the London Docks, which handled luxury goods such as ivory, "
         "spices, coffee and wine.",
         "en:London Docks", ("ivory, spices, coffee and cocoa", "wine cellars"),
         "1065825", "docks"),
        ("Ivory House", "Q27085107",
         "A warehouse at St Katharine Docks, which opened in 1828 to a scheme by Thomas Telford with "
         "warehouses by Philip Hardwick. The docks closed in 1968.",
         "en:St Katharine Docks", ("Ivory House", "Thomas Telford", "Philip Hardwick", "From 1828 to 1968"),
         "1357856", "docks"),
        ("Tower Bridge accumulator tower", "Q26665739",
         "Tower Bridge was raised by water pressure stored in hydraulic accumulators and pumped by steam "
         "engines; this tower and chimney belonged to that system.",
         "en:Tower Bridge", ("hydraulic accumulators", "stationary steam engines"),
         "1385982", "docks"),
        ("St Paul's, Shadwell", "Q7595141",
         "Known as the Church of Sea Captains; some 75 captains are said to be buried here. It became "
         "Shadwell's parish church in 1669.",
         "en:St Paul's Church, Shadwell", ("Church of Sea Captains", "75 sea captains", "rebuilt in 1669 as the Parish Church of Shadwell"),
         "1357840", "sailors"),
        ("St Peter's, London Docks", "Q15979503",
         "A mission church for the dockside poor of Wapping, begun by Charles Lowder in 1856; the church was "
         "built from 1865.",
         "en:St Peter's, London Docks", ("Charles Lowder", "first Anglican mission to the poor of London", "1865"),
         "1065844", "sailors"),
    ],
    "eastend": [
        ("Fieldgate Street Great Synagogue", "Q5447159",
         "An Orthodox congregation founded in 1899 that worshipped here in the Ashkenazi rite. The building "
         "was sold in 2015 and has since been used as a mosque.",
         "en:Fieldgate Street Great Synagogue", ("Established in 1899", "Ashkenazi rite", "sold in 2015"),
         None, "Jewish"),
        ("East London Central Synagogue", "Q60746590",
         "Founded in 1923 as the Nelson Street Sfardish Synagogue, with a plain front and a richly decorated "
         "interior. Services stopped in 2020.",
         "en:East London Central Synagogue", ("founded in 1923", "Nelson Street Sfardish Synagogue", "ceased functioning in 2020"),
         None, "Jewish"),
        ("Howard House, 14 Fournier Street", "Q27081739",
         "Built around 1726 by the carpenter William Taylor and later leased to silk weavers. The silk for "
         "Queen Victoria's coronation gown was woven in its garret.",
         "en:Fournier Street", ("No. 14 Fournier Street", "built circa 1726", "Queen Victoria's Coronation gown"),
         "1240855", "Huguenot"),
        ("23 Fournier Street", "Q27085102",
         "A single-fronted early Georgian house with a weather-boarded garret and the wide windows that gave "
         "weavers light for their looms.",
         "en:Fournier Street", ("No. 23 Fournier Street", "wide weaver's windows", "weather boarded front"),
         "1357851", "Huguenot"),
        ("2 Princelet Street", "Q27085138",
         "Anna Maria Garthwaite, who designed silk patterns for the Spitalfields weavers in the 18th century, "
         "lived here; a blue plaque marks the house.",
         "en:Spitalfields", ("Anna Maria Garthwaite", "designer of silk fabrics; blue plaque at 2 Princelet Street"),
         "1357887", "Huguenot"),
        ("Sutton House", "Q7650284",
         "Built in 1535 for Ralph Sadler, Henry VIII's secretary of state, and the oldest house in Hackney. In "
         "the 18th century it was let to a succession of Huguenot tenants.",
         "en:Sutton House, London", ("built in 1535 by Sir Ralph Sadler", "oldest residential building in Hackney", "succession of Huguenot tenants"),
         "1226810", "Huguenot"),
        ("Neuve Eglise school and vestry", "Q26318387",
         "Former school buildings beside the Brick Lane chapel that Huguenots opened in 1743. The chapel later "
         "became a synagogue and then the mosque; the school is now part of the mosque.",
         "en:Brick Lane Mosque", ("first established in 1743", "Neuve Eglise", "former school buildings"),
         "1065278", "Huguenot"),
        ("Tower Hamlets Town Hall", "Q108911633",
         "The front of the Royal London Hospital, opened in 1757, kept as the face of the council's new "
         "headquarters. The new town hall opened in 2023 on Whitechapel Road.",
         "en:Tower Hamlets Town Hall", ("opened in September 1757", "opened on 1 March 2023", "Royal London Hospital"),
         "1065788", "Bangladeshi"),
        ("Oxford House", "Q7115369",
         "One of the first university settlements, founded by Oxford men in 1884 as a High Church counterpart "
         "to Toynbee Hall. Arthur Blomfield's building opened in 1892.",
         "en:Oxford House (settlement)", ("September 1884", "Toynbee Hall", "Sir Arthur Blomfield"),
         "1396458", "community"),
        ("People's Palace", "Q27087209",
         "The first People's Palace of 1887 gave East Enders a library, classes and entertainment. After a "
         "fire in 1931 it was rebuilt; it is now part of Queen Mary University of London.",
         "en:People's Palace, Mile End", ("People's Palace (1887)", "destroyed by a fire in 1931", "Queen Mary University of London"),
         "1393150", "community"),
        ("Young V&A", "Q644281",
         "The iron hall was first put up in South Kensington in 1856–7 and moved here in 1872 as the Bethnal "
         "Green Museum. It is now the V&A's museum for children.",
         "en:Young V&A", ("founded in 1872", "Bethnal Green Museum", "prefabricated building"),
         "1357777", "community"),
        ("Museum of the Home", "Q2918086",
         "Grade I almshouses of the 18th century on Kingsland Road, now a museum of home life from 1600 to the "
         "present.",
         "en:Museum of the Home", ("former almshouses on Kingsland Road", "Geffrye Museum", "from 1600"),
         "1226772", "community"),
        ("Ragged School Museum", "Q7282907",
         "Dr Barnardo's Copperfield Road school opened in 1877 and had more than 1,000 pupils on weekdays "
         "before it closed in 1908.",
         "en:Ragged School Museum", ("Copperfield Road Ragged School", "opened in 1877", "closed in 1908"),
         None, "community"),
        ("York Hall", "Q4205978",
         "Public baths and hall opened by the Duke and Duchess of York in 1929, best known for professional "
         "boxing.",
         "en:York Hall", ("opened in 1929", "boxing venue", "Duke and Duchess of York"),
         "1412973", "community"),
        ("Bethnal Green Library", "Q27087071",
         "Opened in 1922 on the site of Wright's Madhouse, a private asylum that closed in 1920.",
         "en:Bethnal Green Library", ("13 October 1922", "Wright's Madhouse", "asylum closed in 1920"),
         "1391330", "community"),
        ("Bethnal Green Town Hall", "Q26318353",
         "Baroque town hall of the Metropolitan Borough of Bethnal Green, opened on 1 November 1910.",
         "en:Bethnal Green Town Hall", ("1 November 1910", "Metropolitan Borough of Bethnal Green"),
         "1065243", "community"),
        ("Whitechapel Library", "Q26318777",
         "The Passmore Edwards public library next to the Whitechapel Gallery. The gallery took over the "
         "building in 2009 and doubled in size.",
         "en:Whitechapel Gallery", ("Passmore Edwards library building", "In 2009"),
         "1065733", "community"),
        ("St Augustine with St Philip's Church", "Q17531647",
         "A red-brick church of 1888–1892 behind the Royal London Hospital, converted into a medical library.",
         "en:St Augustine with St Philip's Church, Whitechapel", ("built in 1888–1892", "medical library", "Arthur Cawston"),
         "1065066", "community"),
        ("Limehouse Town Hall", "Q15059599",
         "The vestry hall of the Limehouse District, opened on 29 March 1881 on Commercial Road.",
         "en:Limehouse Town Hall", ("29 March 1881", "Commercial Road", "Palazzo style"),
         "1240047", "community"),
        ("Shoreditch Town Hall", "Q27081424",
         "Built in 1865–66 as the vestry hall of St Leonard's parish on the site of Fuller's Hospital "
         "almshouses. It is now an arts and events venue.",
         "en:Shoreditch Town Hall", ("completed in 1866", "Fuller's Hospital", "Caesar Augustus Long"),
         "1235232", "community"),
        ("Albion Brewery", "Q26318855",
         "Founded in 1808 by Richard Ivory, landlord of the Blind Beggar, and rebuilt in 1860. The entrance "
         "block survives on Whitechapel Road.",
         "en:Whitechapel Road", ("established at the eastern end of Whitechapel Road in 1808", "Richard Ivory", "In 1860, the brewery was rebuilt"),
         "1065822", "trades"),
        ("Beigel Bake", "Q4881063",
         "A 24-hour bakery on Brick Lane, open since 1974, making beigels in the Jewish style with salt beef "
         "and smoked salmon.",
         "en:Beigel Bake", ("24-hour bakery", "founded in 1974", "traditional Jewish style"),
         None, "trades"),
        ("Truman's Director's House", "Q98168873",
         "The brewery director's house at Truman's Black Eagle Brewery, which by 1853 was the largest brewery "
         "in the world.",
         "en:Black Eagle Brewery", ("The Director's House", "largest in the world"),
         "1252152", "trades"),
    ],
    "pubs": [
        ("Ye Olde Mitre", "Q15979621",
         "A pub hidden in Ely Court, off Ely Place. Historic England dates the building to about 1773, with an "
         "interior remodelled in the early 20th century.",
         "en:Ye Olde Mitre", ("Ely Court", "built about 1773"),
         "1078281", "pubs"),
        ("Ye Olde Cock Tavern", "Q7725384",
         "The old tavern stood across Fleet Street until 1886, when a Bank of England branch took its site. It "
         "was rebuilt on the other side of the road with some of its old interior.",
         "en:Ye Olde Cock Tavern", ("22 Fleet Street", "on the other side of the road", "Bank of England"),
         "1192621", "pubs"),
        ("Seven Stars", "Q15979287",
         "A small pub behind the Royal Courts of Justice, probably dating from the 1680s, once called The Log "
         "and Seven Stars.",
         "en:Seven Stars, Holborn", ("Carey Street", "1680s", "The Log and Seven Stars"),
         "1244097", "pubs"),
        ("Cittie of Yorke", "Q5122929",
         "A 1920s rebuilding on a site where there have been pubs since 1430. The hall-like back room has a "
         "long bar and Victorian-style cubicles.",
         "en:Cittie of Yorke", ("pubs since 1430", "rebuilding of the 1920s", "cubicles"),
         "1378857", "pubs"),
        ("Hoop and Grapes", "Q16707742",
         "Probably built in the late 17th century, a timber-framed type Historic England calls once common in "
         "London but now very rare.",
         "en:Hoop and Grapes, Aldgate High Street", ("late 17th century", "once common in London but now very rare"),
         "1064735", "pubs"),
        ("Viaduct Tavern", "Q17030424",
         "A late-Victorian pub opposite the Old Bailey, built in 1874–5 and refitted inside in 1898–1900.",
         "en:Viaduct Tavern", ("built 1874–5", "1898–1900", "Newgate Street"),
         "1262465", "pubs"),
        ("Punch Tavern", "Q17361863",
         "Formerly the Crown and Sugar Loaf, renamed in the 1840s after Punch magazine, whose office was "
         "nearby. Rebuilt in 1894–97.",
         "en:The Punch Tavern", ("Crown and Sugar Loaf", "Punch magazine", "1894–95"),
         "1268142", "pubs"),
        ("Old Bell, Fleet Street", "Q26317813",
         "A 17th-century pub behind St Bride's, said to have been built by Wren for the masons working on the "
         "church.",
         "en:Old Bell, Fleet Street", ("17th century", "Christopher Wren for the use of his masons"),
         "1064658", "pubs"),
        ("The Olde Wine Shades", "Q24022951",
         "Built in 1663 as a merchant's house with a tunnel to the river; it is often said to have survived "
         "the Great Fire. The tunnel was sealed after bomb damage in 1940.",
         "en:The Olde Wine Shades", ("built in 1663", "tunnel river entrance", "Blitz in 1940"),
         "1359197", "pubs"),
        ("The Anchor, Bankside", "Q4752659",
         "Started as the tap room of the Anchor Brewery. Samuel Pepys watched the Great Fire from an alehouse "
         "on Bankside here in 1666.",
         "en:The Anchor, Bankside", ("brewery tap room", "Samuel Pepys observed the Great Fire of London"),
         "1376546", "pubs"),
        ("Captain Kidd", "Q28433128",
         "A former coffee warehouse on Wapping High Street, named after the pirate William Kidd, who was "
         "hanged at nearby Execution Dock.",
         "en:Captain Kidd, Wapping", ("coffee warehouse", "Execution Dock", "108 Wapping High Street"),
         "1242395", "pubs"),
        ("Ten Bells", "Q2414574",
         "The pub on the corner of Commercial Street and Fournier Street linked with Annie Chapman and Mary "
         "Jane Kelly, two victims of Jack the Ripper.",
         "en:Ten Bells", ("Commercial Street and Fournier Street", "Annie Chapman and Mary Jane Kelly"),
         "1065204", "pubs"),
        ("The Blind Beggar", "Q7718589",
         "William Booth preached the sermon here that led to the Salvation Army. Ronnie Kray shot George "
         "Cornell in the bar in front of witnesses.",
         "en:The Blind Beggar", ("William Booth's first sermon", "Ronnie Kray murdered George Cornell"),
         None, "pubs"),
        ("The Lamb", "Q7745280",
         "Built in the 1720s on Lamb's Conduit Street. It keeps the Victorian 'snob screens' that hid drinkers "
         "from the bar staff.",
         "en:The Lamb, Bloomsbury", ("built in the 1720s", "snob screens"),
         "1379276", "pubs"),
        ("Museum Tavern", "Q16707752",
         "Opposite the British Museum, rebuilt about 1855–64. The pub goes back to 1723, when it was called "
         "the Dog and Duck.",
         "en:Museum Tavern", ("1855–64", "From 1723 to 1762 the pub was called the Dog and Duck"),
         "1330367", "pubs"),
        ("Fitzroy Tavern", "Q5455720",
         "From the 1920s to the 1950s the meeting place of artists and writers such as Augustus John, Dylan "
         "Thomas and George Orwell.",
         "en:Fitzroy Tavern", ("Dylan Thomas", "George Orwell", "1920s to the mid-1950s"),
         None, "pubs"),
        ("Coach and Horses, Soho", "Q5137601",
         "A Greek Street pub known for Jeffrey Bernard, the staff of Private Eye and its landlord Norman "
         "Balon, 'London's rudest landlord'.",
         "en:Coach and Horses, Soho", ("Jeffrey Bernard", "Private Eye", "London's rudest landlord"),
         "1235282", "pubs"),
        ("Dog and Duck", "Q15978971",
         "Built in 1897 for the Cannon Brewery, with a tiled interior. George Orwell drank here; the upstairs "
         "room is named after him.",
         "en:Dog and Duck, Soho", ("built in 1897", "Cannon Brewery", "George Orwell"),
         "1264051", "pubs"),
        ("Red Lion, Westminster", "Q18161385",
         "The pub nearest Downing Street, used by MPs and parliamentary staff. A tavern stood on the spot as "
         "early as 1434.",
         "en:Red Lion, Westminster", ("watering hole for MPs", "As early as 1434"),
         "1226437", "pubs"),
        ("The Albert", "Q21008630",
         "A Victoria Street pub built in 1862 and named after Prince Albert. Its Victorian front and fittings "
         "came through the Blitz undamaged.",
         "en:The Albert", ("Built in 1862", "Albert, Prince Consort", "undamaged during The Blitz"),
         "1066148", "pubs"),
        ("Silver Cross Tavern", "Q15673036",
         "Licensed as a pub in 1674 on Whitehall. It is said a royal licence for a brothel on the building was "
         "never revoked.",
         "en:Silver Cross Tavern", ("in 1674", "brothel"),
         "1066104", "pubs"),
        ("The Grenadier", "Q7738264",
         "Built in 1720 as the officers' mess of the 1st Foot Guards and opened to the public in 1818. It is "
         "named after the Grenadier Guards' part at Waterloo.",
         "en:The Grenadier", ("built in 1720", "officers' mess", "opened to the public in 1818"),
         None, "pubs"),
        ("Morpeth Arms", "Q20878182",
         "Built in 1845 for the warders of Millbank Penitentiary. A first-floor room looks across the river at "
         "the MI6 headquarters.",
         "en:Morpeth Arms", ("built in 1845", "Millbank Penitentiary", "MI6"),
         "1222798", "pubs"),
        ("The Flask, Hampstead", "Q15957066",
         "On the site where Hampstead's mineral water was bottled and sold; it was once the Lower Flask. "
         "Young's has owned it since 1904.",
         "en:The Flask, Hampstead", ("Hampstead mineral water", "Lower Flask", "since 1904"),
         "1322190", "pubs"),
        ("Royal Vauxhall Tavern", "Q7374962",
         "Built in 1860–62 on part of the Vauxhall Pleasure Gardens. It is south London's oldest surviving "
         "queer venue.",
         "en:Royal Vauxhall Tavern", ("between 1860 and 1862", "Vauxhall Pleasure Gardens", "oldest surviving queer venue"),
         "1426984", "pubs"),
        ("The Devereux", "Q26319777",
         "Built in about 1676 as the Grecian Coffee House, off Essex Street. It was refitted as a pub in 1843.",
         "en:The Devereux", ("Grecian Coffee House", "about 1676", "1843"),
         "1066888", "coffee and tea"),
        ("The Old Bank of England", "Q26487354",
         "Arthur Blomfield's Italianate building of 1886 housed the Law Courts branch of the Bank of England "
         "until 1975. It has been a pub since 1994.",
         "en:The Old Bank of England", ("Sir Arthur Blomfield", "Law Courts branch of the Bank of England", "1975"),
         "1192681", "pubs"),
        ("George and Vulture", "Q12404791",
         "There has been an inn on this site off Lombard Street since 1142. Dickens mentions it many times in "
         "The Pickwick Papers.",
         "en:George and Vulture", ("since 1142", "The Pickwick Papers", "City Pickwick Club"),
         "1064728", "coffee and tea"),
        ("Sweetings", "Q23461994",
         "A fish restaurant at 39 Queen Victoria Street since 1889. It opens only on weekday lunchtimes and "
         "takes no bookings.",
         "en:Sweetings", ("since 1889", "weekday lunchtimes"),
         "1079140", "coffee and tea"),
        ("Bar Italia", "Q4857936",
         "Opened as a café in 1949 by the Polledri family. John Logie Baird gave the first public "
         "demonstration of television in the same building in 1926.",
         "en:Bar Italia", ("opened as a café in 1949", "John Logie Baird", "first public demonstration of television"),
         None, "coffee and tea"),
        ("Simpson's-in-the-Strand", "Q1783593",
         "Began in 1828 as a smoking room and coffee house. By 1850 it was known for roast meats and as "
         "Britain's most important chess venue.",
         "en:Simpson's-in-the-Strand", ("1828 as a smoking room", "roast meats", "venue in Britain for chess"),
         "1236740", "coffee and tea"),
        ("Regency Café", "Q15272240",
         "An Art Deco working men's café on Regency Street, open since 1946 and often used as a film location.",
         "en:Regency Café", ("opened in 1946", "art deco", "filming location"),
         None, "coffee and tea"),
        ("Kettner's", "Q27081433",
         "Founded in 1867 by Auguste Kettner, a chef to Napoleon III, as the first restaurant in London to "
         "serve French food.",
         "en:Kettner's Townhouse", ("founded in 1867", "Napoleon III", "first restaurant to serve French food"),
         "1235281", "coffee and tea"),
        ("Paxton & Whitfield", "Q2065291",
         "Cheesemongers since 1797, with roots in a market stall of 1742. The shop has been at 93 Jermyn "
         "Street since 1894.",
         "en:Paxton & Whitfield", ("founded in 1797", "1742", "in 1894"),
         None, "shops"),
        ("James Smith & Sons", "Q17542443",
         "An umbrella shop founded in 1830. Its New Oxford Street premises keep shop fittings of about 1865.",
         "en:James Smith & Sons", ("in 1830", "New Oxford Street", "around 1865"),
         "1113171", "shops"),
        ("Burlington Arcade", "Q2928520",
         "Built in 1818 for Lord George Cavendish on the side garden of Burlington House. It is often called "
         "the first modern shopping mall.",
         "en:Burlington Arcade", ("built in 1818", "Burlington House", "first modern shopping mall"),
         "1066338", "shops"),
        ("Royal Arcade", "Q7373669",
         "A Victorian arcade from Albemarle Street to Old Bond Street, completed in 1880 to designs by Archer "
         "& Green.",
         "en:Royal Arcade, London", ("Completed in 1880", "Archer & Green"),
         "1266365", "shops"),
        ("Piccadilly Arcade", "Q7190556",
         "Twenty-eight shops between Piccadilly and Jermyn Street, opened in 1909. Bombed in 1941, it was "
         "fully restored only in 1957.",
         "en:Piccadilly Arcade", ("opened in 1909", "twenty-eight shops", "1957"),
         "1265804", "shops"),
        ("Peter Jones", "Q7175031",
         "William Crabtree's store on Sloane Square for John Spedan Lewis, opened in 1936. It was the first "
         "modern-movement glass curtain wall in Britain.",
         "en:Peter Jones (department store)", ("William Crabtree", "opened in 1936", "John Spedan Lewis", "first modern-movement use of the glass curtain wall in Britain"),
         "1226626", "shops"),
        ("L. Cornelissen & Son", "Q140077411",
         "An artists' colourman founded in 1855 by Louis Cornelissen. The shop is now at 105 Great Russell "
         "Street.",
         "en:L. Cornelissen & Son", ("founded in 1855", "105 Great Russell Street"),
         None, "shops"),
    ],
    "railways": [
        ("Blackfriars station", "Q284195",
         "Its platforms run across Blackfriars Railway Bridge, the only London station that spans the Thames.",
         "en:Blackfriars station", ("Its platforms span the River Thames, the only station in London to do so",),
         None, "termini"),
        ("Great Northern Hotel", "Q26407124",
         "The railway hotel beside King's Cross station; the new western departures concourse, opened in 2012, "
         "sits behind it.",
         "en:London King's Cross railway station", ("Great Northern Hotel", "March 2012"),
         "1113244", "termini"),
        ("Great Eastern Hotel", "Q13529113",
         "Built in 1884 next to Liverpool Street station and enlarged in 1899–1901. It is now the Andaz hotel.",
         "en:Andaz London Liverpool Street", ("Great Eastern Hotel in 1884", "between 1899 and 1901"),
         "1252272", "termini"),
        ("Great Western Royal Hotel", "Q13529026",
         "Brunel's idea and the hotel's first managing director; it opened at Paddington on 9 June 1854.",
         "en:Great Western Royal Hotel", ("Isambard Kingdom Brunel", "opened on 9 June 1854", "Praed Street"),
         "1227144", "termini"),
        ("Grosvenor Hotel", "Q17550738",
         "Opened in 1862 beside Victoria station, with an entrance into the concourse. It was one of the first "
         "buildings in London with a French pavilion roof.",
         "en:The Clermont, Victoria", ("opened in 1862", "French pavilion roof", "station concourse"),
         "1357254", "termini"),
        ("Euston entrance lodges", "Q27084502",
         "Two Portland stone lodges on Euston Road are, with the war memorial, almost all that is left of the "
         "old Euston station after its demolition in the 1960s.",
         "en:Euston railway station", ("two Portland stone entrance lodges", "few relics of the old station survive"),
         "1342042", "termini"),
        ("London Necropolis station", "Q801117",
         "The London terminus of the railway that carried coffins and mourners to Brookwood Cemetery in "
         "Surrey. This second station worked from 1902 to 1941; its office building on Westminster Bridge Road "
         "survives.",
         "en:London Necropolis railway station", ("Brookwood Cemetery", "from 1902 to 1941", "121 Westminster Bridge Road"),
         "1249875", "goods"),
        ("Eastern Coal Drops", "Q27086622",
         "One of two Victorian sheds where coal from South Yorkshire was dropped from wagons into carts and "
         "canal boats. Thomas Heatherwick turned them into shops in 2018.",
         "en:Coal Drops Yard", ("South Yorkshire", "Thomas Heatherwick", "October 2018"),
         "1379214", "goods"),
        ("Farringdon station", "Q800754",
         "Opened in 1863 as the terminus of the Metropolitan Railway, the world's first underground passenger "
         "railway.",
         "en:Farringdon station", ("Opened in 1863", "world's first underground passenger railway"),
         None, "underground"),
        ("Great Portland Street station", "Q946924",
         "Opened in 1863 as Portland Road on the first Underground line. The present terracotta-clad building "
         "of 1930 stands on a traffic island in the Marylebone Road.",
         "en:Great Portland Street tube station", ("Portland Road", "built in 1930 on a traffic island", "terracotta"),
         "1213650", "underground"),
        ("Gloucester Road station", "Q1431088",
         "The Metropolitan Railway opened it as Brompton (Gloucester Road) on 1 October 1868. A disused "
         "platform is used for art installations.",
         "en:Gloucester Road tube station", ("Brompton (Gloucester Road) on 1 October 1868", "Art on the Underground"),
         "1080658", "underground"),
        ("South Kensington station", "Q976035",
         "Opened on 24 December 1868 by the Metropolitan and District railways, the station for the museums of "
         "South Kensington.",
         "en:South Kensington tube station", ("24 December 1868", "Royal Albert Hall"),
         "1392067", "underground"),
        ("Edgware Road station", "Q1284426",
         "On the first underground line of 1863. Fowler's original building was replaced in 1926–8 by one by "
         "Charles Walter Clark.",
         "en:Edgware Road tube station (Circle, District and Hammersmith & City lines)", ("10 January 1863", "Charles Walter Clark", "Sir John Fowler"),
         None, "underground"),
        ("Covent Garden station", "Q38879",
         "Opened in April 1907, four months after the rest of the Piccadilly line. Its frontage was listed in "
         "2011 as a good example of Leslie Green's architecture.",
         "en:Covent Garden tube station", ("11 April 1907", "four months after services on the rest of the line", "good example of Leslie Green's architecture"),
         "1401025", "underground"),
        ("Russell Square station", "Q1377634",
         "A Leslie Green station of 1906 in the Modern Style, the British version of Art Nouveau.",
         "en:Russell Square tube station", ("15 December 1906", "Leslie Green", "Art Nouveau"),
         "1401730", "underground"),
        ("Mornington Crescent station", "Q1890387",
         "Opened in 1907 on the Charing Cross, Euston & Hampstead Railway. It was shut in 1992 to replace its "
         "85-year-old lifts and stayed closed for years.",
         "en:Mornington Crescent tube station", ("22 June 1907", "23 October 1992", "85-year-old lifts"),
         "1378713", "underground"),
        ("Caledonian Road station", "Q1026585",
         "A Leslie Green station of 1906 that still uses lifts, which go straight down to platform level.",
         "en:Caledonian Road tube station", ("15 December 1906", "lifts descend directly to platform level"),
         "1401086", "underground"),
        ("Chalk Farm station", "Q599135",
         "Its narrow wedge-shaped building has the longest frontage of all of Leslie Green's stations. It "
         "opened on 22 June 1907.",
         "en:Chalk Farm tube station", ("longest frontage", "22 June 1907"),
         "1401028", "underground"),
        ("Hampstead station", "Q1573996",
         "Its platforms are the deepest on the Underground, 58.5 metres below ground, and its lift shaft is "
         "the deepest too. The tiled signs below still read Heath Street.",
         "en:Hampstead tube station", ("58.5 metres", "deepest lift shaft", "Heath Street"),
         None, "underground"),
        ("Lambeth North station", "Q1549587",
         "A Leslie Green station opened on 10 March 1906 as Kennington Road, briefly the southern end of the "
         "Bakerloo line.",
         "en:Lambeth North tube station", ("10 March 1906", "Kennington Road", "Leslie Green"),
         None, "underground"),
        ("Kennington station", "Q1738951",
         "Opened in 1890 on the world's first underground electric railway; its surface building is little "
         "changed.",
         "en:Kennington tube station", ("opened in 1890", "world's first underground electric railway", "surface building remains largely unaltered"),
         "1385635", "underground"),
        ("Oval station", "Q426804",
         "Opened on 18 December 1890 on the City and South London Railway and named after the cricket ground.",
         "en:Oval tube station", ("18 December 1890", "City and South London Railway", "cricket ground"),
         None, "underground"),
        ("Borough station", "Q894073",
         "Opened in 1890 on the City and South London Railway, the first successful deep-level tube, and "
         "rebuilt in 1922 when the tunnels were widened.",
         "en:Borough tube station", ("first successful deep-level tube railway", "rebuilt in 1922"),
         None, "underground"),
        ("York Road station", "Q2600828",
         "A Leslie Green station of 1906 that never had many passengers. It closed in 1932; the red-tiled "
         "building still stands at York Way.",
         "en:York Road tube station", ("opened in 1906", "closed in 1932", "Leslie Green"),
         None, "underground"),
        ("South Kentish Town station", "Q1532858",
         "Opened in 1907 and closed in 1924 because few people used it. The surface building is now a shop.",
         "en:South Kentish Town tube station", ("opened in 1907", "closed in 1924", "retail unit"),
         None, "underground"),
        ("55 Broadway", "Q3286924",
         "Charles Holden's headquarters for the Underground group, built in 1927–1929 above St James's Park "
         "station. It was the tallest office block in London when finished.",
         "en:55 Broadway", ("Charles Holden", "between 1927 and 1929", "tallest office block in London"),
         "1219790", "underground"),
        ("Holloway Road station", "Q1624885",
         "A Leslie Green station of 1906. Its second lift shaft held an experimental spiral escalator by Jesse "
         "Reno that was never opened to the public.",
         "en:Holloway Road tube station", ("15 December 1906", "spiral escalator", "Jesse W. Reno"),
         "1195635", "underground"),
        ("Piccadilly Circus station", "Q26448",
         "Charles Holden's circular booking hall under the Circus was built from 1925 to 1928 for more than "
         "£500,000.",
         "en:Piccadilly Circus tube station", ("completed in 1928", "Charles Holden", "£500,000"),
         "1226877", "underground"),
        ("Bow Road station", "Q895388",
         "Opened on 11 June 1902 by the Whitechapel and Bow Railway, linking the District with the line to "
         "Southend.",
         "en:Bow Road tube station", ("11 June 1902", "Whitechapel and Bow Railway"),
         "1357787", "underground"),
        ("London Transport Museum", "Q1541098",
         "The museum fills William Rogers's iron and glass flower market of 1871 in Covent Garden.",
         "en:London Transport Museum", ("flower market by William Rogers in 1871", "iron and glass"),
         None, "engineering"),
    ],
}

# Verified entries that collide with a building already used by another layer (blitz, world) in curated.py.
# Not in LAYERS. Kept here, checked, in case a swap is preferred: {layer: [(layer that has it now, entry)]}.
OVERLAPS = {
    "fire": [
        # now in 'blitz'
        ("St Magnus the Martyr", "Q7594088",
         "The church stood at the north end of old London Bridge, a few hundred yards from where the fire "
         "began. Wren rebuilt it between 1671 and 1687, and it was one of his most expensive churches.",
         "en:St Magnus the Martyr", ("between 1671 and 1687", "one of Wren's most expensive churches", "London Bridge"),
         "1064601", "rebuilt"),
        # now in 'blitz'
        ("St Mary Abchurch", "Q7594555",
         "Destroyed in the fire and rebuilt by Wren's office in 1681–1686. The parish of St Laurence Pountney, "
         "whose church was not rebuilt, was joined to it.",
         "en:St Mary Abchurch", ("1681–1686", "St Laurence Pontney", "destroyed in the Great Fire of London"),
         "1359119", "rebuilt"),
        # now in 'blitz'
        ("St Michael Paternoster Royal", "Q3583162",
         "Richard Whittington paid to rebuild the medieval church and was buried in it in 1423; his tomb was "
         "lost when the fire destroyed the church. Wren's office rebuilt it.",
         "en:St Michael Paternoster Royal", ("Whittington", "In 1423", "rebuilt under the aegis of Sir Christopher Wren"),
         "1286707", "rebuilt"),
        # now in 'blitz'
        ("St Andrew-by-the-Wardrobe", "Q7586911",
         "Named after Edward III's Royal Wardrobe, which burned with it in 1666. Wren's plain church went up "
         "in 1695; after the Blitz only the tower and walls were left.",
         "en:St Andrew-by-the-Wardrobe", ("Royal Wardrobe", "erected in 1695", "only the tower and walls survived"),
         "1079148", "rebuilt"),
        # now in 'blitz'
        ("St Nicholas Cole Abbey", "Q7594953",
         "Rebuilt by Wren's office after the fire, then reconstructed in 1961–62 after bomb damage. It was "
         "never an abbey: the name comes from 'coldharbour', a shelter.",
         "en:St Nicholas Cole Abbey", ("coldharbour", "The church was never an abbey", "1961–62"),
         "1079146", "rebuilt"),
        # now in 'blitz'
        ("St Anne and St Agnes", "Q3495309",
         "Only part of the 14th-century tower survived the fire. Wren rebuilt the church in 1680 as a small "
         "brick Greek cross, perhaps with Robert Hooke.",
         "en:St Anne and St Agnes", ("rebuilt by Sir Christopher Wren in 1680", "Greek cross", "Robert Hooke"),
         "1286384", "rebuilt"),
        # now in 'blitz'
        ("St Augustine Watling Street", "Q7592558",
         "Wren's church east of St Paul's was largely destroyed by bombing. Its tower now belongs to St Paul's "
         "Cathedral Choir School.",
         "en:St Augustine Watling Street", ("rebuilt to the designs of Christopher Wren", "St Paul's Cathedral Choir School"),
         "1079121", "rebuilt"),
        # now in 'blitz'
        ("St James's Piccadilly", "Q4893186",
         "Wren's church for the new West End estate of Henry Jermyn, consecrated in 1684, with a font and "
         "reredos by Grinling Gibbons.",
         "en:St James's Church, Piccadilly", ("consecrated on 13 July 1684", "Henry Jermyn", "Grinling Gibbons"),
         "1226621", "rebuilt"),
        # now in 'world'
        ("St Ethelburga's", "Q7593042",
         "A small medieval church, rebuilt around 1411, that the fire did not reach. An IRA bomb wrecked it in "
         "1993; it reopened as a centre for reconciliation and peace.",
         "en:St Ethelburga's Bishopsgate", ("rebuilt around 1411", "IRA bomb in 1993", "Centre for Reconciliation and Peace"),
         "1191603", "survived"),
    ],
    "power": [
        # now in 'world'
        ("Lancaster House", "Q1146311",
         "Begun in 1825 for the Duke of York and finished by the Duke of Sutherland as Stafford House. Chopin "
         "played there for Queen Victoria in 1848; the government now uses it for receptions and conferences.",
         "en:Lancaster House", ("10 October 1825", "Stafford House", "Chopin gave a recital there in 1848"),
         "1236546", "palaces"),
        # now in 'world'
        ("Queen's Chapel", "Q7269945",
         "Inigo Jones built it in 1623–1625 as a Catholic chapel for a Spanish princess Charles I never "
         "married; his French queen Henrietta Maria used it instead.",
         "en:Queen's Chapel", ("Inigo Jones", "between 1623 and 1625", "Henrietta Maria"),
         "1273605", "palaces"),
        # now in 'blitz'
        ("Guards' Chapel", "Q5614129",
         "On Sunday 18 June 1944 a V-1 flying bomb hit the chapel during the morning service, killing 121 "
         "people. The new chapel reused memorials from the old one.",
         "en:Guards' Chapel, Wellington Barracks", ("18 June 1944", "V-1 flying bomb", "121 people killed", "Using the memorials from the old chapel"),
         "1066441", "palaces"),
        # now in 'world'
        ("St Margaret's, Westminster", "Q823412",
         "The parish church in the grounds of Westminster Abbey, used for society weddings: Pepys, Milton and "
         "Winston Churchill were married here. Walter Raleigh is buried inside.",
         "en:St Margaret's, Westminster", ("Winston Churchill and Clementine Hozier", "Sir Walter Raleigh", "Samuel Pepys"),
         "1226286", "church and crown"),
        # now in 'blitz'
        ("Admiralty Citadel", "Q26319560",
         "A windowless concrete blockhouse behind Admiralty House, built in 1939 as a bomb-proof operations "
         "centre. It is the most visible of London's military citadels.",
         "en:Military citadels under London", ("Admiralty Citadel", "constructed in 1939", "London's most visible military citadel"),
         "1066638", "parliament"),
        # now in 'world'
        ("Pentonville Prison", "Q1504639",
         "Finished in 1842 with four wings radiating from a central hall, built to keep prisoners apart. It "
         "became the model for 54 more British prisons within six years.",
         "en:HM Prison Pentonville", ("completed in 1842", "four radiating wings", "Pentonville became the model"),
         None, "courts"),
        # now in 'world'
        ("Brixton Prison", "Q1764624",
         "Opened in 1820 as the Surrey House of Correction for 175 prisoners. It was overcrowded from the "
         "start.",
         "en:HM Prison Brixton", ("built in 1820", "Surrey House of Correction", "175 prisoners"),
         None, "courts"),
    ],
    "georgian": [
        # now in 'world'
        ("St George's, Hanover Square", "Q3495317",
         "John James's parish church for the new Mayfair estates; the first stone was laid in 1721. Handel "
         "worshipped here, and it became a church for society weddings.",
         "en:St George's, Hanover Square", ("John James", "first stone in 1721", "He was a regular worshipper at St George's", "society weddings"),
         "1235638", "churches"),
        # now in 'blitz'
        ("St John's Smith Square", "Q7593525",
         "Thomas Archer's Baroque church with four corner towers, completed in 1728, nicknamed 'Queen Anne's "
         "Footstool'. It is now a concert hall.",
         "en:Smith Square Hall", ("Thomas Archer", "completed in 1728", "Queen Anne's Footstool"),
         "1236250", "churches"),
        # now in 'world'
        ("St Giles in the Fields", "Q3495322",
         "The third church on the site of a 12th-century leper hospital chapel, rebuilt in Palladian style by "
         "Henry Flitcroft in 1731–1733.",
         "en:St Giles in the Fields", ("1731–1733", "Henry Flitcroft", "leper hospital"),
         "1245864", "churches"),
        # now in 'world'
        ("St Pancras New Church", "Q7595040",
         "A Greek Revival church of 1819–22 by William and Henry William Inwood. Its doorways and ornament are "
         "modelled on the Erechtheum in Athens.",
         "en:St Pancras New Church", ("built in 1819–22", "William and Henry William Inwood", "Erechtheum"),
         "1379062", "churches"),
        # now in 'blitz'
        ("St Marylebone Parish Church", "Q211300",
         "Thomas Hardwick's church of 1813–17 on the Marylebone Road. Lord Byron was baptised in the earlier "
         "church, and Nelson worshipped there.",
         "en:St Marylebone Parish Church", ("Thomas Hardwick in 1813–17", "Lord Byron was baptised", "Horatio Nelson"),
         "1239817", "churches"),
        # now in 'world'
        ("Grosvenor Chapel", "Q5610634",
         "Built in 1730–31 for Sir Richard Grosvenor's Mayfair estate. Its plain brick and white spire served "
         "as a model for churches in New England.",
         "en:Grosvenor Chapel", ("7 April 1730", "Sir Richard Grosvenor", "New England"),
         "1236429", "churches"),
        # now in 'world'
        ("Athenaeum Club", "Q492758",
         "Founded in 1824 for people of intellectual distinction; Humphry Davy and Michael Faraday were its "
         "first chairman and secretary. Decimus Burton designed the clubhouse with a copy of the Parthenon "
         "frieze.",
         "en:Athenaeum Club, London", ("founded in 1824", "Decimus Burton", "frieze of the Parthenon"),
         "1225842", "clubs"),
        # now in 'world'
        ("Theatre Royal, Drury Lane", "Q1756626",
         "The present theatre opened in 1812. It is the fourth on a site used since 1663, the oldest theatre "
         "site in London still in use.",
         "en:Theatre Royal, Drury Lane", ("opened in 1812", "since 1663", "oldest theatre site in London"),
         "1357276", "public buildings"),
        # now in 'world'
        ("Theatre Royal Haymarket", "Q540426",
         "The company dates from 1720. John Nash rebuilt the theatre on its present site in 1821, placing its "
         "portico to close the view along Charles Street.",
         "en:Theatre Royal Haymarket", ("dates back to 1720", "since 1821", "John Nash", "close the vista from Charles Street"),
         "1066641", "public buildings"),
    ],
    "city": [
        # now in 'world'
        ("Bracken House", "Q17549117",
         "Albert Richardson's headquarters for the Financial Times on a bomb site near St Paul's. Listed in "
         "1987, it was the first post-war building in England to be listed.",
         "en:Bracken House, London", ("Financial Times", "Sir Albert Richardson", "the first building built in England after the Second World War to become listed"),
         "1262582", "press"),
        # now in 'blitz'
        ("Electra House, Moorgate", "Q15216419",
         "Built in 1902 for the Eastern Telegraph companies, later Cable & Wireless. In the Second World War "
         "it housed Department EH, one of the bodies merged into the Special Operations Executive.",
         "en:Electra House", ("constructed in 1902", "Department EH", "Special Operations Executive"),
         "1251605", "headquarters"),
    ],
    "port": [
        # now in 'blitz'
        ("Port of London Authority Building", "Q7699363",
         "The Beaux Arts headquarters of the Port of London Authority at Tower Hill, overlooking the river. It "
         "has been a Four Seasons hotel since 2017.",
         "en:10 Trinity Square", ("Port of London Authority", "Beaux Arts", "Four Seasons Hotel"),
         "1079138", "trade"),
        # now in 'world'
        ("Royal Mint Court", "Q140783459",
         "Home of the Royal Mint from 1809 to 1967, on the site of a Cistercian abbey and later a navy "
         "victualling yard and tobacco warehouse. China bought the site in 2018 for its embassy.",
         "en:Royal Mint Court", ("from 1809 until 1967", "victualling yard", "tobacco warehouse", "Cistercian abbey"),
         None, "trade"),
        # now in 'world'
        ("St Mary's, Rotherhithe", "Q7590184",
         "The 18th-century riverside church of Rotherhithe. Christopher Jones, captain of the Mayflower that "
         "took the Pilgrim Fathers to America in 1620, is buried here.",
         "en:St Mary's Church, Rotherhithe", ("Pilgrim Fathers", "Christopher Jones"),
         "1385867", "sailors"),
        # now in 'blitz'
        ("St John's, Wapping", "Q27081780",
         "Wapping's parish church of 1756, bombed in the Second World War. Its tower still stands as a "
         "landmark.",
         "en:St John's Church, Wapping", ("date to 1756", "bombed during World War II", "the tower remains"),
         "1241683", "sailors"),
        # now in 'blitz'
        ("Trinity Green Almshouses", "Q17528170",
         "Built in 1695 by Trinity House for 28 retired ship's masters or their widows. They were restored "
         "after war damage in the 1950s.",
         "en:Trinity Green Almshouses", ("built in 1695", "Corporation of Trinity House", "28 decay"),
         "1241071", "sailors"),
        # now in 'blitz'
        ("St Dunstan's, Stepney", "Q7592980",
         "Known as the Mother Church of the East End and the Church of the High Seas. St Dunstan is said to "
         "have founded or refounded it around 952.",
         "en:St Dunstan's, Stepney", ("Church of the High Seas", "AD 952", "Mother Church of the East End"),
         "1065065", "sailors"),
    ],
    "eastend": [
        # now in 'blitz'
        ("St Matthew's, Bethnal Green", "Q7594708",
         "George Dance the Elder's church of 1743–46 for the weaving district of Bethnal Green. A fire in 1859 "
         "destroyed the interior.",
         "en:St Matthew's, Bethnal Green", ("built 1743–46", "George Dance the Elder", "fire in 1859"),
         "1065051", "Huguenot"),
        # now in 'world'
        ("St Boniface's German Church", "Q54006848",
         "Church of the German-speaking Catholics of East London, whose mission began in 1809. The Modernist "
         "building of 1959–60 replaced one destroyed in the Blitz.",
         "en:St Boniface's German Church, Whitechapel", ("founded in East London in 1809", "built in 1959–60", "destroyed in the London Blitz"),
         "1445649", "community"),
    ],
    "pubs": [
        # now in 'world'
        ("The French House", "Q7735253",
         "Opened in 1891 as the York Minster. Charles de Gaulle's Appeal of 18 June 1940 to the Free French is "
         "said to have been written here.",
         "en:The French House, Soho", ("York Minster", "in 1891", "Appeal of 18 June, is said to have been written in the pub"),
         None, "pubs"),
        # now in 'blitz'
        ("Jack Straw's Castle", "Q18358503",
         "A former pub at the top of Hampstead Heath, named after a leader of the Peasants' Revolt of 1381 who "
         "is said to have hidden here. Dickens was a visitor.",
         "en:Jack Straw's Castle, Hampstead", ("Peasants' Revolt in 1381", "Charles Dickens", "former public house"),
         "1113189", "pubs"),
        # now in 'world'
        ("E. Pellicci", "Q27087072",
         "An Italian café opened in 1900 by Tuscan immigrants on Bethnal Green Road. The building and its Art "
         "Deco interior were listed in 2005.",
         "en:E. Pellicci", ("established in 1900 by Tuscan immigrants", "Art Deco interior was Grade II listed in 2005"),
         "1391332", "coffee and tea"),
        # now in 'world'
        ("Maison Bertaux", "Q24890428",
         "A pâtisserie on Greek Street founded in 1871 by a Paris communard, the oldest in London.",
         "en:Maison Bertaux", ("founded in 1871", "communard", "oldest pâtisserie in London"),
         None, "coffee and tea"),
        # now in 'world'
        ("Liberty", "Q3237793",
         "The mock-Tudor department store on Great Marlborough Street, opened in 1924. The Art Nouveau designs "
         "it sold became known as the Stile Liberty.",
         "en:Liberty (department store)", ("mock-Tudor", "in 1924", "Stile Liberty, after the London shop"),
         "1357064", "shops"),
        # now in 'world'
        ("Harrods", "Q332474",
         "C. W. Stephens designed the present store, opened in 1905, after the first shop burned in 1881. It "
         "is the largest department store in Europe.",
         "en:Harrods", ("C. W. Stephens", "opened in 1905", "largest department store in Europe"),
         "1294346", "shops"),
    ],
    "railways": [
        # now in 'blitz'
        ("Waterloo station", "Q795691",
         "The station grew piecemeal and was hard to find your way round, so it was rebuilt and reopened in "
         "1922 with the Victory Arch for the railway's war dead. It ran London's last steam services, until "
         "1967.",
         "en:London Waterloo station", ("opening in 1922", "Victory Arch", "ended in 1967", "memorial to company staff who were killed during the war"),
         None, "termini"),
        # now in 'blitz'
        ("Victoria station", "Q985210",
         "Two stations side by side: the Brighton line's opened in 1860 and the Chatham line's two years "
         "later. Building it meant a new rail bridge over the Thames, the Grosvenor Bridge.",
         "en:London Victoria station", ("The Brighton station opened in 1860", "Grosvenor Bridge"),
         "1266689", "termini"),
        # now in 'blitz'
        ("Belsize Park station", "Q604060",
         "Opened in 1907. It is one of eight Underground stations with a deep-level air-raid shelter built "
         "beneath it in the Second World War.",
         "en:Belsize Park tube station", ("22 June 1907", "deep-level air-raid shelters"),
         "1401089", "underground"),
        # now in 'blitz'
        ("Brompton Road station", "Q926936",
         "Closed in 1934 for lack of passengers. In the Second World War it was the command centre of an "
         "anti-aircraft brigade.",
         "en:Brompton Road tube station", ("closed in 1934", "26th (London) Anti-Aircraft Brigade"),
         None, "underground"),
        # now in 'world'
        ("Lots Road Power Station", "Q1871101",
         "Built in 1902–1904 on Chelsea Creek to supply electricity to the Underground; it ran from 1 February "
         "1905.",
         "en:Lots Road Power Station", ("completed in December 1904", "1 February 1905", "London Underground"),
         None, "engineering"),
    ],
}
