"""DRAFT expansion B for seven context layers in pipeline/curated.py: housing, modern, exiles, writers, music, science,
secrets. LAYERS = {layer_id: [new entries only]}; the existing entries in curated.py are kept and not repeated here.

Same entry format as pipeline/curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or
None, group). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia
article (API prop=extracts, explaintext=1, redirects=1, User-Agent "london-by-building/0.1
(https://stop-token.com/lab/london/)"); all checks were run on 2026-10-15. Each QID was read from
Special:EntityData: it has P625, and that point falls inside one of the nine borough polygons in
data/raw/boundary.json (point-in-polygon). NHLE is the item's P1216, or None when the item has none. No QID is used
twice here, and none appears in curated.py (outside this expansion) or in drafts/*.py (blitz, expand_a,
harrypotter, streetart, world_a, world_b) as of 13:15. A second pass compared coordinates: no entry lies within 20 m
of, or shares an NHLE number with, an entry in those files (three that did were dropped, see below).
Where the building has no article of its own (NHLE-import items such as 58 Grafton Way or 87 Hackford Road), the
story cites the person's article, which names the address.

NOTE: curated.py already holds an earlier snapshot of this file (the parent merged it while work continued). Since
then: added housing Poplar Baths, Ironmonger Row Baths; modern Brockwell Lido, Ideal House, BFI Southbank, Euston
Tower, Landmark Pinnacle, Canary Wharf station; exiles 11-12 North Audley Street, The Ritz, 7 Sydney Place; music
215 King's Road, 4 Hobart Place, Fenton House, The Logs; science Highgate Literary and Scientific Institution;
secrets St John's Gate, St Mary Moorfields, Crocker's Folly, The Gatehouse (Highgate), Schomberg House, Park
Crescent West ice well, London Silver Vaults, Kingsway telephone exchange, St Ermin's Hotel, Whitehall Court.
Wording changed in: Kingswood Estate, Maiden Lane Estate, One Blackfriars, Waterloo International, Peckham Library,
Cleveland Hall, 47 Palace Court, Pear Tree House. Re-merge from this file.

COUNTS (new here / layer total with the existing entries):
  housing 41 / 55   (philanthropy 5, London County Council 3, private flats 5, workhouses 2, baths and washhouses 2,
                     post-war 24)
  modern  38 / 53   (between the wars 10, South Bank 4, Brutalism 3, towers 12, late modern 9)
  exiles  25 / 35   (exiles 12, visitors 5, radicals 8)
  writers 28 / 39   (houses 19, places 9)
  music   30 / 44   (classical 10, music hall 2, venues 13, pop 5)
  science 29 / 43   (hospitals 21, learning 6, discoveries 2)
  secrets 28 / 39   (survivals 9, hidden rooms 10, odd details 9)
New group keys: housing 'private flats', 'workhouses', 'baths and washhouses'; modern 'late modern' (high-tech,
postmodern and post-1975 buildings that are not towers). All other groups reuse the layer's existing keys.

Dropped during research:
- Taken first by other drafts (now in curated.py or drafts/): Trinity Green Almshouses, Museum of the Home
  (housing); Broadcasting House, Penguin Pool, Odeon Leicester Square, One Canada Square, 8 Canada Square, Adelaide
  House, 55 Broadway, St Olaf House, Unilever House, Freemasons' Hall, Ibex House, Smithfield Poultry Market,
  Portcullis House (modern); Smith Square Hall, St George's Hanover Square, Royal Opera House, Savoy Theatre, London
  Palladium, Lyceum, Rainbow Theatre, LSO St Luke's, St Sepulchre-without-Newgate (music); Royal College of Surgeons,
  Dulwich Picture Gallery, V&A, Marconi House, Barnard's Inn, Bar Italia (science); Bishopsgate Institute, and the
  exile churches (Dutch Church, French Protestant Church, German Lutheran and St Boniface's, Greek and Russian
  cathedrals, London Central Mosque), Polish Institute, German Gymnasium, Indian YMCA, National Liberal Club, East
  India Club, Lancaster House, Savoy Hotel (exiles); St Ethelburga's, Guildhall Art Gallery, Brompton Road station,
  Liberty, Harrods, Witanhurst, 41-42 Cloth Fair, Sutton House, Staple Inn, Young V&A, South Kentish Town and York
  Road stations, Necropolis railway office, Burlington Arcade, Methodist Central Hall, St Matthias Old Church, St
  Dunstan's Stepney, Queen's Chapel, Savoy Chapel (secrets); Carlyle Mansions, Lindsey House, Albany, Aubrey House,
  Athlone House, Burgh House, Kenwood, Athenaeum, Travellers Club, Anchor Bankside, Fitzroy Tavern, Simpson's,
  St Dunstan-in-the-West, Southwark Cathedral and most City churches (writers).
- Same footprint as an entry elsewhere: Polish Hearth Club (19 m from 49-58 Princes Gate in world-europe), Lincoln
  Memorial Tower (10 m from Christ Church Lambeth in blitz), Barbican Centre (shares NHLE 1352667 with the Barbican
  Estate in modern).
- Demolished or not standing: Blackwall Buildings, Katharine Buildings, Newington, Clerkenwell and St Luke's
  workhouses, Heygate Estate, Robin Hood Gardens, Packington Estate (rebuilt), Market Estate (rebuilt), Lyndhurst Hall
  (demolished 2006), Endell Street Military Hospital, Elizabeth Garrett Anderson Hospital (article says the Euston
  Road building was demolished), Duff House, Sardinian Embassy Chapel, Tavistock House, Lambeth Shot Tower, Dickens's
  1 Devonshire Terrace, Strangers' Home (Limehouse).
- Partly demolished or under redevelopment, left out: Aylesbury, Ledbury and Nightingale estates (the Wikidata point
  may fall on a new or doomed block).
- Coordinates outside the nine boroughs: Central Hill Estate, Cressingham Gardens, Lancaster West Estate, Pepys
  Estate, Alton Estate, Battersea Power Station, Arnos Grove, Shepherd's Bush Empire, Morden College.
- Organisation, business or street items with no building item: Peabody Trust, Guinness Trust, Rowton Houses, Royal
  College of Physicians, Royal Veterinary College, Royal College of Music, Sadler's Wells (theatre company), Ministry
  of Sound, Freedom Press, Grant and Petrie museums, Morley College, Dulwich College, AIR Studios, Sarm, Konk, Morgan,
  Basing Street Studios, Apple Corps, EMI; closed clubs whose item is the business (Marquee, Flamingo, 2i's, Bag
  O'Nails, La Gioconda, 12 Bar); Holly Lodge Estate (thin article), Brown Hart Gardens, Denmark Street, Hanover
  Terrace, Lissenden Gardens, Temple Bar (Q125555724 is the neighbourhood), Tower Subway (tunnel).
- Address matches not used: Sheridan at 14 Savile Row (articles disagree on 14 vs 17), Winifred Atwell at 18 Bourdon
  Street (item covers Nos. 10-38), Linley Sambourne at 18 Stafford Terrace (item covers 1-27), Lytton Strachey at
  69 Lancaster Gate (66-74), Walter Pater at 12 Earls Terrace (1-25), Henry Dale at Mount Vernon House (science, cut).
- Verified but not used for balance: Strand Palace Hotel, Kensington Central Library, Shepherd's Well (Frognal Way),
  Highbury Clock Tower, Julius Beer Mausoleum, Hampstead and Westminster Quaker meeting houses, Rosslyn Hill Chapel,
  St James's Spanish Place, Westminster Almshouses (one-line article).

Doubts to check before publishing:
- Institution or business items carrying the building's coordinates: most hospitals (Moorfields, Royal Free, King's
  College, Royal Brompton, Royal Marsden, Maudsley, Evelina, National Hospital, Mile End, St Pancras), Royal Academy
  of Music, LSHTM, Francis Crick Institute, Highgate Literary and Scientific Institution (no P31), Hayward Gallery,
  London Library, Reform and Savile clubs, the music clubs (Scala, Heaven, Fabric, Jazz Cafe, 606 Club, PizzaExpress
  Live, Troubadour), Housmans and Gay's the Word (bookshops), Decca, IBC and RAK studios (studio items; the
  buildings at 165 Broadhurst Gardens and 35 Portland Place stand).
- NHLE-import items that cover a whole listed group rather than the one house: 37 Chalcot Crescent (item 29-39),
  8 Montpelier Square (8-16), 7 Sydney Place (7-12), 4 Hobart Place (1-4), 3 Chalcot Square (1-11), 1-6 Upper
  Wimpole Street (Doyle at No. 2), 2-7 Chester Street (Swinburne at No. 7), 108 Cambridge Street (108-138),
  93 and 94 Cheyne Walk. The map will light up the whole listed range.
- Estates and complexes are single Wikidata points (as for the existing estates): every post-war estate here,
  Pullens, Devon Mansions, Oval Mansions, Caledonian, Regent's Park Estate.
- German Hospital, Dalston has P576 = 1987 (closure); parts of the buildings are listed and stand (converted).
- Underground or buried sites whose point will attach to the building above: Park Crescent West ice well (under
  Park Crescent, a scheduled monument), London Silver Vaults (under Chancery House), Kingsway telephone exchange
  (tunnels under Chancery Lane station; the point may land on a building unrelated to it), Pear Tree House bunker.
- Stories that rely on a "said to" tradition, worded as such: Claridge's suite 212 ("supposedly"), Crocker's Folly
  ("the story goes"), 50 Berkeley Square (ghost legend), Cleveland Street Workhouse as the model for Oliver Twist.
- Claridge's, The Ritz and Brown's are in 'exiles' for the exiled royals and visitors; 'secrets' could also claim
  them. Whitehall Court is in 'secrets' for MI6 but also housed Shaw (writers).
- Reform Club is in 'writers' for Phileas Fogg; Travellers Club (also Verne) is in expand_a.
- London Coliseum, Royal Academy of Music, Maida Vale Studios and Kings Place carry 'classical'; Hippodrome and
  Victoria Palace are the only 'music hall' additions because the Palladium and Lyceum went to other layers.
"""

LAYERS = {
    "housing": [
        ("Leopold Buildings", "Q6526918",
         "A tenement block on Columbia Road built in 1872 by Sydney Waterlow's Improved Industrial Dwellings Company, on "
         "land leased from Angela Burdett-Coutts. It was refurbished in 1997 after years of neglect.",
         "en:Leopold Buildings", ("built in 1872", "Improved Industrial Dwellings Company", "Sir Sydney Waterlow",
                                  "Angela Burdett-Coutts", "refurbished"), "1242116", "philanthropy"),
        ("Gibson Gardens", "Q5559341",
         "Built in Stoke Newington in 1880 by the Metropolitan Association for Improving the Dwellings of the Industrious "
         "Classes. A row of 'cottages' beside the blocks housed older relations of the tenants.",
         "en:Gibson Gardens", ("Metropolitan Association for Improving the Dwellings of the Industrious Classes in 1880",
                               "older relations"), None, "philanthropy"),
        ("Arlington House", "Q1821521",
         "The last and largest of the Rowton Houses, cheap hostels for single working men. It opened in Camden Town in "
         "1905 with beds for 1,200 men and is the only one still used as a hostel.",
         "en:Arlington House (London)", ("last and largest of the Rowton Houses", "1905", "1,200 tenants",
                                         "only one to remain in use as a hostel"), "1396420", "philanthropy"),
        ("Bruce House", "Q27083672",
         "The third of three lodging houses built by the London County Council after the success of the Rowton Houses, "
         "part of the clearance of the Drury Lane slums.",
         "en:Bruce House, London", ("third of three lodging-houses", "Rowton Houses", "Drury Lane"),
         "1275722", "London County Council"),
        ("Caledonian Estate", "Q16707718",
         "Five LCC blocks on the Caledonian Road next to Pentonville Prison, built in the early 1900s on the site of the "
         "Caledonian Asylum. They are named after Scottish places and writers, including Burns and Scott.",
         "en:Caledonian Estate", ("Pentonville Prison", "Caledonian Asylum", "five blocks", "Robert Burns",
                                  "Sir Walter Scott"), None, "London County Council"),
        ("Coventry Cross Estate", "Q15059595",
         "178 LCC flats in Bromley-by-Bow, opened in 1935. In the smaller blocks three flats originally shared one "
         "bathroom.",
         "en:Coventry Cross Estate", ("178 flats", "opening in 1935", "each three flats shared one"),
         None, "London County Council"),
        ("Hopton's Almshouses", "Q87739512",
         "Twenty-six homes for poor men of Southwark, built in 1746–49 under the will of Charles Hopton. They now hold 20 "
         "homes for older people from the borough.",
         "en:Hopton's Almshouses", ("1746–49", "26 homes for poor men of Southwark", "Charles Hopton",
                                    "20 single bedroom homes for older people from Southwark"), None, "philanthropy"),
        ("Caroline Gardens", "Q137671379",
         "Almshouses with a central chapel off the Old Kent Road, built from 1828 for retired publicans by the Licensed "
         "Victuallers' Benevolent Institution.",
         "en:Caroline Gardens", ("Licensed Victuallers' Benevolent Institution", "central chapel", "completed by 1833"),
         None, "philanthropy"),
        ("Pullens Buildings", "Q7259437",
         "Some of the last Victorian tenements in London, built in Walworth by the local builder James Pullen from 1886, "
         "with workshop yards behind the flats. Pullen went on building ten years longer than he had been permitted.",
         "en:Pullens buildings", ("last Victorian tenement buildings", "James Pullen", "1886", "workshop yards",
                                  "ten years more than had been permitted"), None, "private flats"),
        ("Devon Mansions", "Q5267739",
         "Five six-storey mansion blocks on Tooley Street, built from 1875 opposite the riverside warehouses known as "
         "London's Larder.",
         "en:Devon Mansions", ("five separate, six-storey mansion buildings", "In 1875", "London's Larder"),
         None, "private flats"),
        ("Oval Mansions", "Q96397884",
         "Eight 1890s tenement blocks between the Oval cricket ground and the gasholders. About 100 squatters lived "
         "here from 1983 to 2000, among them Ian Dury.",
         "en:Oval Mansions", ("built as tenement housing in the 1890s", "100 squatters", "Ian Dury", "Oval Gasholders"),
         None, "private flats"),
        ("Dolphin Square", "Q5289654",
         "1,234 private flats in Pimlico, built in 1935–37. Pevsner called it the largest self-contained block of flats "
         "in Europe; its 13 blocks are named after navigators and admirals.",
         "en:Dolphin Square", ("1935 and 1937", "1,234 flats", "largest self-contained block of flats in Europe",
                               "13 blocks"), "1455668", "private flats"),
        ("Pullman Court", "Q17552763",
         "Three modernist blocks of 218 flats on Streatham Hill, built in 1936. Frederick Gibberd was 23 when he got the "
         "commission.",
         "en:Pullman Court", ("Frederick Gibberd", "1936", "when he was 23", "218 flats"), "1064939", "private flats"),
        ("Cleveland Street Workhouse", "Q5132256",
         "A Georgian workhouse of 1775–78 that later became a hospital annexe and closed in 2005. Dickens lived a few "
         "doors away as a boy, and it may have inspired Oliver Twist.",
         "en:Cleveland Street Workhouse", ("1775 and 1778", "2005", "Charles Dickens", "22 Cleveland Street",
                                           "inspiration for Oliver Twist"), "1242917", "workhouses"),
        ("Lambeth Workhouse", "Q18393107",
         "Built in 1871–73 for 820 inmates. Charlie Chaplin was sent here at the age of seven; the master's house and "
         "chapel are now the Cinema Museum.",
         "en:Lambeth Workhouse", ("1871 to 1873", "820 inmates", "Charlie Chaplin", "seven years old", "Cinema Museum"),
         None, "workhouses"),
        ("Regent's Park Estate", "Q7308070",
         "Nearly 2,000 council homes built in the 1950s where Nash's working-class terraces east of Regent's Park were "
         "destroyed in the Blitz.",
         "en:Regent's Park Estate", ("nearly 2,000 homes", "1950s", "John Nash designed public housing", "London Blitz"),
         None, "post-war"),
        ("Fairchild House", "Q20876111",
         "When opened by Aneurin Bevan in 1950 this six-storey block was the largest council block Hackney had built. "
         "It is named after the gardener Thomas Fairchild.",
         "en:Fairchild House, Hoxton", ("1950", "Aneurin (Nye) Bevan", "largest council block", "Thomas Fairchild"),
         None, "post-war"),
        ("Kingswood Estate", "Q131782970",
         "789 homes built by the LCC in the 1950s in the grounds of Kingswood House, Dulwich. The brick modernism is an "
         "unusually late echo of the pre-war style of Willem Dudok.",
         "en:Kingswood Estate", ("789 homes", "Kingswood House", "1946", "Dudok"), None, "post-war"),
        ("St John's Estate", "Q7593588",
         "Built by Poplar Borough Council after the war on the Isle of Dogs. John Betjeman called it one of the best new "
         "estates he had seen since the war.",
         "en:St John's Estate", ("Poplar Borough Council", "one of the best new housing estates I have seen since the war"),
         None, "post-war"),
        ("Dorset Estate", "Q23304805",
         "Lubetkin's team completed this Bethnal Green estate in 1957. Its two Y-shaped blocks and the low-rise houses "
         "are named after the Tolpuddle Martyrs.",
         "en:Dorset Estate", ("Skinner, Bailey & Lubetkin", "1957", "Y-shaped", "Tolpuddle Martyrs"), None, "post-war"),
        ("Lakeview Estate", "Q6479237",
         "A Lubetkin estate opened in 1958 on a bomb site on Grove Road, overlooking the lake in Victoria Park.",
         "en:Lakeview Estate", ("Berthold Lubetkin", "opened in 1958", "Victoria Park"), None, "post-war"),
        ("Sivill House", "Q7532488",
         "A 19-storey council tower on Columbia Road, completed in 1962 by Skinner, Bailey and Lubetkin in a "
         "constructivist style.",
         "en:Sivill House", ("19-storeys", "constructivist", "completed in 1962"), "1469965", "post-war"),
        ("Cranbrook Estate", "Q5181950",
         "Lubetkin's estate around the figure-of-eight Mace Street off Roman Road. The six towers opened in 1963 and "
         "are named after Bethnal Green's twin towns, such as Puteaux and Velletri.",
         "en:Cranbrook Estate", ("figure of eight", "Mace Street", "opened in 1963", "Puteaux", "Velletri"),
         None, "post-war"),
        ("Brandon Estate", "Q42291511",
         "An LCC estate of 1958 in Walworth whose six 18-storey towers were then the tallest in London. A mural on the "
         "estate shows the Chartist meeting on Kennington Common in 1848.",
         "en:Brandon Estate", ("1958", "six 18-storey towers", "the tallest in London", "Chartists",
                               "Kennington Common"), None, "post-war"),
        ("Finsbury Estate", "Q5450922",
         "Four blocks of 451 homes in Clerkenwell designed in 1965 by Emberton, Franck & Tardrew, led by the 25-storey "
         "Michael Cliffe House.",
         "en:Finsbury Estate", ("451 residences", "Emberton, Franck & Tardrew in 1965", "Michael Cliffe House"),
         None, "post-war"),
        ("Middlesex Street Estate", "Q47012677",
         "The City of London's own estate at Aldgate, built in 1965–70 around Petticoat Square with the 23-storey "
         "Petticoat Tower.",
         "en:Middlesex Street Estate", ("between 1965 and 1970", "Corporation of London", "23-storey Petticoat Tower"),
         None, "post-war"),
        ("Samuda Estate", "Q7410675",
         "An Isle of Dogs estate begun in 1965 on the site of the Samuda Brothers' shipyard. Its 25-storey Kelson House "
         "borrows from Le Corbusier's Unité d'Habitation.",
         "en:Samuda Estate", ("Samuda Brothers", "1965", "Kelson House", "Unité d'Habitation"), None, "post-war"),
        ("Barkantine Estate", "Q59647450",
         "An LCC estate on the Isle of Dogs whose first block opened in 1968. The 1996 Docklands bombing damaged it so "
         "badly that one block was pulled down.",
         "en:Barkantine Estate", ("first block being opened in 1968", "1996 Docklands bombing", "Lantern House"),
         None, "post-war"),
        ("Chalcots Estate", "Q30627000",
         "Five tower blocks in Swiss Cottage built in 1967–68 on land owned by Eton College; four of them are 23 storeys "
         "and named after places near Eton.",
         "en:Chalcots Estate", ("Eton College", "23-storey", "1967 and 1968", "Taplow"), None, "post-war"),
        ("Ampthill Square Estate", "Q104852068",
         "A 1960s Somers Town estate of eight six-storey blocks and three 21-storey towers. Its cladding was "
         "checked after the Grenfell fire and found to be solid aluminium.",
         "en:Ampthill Square Estate", ("1960s", "three distinctive 21-storey high rises", "solid aluminium"), None, "post-war"),
        ("Brunswick Centre", "Q4979489",
         "Patrick Hodgkinson's terraced megastructure of flats over shops in Bloomsbury, built in 1967–72. It was "
         "planned as a private development and listed Grade II in 2000.",
         "en:Brunswick Centre", ("Patrick Hodgkinson", "Building started in 1967 and was completed in 1972",
                                 "private development", "2000"), "1246230", "post-war"),
        ("Perronet House", "Q7169666",
         "An 11-storey GLC tower at the Elephant and Castle, designed in 1969 by Sir Roger Walters and completed in May "
         "1970.",
         "en:Perronet House", ("11-storey", "Sir Roger Walters", "completed in May 1970"), None, "post-war"),
        ("Dunboyne Road Estate", "Q27087294",
         "Neave Brown's low-rise estate in Gospel Oak, built in 1971–77: 71 split-level houses in parallel terraces "
         "with terraces over shared gardens.",
         "en:Dunboyne Road Estate", ("Neave Brown", "between 1971 and 1977", "71 houses", "split level"),
         "1393894", "post-war"),
        ("Whittington Estate", "Q116214086",
         "Six parallel concrete terraces in Highgate New Town, built in 1972–79. Peter Tábori first drew the scheme as his "
         "final-year student project.",
         "en:Whittington Estate", ("Highgate New Town", "Peter Tábori", "1972", "1979", "final year project",
                                   "6 parallel terraces"), None, "post-war"),
        ("Southwyck House", "Q20714137",
         "The 'Barrier Block' in Brixton, a long Brutalist wall of flats built in 1972–81 to shield the estate from a "
         "planned motorway. The motorway was scrapped in 1973 but the design was kept.",
         "en:Southwyck House", ("Barrier Block", "Brutalist", "1972-1981", "scrapped in 1973"), "1413564", "post-war"),
        ("Andover Estate", "Q4754609",
         "Islington's estate in Holloway, mostly built in 1973–79 with over 1,000 homes. Three triangular towers are "
         "named after local architects.",
         "en:Andover Estate", ("1973 to 1979", "over 1000 homes", "triangular buildings", "local architects"),
         None, "post-war"),
        ("South Quay Estate", "Q7568282",
         "GLC housing beside St Katharine Docks, first occupied in 1979–81, on the site of warehouses destroyed on the "
         "first day of the Blitz.",
         "en:South Quay Estate", ("Greater London Council", "1979 and 1981", "Black Saturday", "St Katharine Docks"),
         None, "post-war"),
        ("Maiden Lane Estate", "Q16940429",
         "Terraces beside the railway at York Way, designed by Gordon Benson and Alan Forsyth and built in "
         "1979–82.",
         "en:Maiden Lane Estate", ("Gordon Benson and Alan Forsyth", "between 1979 and 1982", "York Way"),
         None, "post-war"),
        ("New Era Estate", "Q19604879",
         "A Hoxton estate whose tenants fought rent rises by a US investment fund in 2014. After a petition of 350,000 "
         "signatures it was sold to the affordable housing group Dolphin Living.",
         "en:New Era Estate", ("Westbrook Partners", "350,000 signatures", "Dolphin Living"), None, "post-war"),
        ("Poplar Baths", "Q7229378",
         "Poplar's first baths opened in 1852 under the Baths and Washhouses Act to give the poor somewhere to wash. The "
         "present building of 1933 closed in 1988 and reopened as a leisure centre in 2016.",
         "en:Poplar Baths", ("opened in 1852", "Baths and Washhouses Act 1846", "constructed in 1933", "1988",
                             "July 2016"), "1334939", "baths and washhouses"),
        ("Ironmonger Row Baths", "Q6073215",
         "A public wash house and slipper baths opened in 1931 near Old Street, followed in 1938 by a swimming pool and "
         "Turkish baths.",
         "en:Ironmonger Row Baths", ("opened in 1931", "slipper baths", "1938", "Turkish baths"), "1391805",
         "baths and washhouses"),
    ],
    "modern": [
        ("Kodak House", "Q27086660",
         "Kodak's European headquarters on Kingsway, completed in 1911 by Sir John Burnet's firm with Thomas Tait. Its "
         "plain, unornamented front was unusual among the grand offices on the new avenue.",
         "en:Kodak House, London", ("completed in 1911", "Sir John Burnet", "Thomas Tait", "un-ornamented"),
         "1379260", "between the wars"),
        ("Daily Telegraph Building", "Q60745246",
         "An Art Deco newspaper office on Fleet Street with Egyptian decoration and a large clock over the street, "
         "opened in 1928. Goldman Sachs had its European headquarters here from 1991 to 2019.",
         "en:Daily Telegraph Building", ("Egyptian decorations", "opened in 1928", "large clock", "Goldman Sachs"),
         "1358917", "between the wars"),
        ("Shell Mex House", "Q3481833",
         "Opened in 1932 behind the old front of the Hotel Cecil. The clock on its river side has the largest clock "
         "faces in the UK, 7.62 metres across.",
         "en:Shell Mex House", ("opened in 1932", "Hotel Cecil", "largest clock faces in the UK", "7.62 metres"),
         "1236752", "between the wars"),
        ("RIBA building", "Q17549828",
         "Headquarters of the Royal Institute of British Architects on Portland Place. George Grey Wornum won a "
         "competition with 284 entries, and George V opened the building in 1934.",
         "en:66 Portland Place", ("Royal Institute of British Architects", "284 entries", "George Grey Wornum",
                                  "8 November 1934"), "1227026", "between the wars"),
        ("Sun House", "Q17548595",
         "A modernist house on Frognal Way, Hampstead, built in 1935–36 by Maxwell Fry.",
         "en:Sun House, Frognal", ("1935–1936", "Maxwell Fry", "Frognal Way"), "1322140", "between the wars"),
        ("Cohen House", "Q5141321",
         "A house in Old Church Street, Chelsea, designed in 1935–36 by Erich Mendelsohn and Serge Chermayeff. Walter "
         "Gropius and Maxwell Fry built the house next door at the same time.",
         "en:Cohen House, London", ("1935–1936", "Erich Mendelsohn and Serge Chermayeff", "Walter Gropius and Maxwell Fry"),
         "1225772", "between the wars"),
        ("Simpsons of Piccadilly", "Q7521170",
         "Joseph Emberton's menswear store, opened in April 1936 as the largest in Britain, with a welded steel frame by "
         "Felix Samuely. It is now Waterstones.",
         "en:Simpsons of Piccadilly", ("Joseph Emberton", "April 1936", "largest menswear store in Britain",
                                       "Felix Samuely", "Waterstones"), "1226639", "between the wars"),
        ("Florin Court", "Q5461830",
         "Streamlined flats of 1936 on Charterhouse Square, with a curved front, roof garden and basement pool. It "
         "played Hercule Poirot's Whitehaven Mansions on television.",
         "en:Florin Court", ("Built in 1936", "curved façade", "basement swimming pool", "Whitehaven Mansions"),
         "1390634", "between the wars"),
        ("Shell Centre", "Q939044",
         "Shell's headquarters on the South Bank, built in 1957–62. Its 27-storey tower took the title of the UK's "
         "tallest building from the Royal Liver Building.",
         "en:Shell Centre", ("between 1957 and 1962", "27 storeys", "Royal Liver Building"), None, "South Bank"),
        ("Queen Elizabeth Hall", "Q1622428",
         "A Brutalist concert hall opened in March 1967 with a concert conducted by Benjamin Britten. Skateboarders "
         "have used the undercroft beneath its foyer since 1973.",
         "en:Queen Elizabeth Hall", ("opened in March 1967", "Benjamin Britten", "undercroft",
                                     "first used by skateboarders in 1973"), None, "South Bank"),
        ("Hayward Gallery", "Q779736",
         "An art gallery of exposed concrete with outdoor sculpture courts on its upper level, opened on 9 July 1968.",
         "en:Hayward Gallery", ("opened on 9 July 1968", "exposed concrete", "Brutalist", "outdoor sculpture courts"),
         None, "South Bank"),
        ("Portland House", "Q3755685",
         "A 29-storey office tower of 1959–63 on the site of Watney's brewery near Victoria. Pevsner saw the influence of "
         "Gio Ponti's Pirelli Tower in Milan.",
         "en:Portland House", ("29 floors", "Watney's Brewery", "1959 to 1963", "Pirelli Tower"), None, "towers"),
        ("Millbank Tower", "Q2915930",
         "Built in 1963 as Vickers House beside the Thames. Labour ran its 1997 general election campaign from offices at "
         "its base.",
         "en:Millbank Tower", ("constructed in 1963", "Vickers House", "1997 General Election"), "1242617", "towers"),
        ("Metro Central Heights", "Q6824538",
         "Ernő Goldfinger's office complex at the Elephant and Castle, built in the early 1960s for the Ministry of "
         "Health as Alexander Fleming House. It was saved from demolition and turned into flats in 1997.",
         "en:Metro Central Heights", ("Ernő Goldfinger", "Alexander Fleming House", "Ministry of Health",
                                      "saved from demolition", "1997"), "1405570", "Brutalism"),
        ("Swiss Cottage Library", "Q7658861",
         "Sir Basil Spence's library on Avenue Road, built in 1963–64, the surviving part of a larger civic centre for "
         "Hampstead.",
         "en:Swiss Cottage Library", ("Sir Basil Spence", "between 1963 and 1964", "Civic Centre"),
         "1272259", "Brutalism"),
        ("Space House", "Q27087667",
         "A cylindrical office block off Kingsway built in 1964–68 for Harry Hyams, the developer of Centre Point. Like "
         "Centre Point, it was kept empty for years after completion.",
         "en:Space House", ("Harry Hyams", "between 1964 and 1968", "Centre Point", "kept empty"),
         "1421847", "Brutalism"),
        ("Citypoint", "Q2920650",
         "Built in 1967 as Britannic House, BP's 35-storey headquarters. It was the first building in the City to rise "
         "higher than St Paul's Cathedral.",
         "en:Citypoint", ("built in 1967", "Britannic House", "35-storey", "exceed the height of St Paul's Cathedral"),
         None, "towers"),
        ("Tower 42", "Q1331574",
         "Richard Seifert's NatWest Tower, opened in 1980 as the tallest building in the UK. Seen from above it has the "
         "shape of the NatWest logo; the 1993 Bishopsgate bomb badly damaged it.",
         "en:Tower 42", ("R Seifert & Partners", "opened in 1980", "NatWest logo", "1993 Bishopsgate bombing"),
         None, "towers"),
        ("Strata SE1", "Q2284719",
         "A 43-storey residential tower at the Elephant and Castle with three wind turbines built into its top. They "
         "have rarely run, partly because residents complained of noise.",
         "en:Strata SE1", ("43-storey", "wind turbines", "rarely been used", "noise and vibration"), None, "towers"),
        ("St George Wharf Tower", "Q1469829",
         "A 50-storey residential tower at Vauxhall. In January 2013, before it was finished, a helicopter hit a crane "
         "on the building and crashed, killing two people.",
         "en:St George Wharf Tower", ("50 storeys", "16 January 2013", "helicopter", "crane", "two people were killed"),
         None, "towers"),
        ("Leadenhall Building", "Q2742547",
         "The 'Cheesegrater' by Rogers Stirk Harbour, opened in 2014. Its sloping face keeps it out of the protected "
         "view of St Paul's from Fleet Street.",
         "en:122 Leadenhall Street", ("Cheesegrater", "July 2014", "Rogers Stirk Harbour", "sightline of St Paul's Cathedral"),
         None, "towers"),
        ("Heron Tower", "Q1613853",
         "110 Bishopsgate, 230 metres including its mast. The reception holds a 70,000-litre aquarium with about 1,200 "
         "fish, the largest privately owned one in the UK.",
         "en:Heron Tower", ("230 metres", "70,000-litre", "1,200 fish", "largest privately owned example in the United Kingdom"),
         None, "towers"),
        ("22 Bishopsgate", "Q18602",
         "A 62-storey tower completed in 2020 on the site of the Pinnacle, whose construction stopped in 2012 "
         "with only seven storeys of concrete core built. The core was removed in 2015.",
         "en:22 Bishopsgate", ("Completed in 2020", "62 storeys", "The Pinnacle", "first seven storeys", "December 2015"), None, "towers"),
        ("One Blackfriars", "Q2893700",
         "A 50-storey tower known as the Vase or the Boomerang. The architect Ian Simpson based its shape on a 1952 "
         "glass vase by Timo Sarpaneva.",
         "en:One Blackfriars", ("50-storey", "The Vase", "Timo Sarpaneva", "1952"), None, "towers"),
        ("Hopkins House", "Q23038187",
         "Michael and Patty Hopkins built this two-storey glass and steel box at 49a Downshire Hill in 1976 as their "
         "home and studio, an early landmark of High Tech.",
         "en:Hopkins House, Hampstead", ("49a Downshire Hill", "Michael and Patty Hopkins", "1976",
                                         "two-storey glass and steel box", "High Tech"), "1444039", "late modern"),
        ("Waterloo International", "Q795678",
         "Grimshaw Architects' Eurostar terminal, used from 1994 to 2007. Its roof rests on curved, tapering steel trusses "
         "the engineer Anthony Hunt called 'banana shaped'.",
         "en:Waterloo International railway station", ("14 November 1994", "13 November 2007", "Grimshaw",
                                                       "banana shaped"), None, "late modern"),
        ("No 1 Poultry", "Q1994490",
         "James Stirling's striped postmodern block at Bank, completed in 1997 after his death. When listed Grade II* in "
         "2016 it was the youngest building in England with that grade.",
         "en:No 1 Poultry", ("James Stirling", "completed in 1997", "Grade II*", "youngest building in England"),
         "1428881", "late modern"),
        ("Southwark station", "Q38909",
         "Richard MacCormac's Jubilee line station of 1999. A curved wall of 660 pieces of blue glass by Alexander "
         "Beleschenko lines the concourse.",
         "en:Southwark tube station", ("20 November 1999", "Richard MacCormac", "660 specially cut pieces of blue glass",
                                       "Alexander Beleschenko"), "1491631", "late modern"),
        ("Tate Modern", "Q193375",
         "Giles Gilbert Scott's Bankside Power Station, built in 1947–63, turned into a gallery by Herzog & de Meuron "
         "and opened in 2000.",
         "en:Tate Modern", ("Bankside Power Station", "Sir Giles Gilbert Scott", "between 1947 and 1963",
                            "Herzog & de Meuron", "January 2000"), None, "late modern"),
        ("Peckham Library", "Q3511923",
         "Alsop and Störmer's library raised on thin, angled steel legs and clad in pre-patinated copper. It won the "
         "Stirling Prize in 2000.",
         "en:Peckham Library", ("Alsop and Störmer", "Stirling Prize for Architecture in 2000", "pre-patinated copper",
                                "thin steel pillars"), None, "late modern"),
        ("88 Wood Street", "Q4645063",
         "A Richard Rogers office block of 1993–2001 with glass lifts on the outside, red and blue air funnels and "
         "yellow stairs.",
         "en:88 Wood Street", ("between 1993 and 2001", "glass lifts are on the outside", "red and blue air funnels",
                               "bright yellow stairs"), None, "late modern"),
        ("Bloomberg London", "Q46996829",
         "Foster and Partners' European headquarters for Bloomberg, opened in 2017. The remains of the Roman temple of "
         "Mithras were moved back close to their original site; it won the 2018 Stirling Prize.",
         "en:Bloomberg London", ("opened in 2017", "Foster and Partners", "Mithraeum", "Stirling Prize"),
         None, "late modern"),
        ("Brockwell Lido", "Q4972912",
         "An LCC open-air pool in the Moderne style, opened in July 1937. Lambeth closed it in 1990; a local campaign "
         "reopened it in 1994.",
         "en:Brockwell Lido", ("Moderne style", "London County Council", "opened in July 1937", "closed in 1990",
                               "re-opened in 1994"), "1390519", "between the wars"),
        ("Ideal House", "Q5987952",
         "A black granite office block of 1928–29 by Raymond Hood, a smaller version of his American Radiator Building "
         "in New York, built for the National Radiator Company.",
         "en:Ideal House, London", ("Raymond Hood", "American Radiator Building", "black granite", "1928–9"),
         "1357168", "between the wars"),
        ("BFI Southbank", "Q683076",
         "The National Film Theatre moved under the approach to Waterloo Bridge in 1957 and opened with the first "
         "London Film Festival.",
         "en:BFI Southbank", ("National Film Theatre", "1957", "Waterloo Bridge", "first BFI London Film Festival"),
         None, "South Bank"),
        ("Euston Tower", "Q2389056",
         "A 36-storey International Style office tower on Euston Road, completed in 1970. Capital Radio was an early "
         "tenant.",
         "en:Euston Tower", ("completed in 1970", "36-storeys", "International style", "Capital Radio"), None, "towers"),
        ("Landmark Pinnacle", "Q16258428",
         "A 75-storey tower on the Isle of Dogs, the tallest residential building in the UK.",
         "en:Landmark Pinnacle", ("75-storey", "tallest residential tower in the United Kingdom"), None, "towers"),
        ("Canary Wharf station", "Q1032842",
         "Norman Foster's Jubilee line station, opened in 1999. Its concourse is so large that it has been compared to a "
         "cathedral and used for a wedding.",
         "en:Canary Wharf tube station", ("17 September 1999", "Norman Foster", "compared to a cathedral", "wedding"),
         None, "late modern"),
    ],
    "exiles": [
        ("58 Grafton Way", "Q17542363",
         "The Venezuelan revolutionary Francisco de Miranda lived here from 1803. In 1810 a delegation including Simón "
         "Bolívar and Andrés Bello persuaded him to return home; the house is now Venezuela's consulate.",
         "en:Francisco de Miranda", ("27 Grafton Street (now 58 Grafton Way)", "moving to Grafton Way in 1803",
                                     "Simón Bolívar and Andrés Bello", "Consulate of Venezuela"), "1113071", "exiles"),
        ("37 Chalcot Crescent", "Q27081888",
         "José Rizal, the writer later honoured as the national hero of the Philippines, lived in this terrace while in "
         "London researching Antonio de Morga's history of the islands.",
         "en:José Rizal", ("37 Chalcot Crescent", "Antonio de Morga", "Blue Plaque"), "1244109", "exiles"),
        ("44 Grove End Road", "Q26639679",
         "The Dutch painter Lawrence Alma-Tadema left the Continent when the Franco-Prussian War broke out in 1870 and "
         "settled in London. This was his home from 1886 until his death in 1912.",
         "en:Lawrence Alma-Tadema", ("Franco-Prussian War", "settled in London, England in 1870", "44 Grove End Road",
                                     "from 1886 until his death in 1912"), "1357085", "exiles"),
        ("Cleveland Hall", "Q15210921",
         "A hall in Cleveland Street that was the London centre of the secularist movement from 1861 to 1878. In those decades "
         "French communards, German socialists and Italian anarchists who had fled to London met here.",
         "en:Cleveland Hall, London", ("between 1861 and 1878", "French communards", "German socialists",
                                       "Italian anarchists"), None, "exiles"),
        ("10 Palace Green", "Q26318935",
         "The Norwegian legation in Kensington, where King Haakon VII lived during the Second World War. It became the "
         "seat of the Norwegian government in exile.",
         "en:Haakon VII", ("Norwegian Legation at 10 Palace Green", "seat of the Norwegian government in exile"),
         "1065911", "exiles"),
        ("Stratton House", "Q27083210",
         "An office block on Piccadilly built in 1926–28 by William Curtis Green. The Dutch government in exile worked "
         "from it during the Second World War.",
         "en:Stratton House, London", ("between 1926 and 1928", "William Curtis Green", "Dutch government-in-exile"),
         "1265713", "exiles"),
        ("Claridge's", "Q2748565",
         "The Yugoslav government in exile was based here in the Second World War. Suite 212 was supposedly ceded to "
         "Yugoslavia for one day in July 1945 so that the heir to the throne could be born on Yugoslav soil.",
         "en:Claridge's", ("Kingdom of Yugoslavia's government in exile", "Peter II of Yugoslavia", "suite 212",
                           "17 July 1945"), "1219905", "exiles"),
        ("2 Wildwood Terrace", "Q124152583",
         "The architectural historian Nikolaus Pevsner, born in Leipzig to a Russian-Jewish family, settled here after "
         "leaving Germany. He lived here until his death in 1983, and wrote The Buildings of England.",
         "en:Nikolaus Pevsner", ("2, Wildwood Terrace", "born in Leipzig", "Russian-Jewish family", "August 1983",
                                 "The Buildings of England"), None, "exiles"),
        ("8 Montpelier Square", "Q26517615",
         "Arthur Koestler, the Hungarian-born author of Darkness at Noon, came to Britain in 1940. He and his wife "
         "Cynthia died together in their home here in 1983.",
         "en:Arthur Koestler", ("Darkness at Noon", "moved to Britain in 1940", "8 Montpelier Square", "1 March 1983"),
         "1223344", "exiles"),
        ("138 Kensington Church Street", "Q27081699",
         "Lucian Freud, whose family left Berlin for London in 1933 to escape Nazism, had his home and studio in this "
         "house of 1736–37 from the 1970s until his death.",
         "en:Lucian Freud", ("in 1933 to escape the rise of Nazism", "138 Kensington Church Street", "1736–37"),
         "1239852", "exiles"),
        ("87 Hackford Road", "Q26355208",
         "Vincent van Gogh lodged here in 1873 while working at Goupil's London branch. He fell for his landlady's "
         "daughter, Eugénie Loyer, who turned him down.",
         "en:Vincent van Gogh", ("87 Hackford Road, Stockwell", "Goupil's London branch", "Eugénie Loyer"),
         "1080441", "visitors"),
        ("18 Melbury Road", "Q122370616",
         "Cetshwayo, King of the Zulus, stayed here in 1882. He and the painter Holman Hunt both have English Heritage "
         "blue plaques on the house.",
         "en:18 Melbury Road", ("King of the Zulus, stayed here in 1882", "Holman Hunt", "blue plaques"),
         None, "visitors"),
        ("Brown's Hotel", "Q4975949",
         "London's oldest luxury hotel. Rudyard Kipling spent his wedding night here in 1892, and Franklin Roosevelt and "
         "Gandhi were among its guests.",
         "en:Brown's Hotel, London", ("oldest luxury hotel", "Rudyard Kipling", "18 January 1892", "Franklin Roosevelt",
                                      "Mahatma Gandhi"), None, "visitors"),
        ("14 Prince's Gate", "Q4549947",
         "A house of 1849 bought by the American banker Junius Morgan and inherited by J. P. Morgan. From 1921 into the "
         "1950s it was the residence of eight American ambassadors.",
         "en:14 Prince's Gate, London", ("Built in 1849", "Junius Spencer Morgan", "John Pierpont Morgan",
                                         "eight American ambassadors"), None, "visitors"),
        ("Newington Green Unitarian Church", "Q7018260",
         "Founded in 1708, London's oldest Nonconformist place of worship still in use. Its minister Richard Price "
         "defended the French Revolution, and Mary Wollstonecraft drew on his sermons.",
         "en:Newington Green Unitarian Church", ("founded in 1708", "oldest Nonconformist place of worship still in use",
                                                 "Richard Price", "Mary Wollstonecraft"), "1235210", "radicals"),
        ("Hampstead Town Hall", "Q27086263",
         "An Italianate town hall opened in 1878. Emmeline Pankhurst spoke here in 1913, Oswald Mosley in 1938 and the "
         "anti-racism campaigner David Pitt in 1959.",
         "en:Hampstead Town Hall", ("June 1878", "Emmeline Pankhurst", "Oswald Mosley", "David Pitt"),
         "1378818", "radicals"),
        ("Mary Ward House", "Q96392172",
         "An Arts and Crafts settlement house of 1896–98 in Tavistock Place, named after the novelist Mary Ward and paid "
         "for mostly by Passmore Edwards.",
         "en:Mary Ward House", ("Built between 1896 and 1898", "Tavistock Place", "Mary Augusta Ward", "Passmore Edwards",
                                "Arts and Crafts"), "1378962", "radicals"),
        ("Transport House", "Q2449627",
         "Opened in May 1928 on Smith Square as the headquarters of the Transport and General Workers' Union, the Labour "
         "Party and the TUC. Labour moved out in 1980.",
         "en:Transport House", ("May 1928", "Smith Square", "Transport and General Workers' Union",
                                "The Labour Party moved out in 1980"), None, "radicals"),
        ("Friends House", "Q19461855",
         "The central offices of British Quakers on Euston Road since 1926, when they moved from Devonshire House in "
         "Bishopsgate. Britain Yearly Meeting gathers here.",
         "en:Friends House", ("173 Euston Road", "British Quakers", "Prior to 1926", "Britain Yearly Meeting"),
         "1078321", "radicals"),
        ("Congress House", "Q5160797",
         "The headquarters of the Trades Union Congress, opened on 27 March 1958. Jacob Epstein carved its courtyard "
         "memorial to trade unionists killed in the two world wars.",
         "en:Congress House", ("Trades Union Congress", "27 March 1958", "Jacob Epstein", "dead trade unionists"),
         "1113223", "radicals"),
        ("Housmans", "Q99472923",
         "A bookshop founded by pacifists in 1945 and on the Caledonian Road since 1959, sharing its building with Peace "
         "News. The Gay Liberation Front and CND have worked from its address.",
         "en:Housmans", ("founded by a collective of pacifists in 1945", "since 1959", "Peace News",
                         "Gay Liberation Front", "Campaign for Nuclear Disarmament"), None, "radicals"),
        ("Gay's the Word", "Q5528519",
         "The oldest LGBT bookshop in the UK, founded in 1979. Lesbians and Gays Support the Miners met here during the "
         "1984–85 strike.",
         "en:Gay's the Word (bookshop)", ("oldest LGBT bookshop in the United Kingdom", "1979",
                                          "Lesbians and Gays Support the Miners"), None, "radicals"),
        ("11–12 North Audley Street", "Q17549766",
         "Two Mayfair houses of 1726–30, the only original survivors on the street. Their Georgian interiors were made "
         "for Jean Louis Ligonier, a Huguenot refugee who became Commander-in-Chief of the Army.",
         "en:11–12 North Audley Street", ("between 1726 and 1730", "only original surviving house on the street",
                                          "Jean Louis Ligonier, a Huguenot refugee", "Commander-in-Chief"),
         "1225300", "exiles"),
        ("The Ritz", "Q1481002",
         "In summer 1940 King Zog I of Albania and his family moved into the hotel and took a floor of their own. The "
         "royal gold was kept in the hotel storeroom before going to the Bank of England.",
         "en:The Ritz Hotel, London", ("summer of 1940", "King Zog I", "royal gold", "Bank of England"),
         "1226499", "exiles"),
        ("7 Sydney Place", "Q27081257",
         "Béla Bartók stayed at No. 7 when he came to perform in London. An English Heritage plaque was unveiled in "
         "1997.",
         "en:Béla Bartók", ("7 Sydney Place", "where he stayed when performing in London", "unveiled in 1997"),
         "1226870", "visitors"),
    ],
    "writers": [
        ("Canonbury Tower", "Q17552171",
         "The Tudor tower of the Canonbury manor house, built for the canons of St Bartholomew's in 1509–32 and the "
         "oldest building in Islington. Francis Bacon leased the house from 1616; Oliver Goldsmith and Washington Irving "
         "later lived here.",
         "en:Canonbury House and Canonbury Tower", ("between 1509 and 1532", "oldest building in Islington",
                                                    "From 1616 to 1625", "Oliver Goldsmith", "Washington Irving"),
         "1280424", "houses"),
        ("9 Gerrard Street", "Q27083893",
         "Joshua Reynolds brought together The Club, founded in 1764, whose first members included Edmund Burke. It met "
         "on the first floor of the Turk's Head at 9 Gerrard Street, now marked by a plaque.",
         "en:Joshua Reynolds", ("The Club", "founded in 1764", "Original members included Burke", "Turks Head at 9 Gerrard Street"), "1289415", "places"),
        ("1 and 2 Robert Street", "Q17549910",
         "The poet Thomas Hood and his wife Jane settled at 2 Robert Street, Adelphi, after their marriage in 1824.",
         "en:Thomas Hood", ("5 May 1824", "2 Robert Street, Adelphi"), "1235244", "houses"),
        ("11 Bolton Street", "Q26319373",
         "The novelist and diarist Fanny Burney lived at this Mayfair house; a Royal Society of Arts plaque records her "
         "stay.",
         "en:Fanny Burney", ("11 Bolton Street, Mayfair", "Royal Society of Arts"), "1066426", "houses"),
        ("3 The Grove", "Q17548805",
         "A house in Highgate where Samuel Taylor Coleridge lived from 1823 with his doctor James Gillman, who treated "
         "his opium addiction. J. B. Priestley later lived here.",
         "en:3 The Grove", ("Samuel Taylor Coleridge", "James Gillman", "opium", "In 1823", "Priestley"),
         "1378978", "houses"),
        ("Hazlitt's", "Q17549587",
         "The essayist William Hazlitt died in this house at 6 Frith Street in 1830. It is now a hotel named after "
         "him, with his blue plaque by the door.",
         "en:Hazlitt's", ("6 Frith Street", "William Hazlitt who died in the house in 1830", "blue plaque"),
         "1211966", "houses"),
        ("93 and 94 Cheyne Walk", "Q27085343",
         "Elizabeth Gaskell was born on 29 September 1810 at what was then Lindsey Row, now 93 Cheyne Walk.",
         "en:Elizabeth Gaskell", ("29 September 1810", "Lindsey Row, Chelsea, London, now 93 Cheyne Walk"),
         "1358128", "houses"),
        ("2–7 Chester Street", "Q27083979",
         "The poet Algernon Charles Swinburne was born at 7 Chester Street, off Grosvenor Place, on 5 April 1837.",
         "en:Algernon Charles Swinburne", ("born at 7 Chester Street", "5 April 1837"), "1291544", "houses"),
        ("Thackeray's house", "Q17552658",
         "William Makepeace Thackeray had this red-brick house built at 2 Palace Green in 1860–62. It is now the Embassy "
         "of Israel.",
         "en:2 Palace Green", ("1860–62", "William Makepeace Thackeray", "red brick", "Embassy of Israel"),
         "1357462", "houses"),
        ("19 Curzon Street", "Q26319826",
         "Benjamin Disraeli, prime minister and novelist, died at his home here in April 1881; his last finished novel, "
         "Endymion, had come out shortly before.",
         "en:Benjamin Disraeli", ("19 Curzon Street", "19 April", "Endymion"), "1066944", "houses"),
        ("4 Cheyne Walk", "Q15978845",
         "George Eliot moved into this Chelsea house on 3 December 1880 and died here on 22 December. The painter "
         "Daniel Maclise had lived here earlier.",
         "en:4 Cheyne Walk", ("George Eliot", "3 December", "22 December 1880", "Daniel Maclise"), "1080721", "houses"),
        ("Abernethy House", "Q26407050",
         "Robert Louis Stevenson first stayed in this Hampstead house in 1873 and wrote that Hampstead was the most "
         "delightful place for air and scenery near London.",
         "en:Abernethy House", ("In 1873 the writer Robert Louis Stevenson stayed here",
                                "Hampstead is the most delightful place for air and scenery near London"),
         "1113153", "houses"),
        ("1–6 Upper Wimpole Street", "Q27083628",
         "Arthur Conan Doyle opened a consulting room at No. 2. By his own account he had no patients, and while waiting "
         "for them he went back to writing fiction.",
         "en:Arthur Conan Doyle", ("2 Upper Wimpole Street", "He had no patients", "returned to writing fiction"),
         "1274702", "houses"),
        ("47 Palace Court", "Q18149067",
         "The poet and essayist Alice Meynell and her husband lived in this Bayswater house; an LCC blue plaque "
         "marks it.",
         "en:47 Palace Court", ("Alice Meynell", "blue plaque"), "1065878", "houses"),
        ("Cannon Hall", "Q17542646",
         "The actor Gerald du Maurier bought this Hampstead house in 1916. His daughter Daphne du Maurier grew up here. "
         "One of Hampstead's lock-ups was built into the garden wall.",
         "en:Cannon Hall, Hampstead", ("purchased the house in 1916", "Daphne du Maurier", "lock-ups"),
         "1244093", "houses"),
        ("Chiltern Court", "Q111724841",
         "Flats built in 1927–29 over Baker Street station. H. G. Wells lived here from 1930 to 1936 and held a weekly "
         "literary salon; Arnold Bennett died here in 1931.",
         "en:Chiltern Court", ("between 1927 and 1929", "Baker Street tube station", "1930 to 1936", "literary salon",
                               "Arnold Bennett, who died at the Court in 1931"), None, "houses"),
        ("3 Chalcot Square", "Q27082587",
         "Sylvia Plath and Ted Hughes lived in a flat at No. 3 from 1960 to 1961; an English Heritage plaque records "
         "Plath's stay.",
         "en:Sylvia Plath", ("3 Chalcot Square", "English Heritage plaque", "from 1960 to 1961"), "1258094", "houses"),
        ("Kensington Court Gardens", "Q6391439",
         "T. S. Eliot moved to a flat at No. 3 in 1957 after his secret marriage to Valerie, his secretary at Faber "
         "and Faber, and died there on 4 January 1965.",
         "en:Kensington Court Gardens", ("No.3 Kensington Court Gardens in 1957", "Faber and Faber", "4 January 1965"),
         None, "houses"),
        ("72 Cadogan Square", "Q15978852",
         "The American war correspondent and writer Martha Gellhorn had a flat here for 28 years.",
         "en:72 Cadogan Square", ("Martha Gellhorn", "28 years"), "1080739", "houses"),
        ("108 Cambridge Street", "Q27084783",
         "The novelist Barbara Pym lived here from 1945 to 1949. An English Heritage blue plaque was put up on 1 May "
         "2025.",
         "en:Barbara Pym", ("108 Cambridge Street, Pimlico", "between 1945 and 1949", "1 May 2025"), "1357243", "houses"),
        ("Newman Arms", "Q18748737",
         "A Fitzrovia pub that George Orwell used as the model for the proles' pub in Nineteen Eighty-Four; it also "
         "appears in Keep the Aspidistra Flying.",
         "en:Newman Arms", ("George Orwell", "Nineteen Eighty-Four", "Keep the Aspidistra Flying"), None, "places"),
        ("Heywood Hill", "Q23891191",
         "A Mayfair bookshop opened in 1936. During the last years of the Second World War Nancy Mitford helped run it.",
         "en:Heywood Hill", ("3 August 1936", "Nancy Mitford", "Second World War"), "1221069", "places"),
        ("London Library", "Q269192",
         "A subscription library founded in 1841 on Thomas Carlyle's initiative, who was dissatisfied with the British "
         "Museum Library. It has been at 14 St James's Square since 1845.",
         "en:London Library", ("established in 1841", "Thomas Carlyle", "British Museum Library",
                               "14 St James's Square", "since 1845"), "1235825", "places"),
        ("Reform Club", "Q962177",
         "Sir Charles Barry's clubhouse on Pall Mall. In Jules Verne's Around the World in Eighty Days, Phileas Fogg sets "
         "out from here; Thackeray and Arnold Bennett were members.",
         "en:Reform Club", ("Sir Charles Barry", "Around the World in Eighty Days", "Phileas Fogg",
                            "William Makepeace Thackeray and Arnold Bennett"), "1225841", "places"),
        ("Garrick Club", "Q125481190",
         "Frederick Marrable's Italian palazzo on Garrick Street, the Garrick Club's home since 1860. It is listed "
         "Grade II*.",
         "en:Garrick Club Clubhouse", ("Garrick Street", "1860", "Frederick Marrable", "Italian palazzo"), "1066808", "places"),
        ("Savile Club", "Q7428222",
         "A club strong in literature and the arts. Robert Louis Stevenson, a member from 1874, said in its billiard room "
         "that playing billiards well was the sign of an ill-spent youth.",
         "en:Savile Club", ("69 Brook Street", "Robert Louis Stevenson, a member from 1874", "ill-spent youth"),
         "1219938", "places"),
        ("Crown and Greyhound", "Q17361842",
         "A Dulwich Village pub that replaced the Greyhound, where the Dulwich Club met from 1772. Dickens and Thackeray "
         "were among the club's guests.",
         "en:The Crown and Greyhound", ("Dulwich Club", "1772", "Charles Dickens", "William Makepeace Thackeray"),
         "1385506", "places"),
        ("Dr Williams's Library", "Q5304565",
         "A library of Dissenters' books founded in 1729. It moved to University Hall in Gordon Square in 1890.",
         "en:Dr Williams's Library", ("opened in 1729", "English Dissenters", "Gordon Square, in 1890"), None, "places"),
    ],
    "music": [
        ("20 Frith Street", "Q4630554",
         "Mozart, aged eight, lodged in an earlier house on this site from September 1764 during his family's tour of "
         "Europe. The present building dates from 1858.",
         "en:20 Frith Street", ("Wolfgang Amadeus Mozart", "aged eight from September 1764", "built in 1858"),
         None, "classical"),
        ("London Coliseum", "Q1868965",
         "Frank Matcham's variety theatre for Oswald Stoll, opened on 24 December 1904. With 2,359 seats it is the "
         "largest theatre in London and the home of English National Opera.",
         "en:London Coliseum", ("Frank Matcham", "Oswald Stoll", "24 December 1904", "2,359 seats",
                                "English National Opera"), "1236022", "classical"),
        ("Cadogan Hall", "Q2261872",
         "A Byzantine Revival church of Christ, Scientist, completed in 1907, now a 953-seat concert hall and home of "
         "the Royal Philharmonic Orchestra.",
         "en:Cadogan Hall", ("Church of Christ, Scientist", "completed in 1907", "953-seat", "Royal Philharmonic Orchestra"),
         "1226700", "classical"),
        ("Royal Academy of Music", "Q1144673",
         "Founded in 1822, the academy moved in 1911 into Sir Ernest George's building on Marylebone Road, with the "
         "450-seat Duke's Hall.",
         "en:Royal Academy of Music", ("founded in 1822", "In 1911", "Sir Ernest George", "450-seat Duke's Hall"),
         "1239816", "classical"),
        ("Maida Vale Studios", "Q127603",
         "Built in 1909–10 as a roller-skating rink and rebuilt for the BBC in 1933–34. The Beatles recorded radio sessions "
         "here in 1963, and John Peel's sessions were recorded here.",
         "en:Maida Vale Studios", ("1909–1910", "roller skating rink", "1933–1934", "The Beatles used studio MV5",
                                   "John Peel"), "1463441", "classical"),
        ("Henry Wood Hall", "Q26665755",
         "Holy Trinity Church of 1823–24 in Trinity Church Square, chosen by the London Philharmonic and London Symphony "
         "orchestras as a rehearsal studio and opened in 1975.",
         "en:Henry Wood Hall, London", ("1823–24", "Holy Trinity Church", "rehearsal studio", "opened in 1975"),
         "1385999", "classical"),
        ("Kings Place", "Q6413000",
         "Offices at King's Cross completed in 2008, with the first public concert hall built in central London since "
         "the Barbican's in 1982. The Guardian has its offices here.",
         "en:Kings Place", ("completed in summer 2008", "first public concert hall", "1982", "The Guardian"),
         None, "classical"),
        ("London Hippodrome", "Q1150147",
         "Frank Matcham's hippodrome for circus and variety, opened in 1900. Its arena could sink into a 100,000-gallon "
         "water tank for aquatic shows.",
         "en:Hippodrome, London", ("opened in 1900", "Frank Matcham", "circus and variety", "100,000 gallon water tank"),
         "1066287", "music hall"),
        ("Victoria Palace Theatre", "Q7926899",
         "The last London theatre designed by Frank Matcham, opened in 1911 with a gilded statue of Anna Pavlova above "
         "the cupola. The Crazy Gang revues ran here from 1947 to 1962.",
         "en:Victoria Palace Theatre", ("last London theatre he designed", "Anna Pavlova", "The Crazy Gang", "1947 through 1962"),
         "1238140", "music hall"),
        ("Islington Assembly Hall", "Q20711847",
         "An Art Deco hall at Islington Town Hall, opened in March 1930. It closed in the mid-1980s, was used as a store "
         "for 30 years, and reopened as a music venue in 2010.",
         "en:Islington Assembly Hall", ("opened in March 1930", "closed in the mid-1980s", "reopened in 2010"),
         None, "venues"),
        ("O2 Forum Kentish Town", "Q7734912",
         "An Art Deco cinema opened in December 1934. It became a music venue in 1985 as the Town & Country Club.",
         "en:O2 Forum Kentish Town", ("17th December 1934", "art deco cinema", "Town & Country Club"),
         "1379018", "venues"),
        ("Scala", "Q7429657",
         "A cinema begun before the First World War and opened in 1920. In 1972 it hosted the only UK concert by Iggy & "
         "the Stooges, then recording Raw Power in London.",
         "en:Scala (club)", ("opening in 1920", "First World War", "Iggy & The Stooges", "Raw Power"), None, "venues"),
        ("Troubadour", "Q7770338",
         "A coffee house and club on Old Brompton Road, opened in 1954. Bob Dylan played here at Christmas 1962 as "
         "'Blind Boy Grunt'.",
         "en:Troubadour (London nightclub)", ("265 Old Brompton Road", "Established in 1954", "Blind Boy Grunt"),
         None, "venues"),
        ("606 Club", "Q4641642",
         "A basement jazz club at 90 Lots Road, opposite the old Lots Road Power Station, with music seven nights a week.",
         "en:606 Club", ("90 Lots Road", "Lots Road Power Station", "seven nights a week"), None, "venues"),
        ("PizzaExpress Live Soho", "Q7199945",
         "A jazz club in the basement of a Dean Street pizza restaurant, opened by Peter Boizot in 1969. Amy Winehouse "
         "and Jamie Cullum played here.",
         "en:PizzaExpress Live Soho", ("Peter Boizot in 1969", "Dean Street", "Amy Winehouse", "Jamie Cullum"),
         None, "venues"),
        ("Hope and Anchor", "Q15225054",
         "An Upper Street pub of 1880 that became a pub-rock and punk venue in the 1970s. The Stranglers recorded Live at "
         "the Hope and Anchor here in 1977.",
         "en:Hope and Anchor, Islington", ("1880", "pub rock", "punk rock", "Live at the Hope and Anchor"),
         "1195774", "venues"),
        ("Dublin Castle", "Q19587199",
         "A Camden Town pub where Madness built its live following in the late 1970s. Amy Winehouse performed here and "
         "sometimes served behind the bar.",
         "en:Dublin Castle, Camden", ("Madness", "late 1970s", "Amy Winehouse", "helped to serve drinks"),
         None, "venues"),
        ("Bull & Gate", "Q16985641",
         "A Kentish Town pub of 1871 where the Pogues, Blur, Suede and Coldplay played early in their careers.",
         "en:Bull & Gate", ("built in 1871", "The Pogues", "Coldplay", "Blur", "Suede"), "1391501", "venues"),
        ("Heaven", "Q5694616",
         "A gay club opened in December 1979 by Jeremy Norman in the arches under Charing Cross station, once wine cellars. "
         "Paul Oakenfold's acid house nights were held here in the 1980s.",
         "en:Heaven (nightclub)", ("December 1979 by Jeremy Norman", "arches beneath Charing Cross railway station",
                                   "wine-cellar", "Paul Oakenfold"), None, "venues"),
        ("Jazz Cafe", "Q6168202",
         "A Camden Town venue for 450 people, opened in 1990 in a former Barclays Bank branch.",
         "en:The Jazz Cafe", ("opened in 1990", "Barclays Bank", "450 people"), None, "venues"),
        ("Fabric", "Q1390710",
         "A nightclub opened in 1999 in the former Metropolitan Cold Stores opposite Smithfield meat market. Islington "
         "Council revoked its licence in 2016; it reopened after a campaign.",
         "en:Fabric (club)", ("Founded in 1999", "Metropolitan Cold Stores", "Smithfield", "revoked by Islington Council in 2016"),
         None, "venues"),
        ("Cafe Oto", "Q18411011",
         "A Dalston venue for free jazz and experimental music, opened in 2008 in a building used by a paint-mixing firm "
         "from 1866 to 1954.",
         "en:Cafe Oto", ("opened in 2008", "paint mixing company from 1866 to 1954", "free jazz"), None, "venues"),
        ("34 Montagu Square", "Q14993660",
         "A flat leased by Ringo Starr in the 1960s. Jimi Hendrix wrote 'The Wind Cries Mary' here, and John Lennon and "
         "Yoko Ono took the photograph for the Two Virgins cover here.",
         "en:34 Montagu Square, Marylebone", ("Ringo Starr", "The Wind Cries Mary", "John Lennon and Yoko Ono",
                                              "Two Virgins"), None, "pop"),
        ("Decca Studios", "Q5248844",
         "Decca's studios at 165 Broadhurst Gardens from 1937 to 1980, in a former West Hampstead Town Hall. The Beatles "
         "failed their audition here on 1 January 1962.",
         "en:Decca Studios", ("165 Broadhurst Gardens", "1937 to 1980", "West Hampstead Town Hall",
                              "failed their Decca audition", "1 January 1962"), None, "pop"),
        ("IBC Studios", "Q3501074",
         "Studios at 35 Portland Place set up by Leonard Plugge in the 1930s as a commercial rival to the BBC. In the "
         "1960s the Who, the Kinks and Cream recorded here.",
         "en:IBC Studios", ("35 Portland Place", "Leonard Plugge", "commercial rival to the BBC", "the Kinks", "the Who",
                            "Cream"), None, "pop"),
        ("RAK Studios", "Q4993389",
         "Mickie Most founded these studios in 1976 in a Victorian former school and church hall near Regent's Park.",
         "en:RAK Studios", ("founded in 1976", "Mickie Most", "school and church hall"), None, "pop"),
        ("215 King's Road", "Q15978840",
         "A pair of houses of 1720 in Chelsea. In 1771 No. 215 was the home of the composer Thomas Arne; "
         "the actress Ellen Terry lived there from 1904 to 1920.",
         "en:213 and 215 King's Road", ("built in 1720", "1771", "Thomas Arne", "Ellen Terry", "1904 to 1920"),
         "1266690", "classical"),
        ("4 Hobart Place", "Q26319557",
         "Felix Mendelssohn made ten visits to Britain, where many of his major works were first performed. A blue "
         "plaque for his London residence was put up at 4 Hobart Place, Belgravia, in 2013.",
         "en:Felix Mendelssohn", ("ten visits to Britain", "4 Hobart Place", "2013"), "1066634", "classical"),
        ("Fenton House", "Q5443622",
         "A Hampstead merchant's house of the 1690s, left to the National Trust in 1952. It holds the Benton Fletcher "
         "collection of early keyboard instruments, some of which are played for visitors.",
         "en:Fenton House, Hampstead", ("17th-century merchant's house", "1952", "Benton Fletcher collection",
                                        "early keyboard instruments"), "1378648", "classical"),
        ("The Logs", "Q27086566",
         "A Hampstead house of about 1868 that Pevsner called a 'formidable atrocity'. The comedian Marty Feldman lived "
         "here, and Boy George has owned it since the 1980s.",
         "en:The Logs", ("c.1868", "formidable atrocity", "Marty Feldman", "Boy George"), "1379149", "pop"),
    ],
    "science": [
        ("Guy's Hospital", "Q777039",
         "Founded in 1721 by the philanthropist Thomas Guy. Its Tower Wing of 1974, 148.65 metres tall, was "
         "then the tallest hospital building in the world.",
         "en:Guy's Hospital", ("Thomas Guy in 1721", "Tower Wing", "1974", "tallest hospital building in the world"),
         "1385877", "hospitals"),
        ("General Lying-In Hospital", "Q5532007",
         "One of the first maternity hospitals in Britain, opened in 1767. It moved to this building on York Road in "
         "1828 and closed in 1971.",
         "en:General Lying-In Hospital", ("one of the first maternity hospitals in Great Britain", "1767",
                                          "York Road", "22 September 1828", "closed in 1971"), "1357956", "hospitals"),
        ("Moorfields Eye Hospital", "Q1946861",
         "Founded in 1805 as a dispensary for diseases of the eye and ear, it moved to City Road in 1899. With the UCL "
         "Institute of Ophthalmology it is the oldest and largest eye centre in Europe.",
         "en:Moorfields Eye Hospital", ("in 1805", "diseases of the Eye and Ear", "present site in 1899",
                                        "oldest and largest centre for ophthalmic treatment"), None, "hospitals"),
        ("Royal Free Hospital", "Q7374196",
         "William Marsden founded the Royal Free in 1828 to give free care to the poor. The 12-storey tower in Hampstead "
         "opened in 1974.",
         "en:Royal Free Hospital", ("founded in 1828 by the surgeon William Marsden", "free care",
                                    "12-storey cruciform tower", "It opened in 1974"), None, "hospitals"),
        ("King's College Hospital", "Q1742181",
         "Opened in 1840 in a disused workhouse in Portugal Street, near King's College. It moved to William Pite's new "
         "buildings on Denmark Hill, begun in 1909.",
         "en:King's College Hospital", ("opened in 1840", "St Clement Danes workhouse", "Portugal Street",
                                        "William Pite", "Denmark Hill"), None, "hospitals"),
        ("Royal Brompton Hospital", "Q7373850",
         "Founded in the 1840s for patients with consumption (tuberculosis), whom other hospitals turned away. It is now "
         "the largest specialist heart and lung centre in the UK.",
         "en:Royal Brompton Hospital", ("consumption", "tuberculosis", "turned away from other hospitals",
                                        "largest specialist heart and lung medical centre"), None, "hospitals"),
        ("Royal Marsden Hospital", "Q50575536",
         "Founded by William Marsden in 1851 as the Free Cancer Hospital, the first hospital in the world dedicated to "
         "cancer. Its Brompton site is on Fulham Road.",
         "en:Royal Marsden Hospital", ("Free Cancer Hospital in 1851", "first hospital in the world dedicated to the study and treatment of cancer",
                                       "Fulham Road"), None, "hospitals"),
        ("London Chest Hospital", "Q6670225",
         "Founded in 1848, largely by Quakers, and opened beside Victoria Park in 1855. It closed in 2015 when its "
         "services moved to St Bartholomew's.",
         "en:London Chest Hospital", ("13 March 1848", "Quakers", "opened in 1855", "Victoria Park", "17 April 2015"),
         None, "hospitals"),
        ("St Pancras Hospital", "Q7595036",
         "Set up in 1848 as the infirmary of the St Pancras workhouse, and partly housed in the original 18th-century "
         "workhouse buildings.",
         "en:St Pancras Hospital", ("infirmary for the St Pancras Union Workhouse in 1848",
                                    "original 18th-century workhouse buildings"), None, "hospitals"),
        ("German Hospital", "Q15428772",
         "Founded in Dalston in 1845 to give free treatment to London's German-speaking community. Its German staff were "
         "interned in the Second World War; it closed in 1987.",
         "en:German Hospital, Dalston", ("1845", "German-speaking community", "interned during the Second World War",
                                         "closed in 1987"), None, "hospitals"),
        ("Mile End Hospital", "Q6851069",
         "Started in 1859 as the infirmary of the Mile End workhouse and rebuilt in 1883. It was a military hospital in "
         "the First World War.",
         "en:Mile End Hospital", ("infirmary for the local workhouse in 1859", "1883", "military hospital"),
         "1065302", "hospitals"),
        ("National Hospital, Queen Square", "Q3336892",
         "Founded by Johanna Chandler in 1859 as the National Hospital for the Paralysed and Epileptic, the first in "
         "England for diseases of the nervous system.",
         "en:National Hospital for Neurology and Neurosurgery", ("Johanna Chandler", "1859",
                                                                 "National Hospital for the Paralysed and Epileptic",
                                                                 "first hospital to be established in England"),
         None, "hospitals"),
        ("St Peter's Hospital", "Q18392694",
         "The Hospital for Stone, founded in 1860, moved into this Queen Anne style building in Henrietta Street, Covent "
         "Garden, opened in 1882.",
         "en:St Peter's Hospital, Covent Garden", ("Hospital for Stone", "1860", "Henrietta Street", "Queen Anne style",
                                                   "1882"), "1278382", "hospitals"),
        ("Samaritan Hospital for Women", "Q26532766",
         "Began in 1847 as the Gynaepathic Institute in Manchester Square. Its purpose-built hospital on Marylebone "
         "Road opened in October 1889.",
         "en:Samaritan Hospital for Women", ("Gynaepathic Institute", "January 1847", "Marylebone Road",
                                             "opened in October 1889"), "1239818", "hospitals"),
        ("Paddington Green Children's Hospital", "Q55628344",
         "A children's hospital founded as a free dispensary in 1862. It moved to Paddington Green in 1883, was rebuilt "
         "in 1895, and closed in 1987.",
         "en:Paddington Green Children's Hospital", ("1862", "Paddington Green in 1883", "1895", "closed in 1987"),
         "1357437", "hospitals"),
        ("Belgrave Hospital for Children", "Q15198238",
         "A children's hospital designed by Charles Holden and built in 1899–1926 at 1 Clapham Road, Kennington. It is "
         "now flats.",
         "en:Belgrave Hospital for Children", ("Charles Holden", "between 1899 and 1926", "1 Clapham Road",
                                               "residential flats"), "1358241", "hospitals"),
        ("Royal Waterloo Hospital", "Q7374995",
         "Founded in 1816 as the Universal Dispensary for Children. The present building of 1903–05 by Sir Charles "
         "Nicholson closed as a hospital in 1981.",
         "en:Royal Waterloo Hospital for Children and Women", ("1816", "Universal Dispensary for Children",
                                                               "Between 1903 and 1905", "Sir Charles Nicholson",
                                                               "closed in 1981"), "1356166", "hospitals"),
        ("Queen Alexandra Military Hospital", "Q7270174",
         "An army hospital beside the Tate on Millbank, opened by Edward VII and Queen Alexandra in 1905 and closed in "
         "1977. Several of its buildings remain.",
         "en:Queen Alexandra Military Hospital", ("July 1905", "Edward VII", "closed in 1977", "several buildings remain"),
         None, "hospitals"),
        ("Royal Army Medical College", "Q7373693",
         "The army's medical college on the site of Millbank Prison, next to Tate Britain. It left in 1999 and Chelsea "
         "College of Arts took over the buildings.",
         "en:Royal Army Medical College", ("Millbank Prison", "Tate Britain", "moved from the site in 1999",
                                           "Chelsea College of Arts"), None, "hospitals"),
        ("Maudsley Hospital", "Q6792344",
         "The psychiatrist Henry Maudsley offered the LCC £30,000 in 1907 for a new mental hospital, which opened in "
         "February 1923.",
         "en:Maudsley Hospital", ("Henry Maudsley", "£30,000", "1907", "February 1923"), None, "hospitals"),
        ("Evelina London Children's Hospital", "Q5416238",
         "Founded in 1869 by Ferdinand de Rothschild in memory of his wife Evelina. It moved into Hopkins Architects' "
         "building beside St Thomas' in 2005.",
         "en:Evelina London Children's Hospital", ("1869", "Ferdinand de Rothschild", "Evelina", "Hopkins Architects",
                                                   "31 October 2005"), None, "hospitals"),
        ("Working Men's College", "Q8034933",
         "Founded in 1854 by Christian Socialists to give working men a liberal education; John Ruskin and "
         "Dante Gabriel Rossetti were among its early supporters. It is Europe's oldest surviving centre for adult education.",
         "en:Working Men's College", ("Founded in 1854", "Christian Socialists", "John Ruskin", "Dante Gabriel Rossetti",
                                      "Europe's oldest extant centre for adult education"), "1067378", "learning"),
        ("Lowther Lodge", "Q6694193",
         "A house built by Norman Shaw in about 1872–75 for the MP William Lowther. The Royal Geographical Society bought "
         "it in 1912.",
         "en:Lowther Lodge", ("Richard Norman Shaw", "1872 and 1875", "William Lowther", "Royal Geographical Society since 1912"),
         "1217774", "learning"),
        ("One Great George Street", "Q7092688",
         "The four-domed headquarters of the Institution of Civil Engineers off Parliament Square, built in 1910–13 to a "
         "design by James Miller.",
         "en:One Great George Street", ("four-domed", "Institution of Civil Engineers", "between 1910 and 1913",
                                        "James Miller"), "1066740", "learning"),
        ("London School of Hygiene and Tropical Medicine", "Q1126189",
         "Founded by Sir Patrick Manson in 1899; the school moved into its Art Deco building in Keppel Street in 1929.",
         "en:London School of Hygiene and Tropical Medicine", ("Sir Patrick Manson", "1899", "Art Deco headquarters in Keppel Street in 1929"),
         "1113106", "learning"),
        ("Francis Crick Institute", "Q326044",
         "A biomedical research centre beside St Pancras, opened in 2016. With 1,250 scientists it is the biggest single "
         "biomedical laboratory in Europe.",
         "en:Francis Crick Institute", ("opened in 2016", "1,250 scientists", "biomedical laboratory in Europe",
                                        "Brill Place"), None, "learning"),
        ("Colonnade Hotel", "Q5148462",
         "Two Victorian houses of 1865 in Little Venice, later a boarding school and a nursing home. Alan Turing was born "
         "here in 1912.",
         "en:Colonnade Hotel", ("two private Victorian residences in 1865", "Alan Turing was born there in 1912"),
         "1274016", "discoveries"),
        ("Faraday Building", "Q5434697",
         "A Post Office telephone exchange from 1902, rebuilt in 1933 for the International Telephone Exchange. Its "
         "height blocked the view of St Paul's from the river and caused an outcry.",
         "en:Faraday Building", ("In 1902", "telephone exchange", "International Telephone Exchange",
                                 "blocked the view of St Paul's Cathedral"), None, "discoveries"),
        ("Highgate Literary and Scientific Institution", "Q105044158",
         "Founded in 1839 to help local people follow new developments in industry and science. It is one of the few "
         "such institutions to outlive the arrival of public libraries.",
         "en:Highgate Literary and Scientific Institution", ("founded in 1839", "discoveries in science",
                                                             "predate the widespread establishment of public libraries"),
         None, "learning"),
    ],
    "secrets": [
        ("Crosby Hall", "Q5188033",
         "The great hall of a merchant's house built on Bishopsgate in 1466. In 1910 it was taken down and rebuilt on "
         "Cheyne Walk in Chelsea, where it is now part of a private house.",
         "en:Crosby Hall, London", ("built in 1466", "Bishopsgate", "moved in 1910", "Cheyne Walk", "private residence"),
         "1358160", "survivals"),
        ("Bromley Hall", "Q4973682",
         "A manor house on the Blackwall Tunnel approach road, dated by tree rings to about 1485, the year of Bosworth. It "
         "is thought to be the oldest brick house in London.",
         "en:Bromley Hall", ("Blackwall Tunnel northern approach", "around 1485", "Tree ring analysis",
                             "oldest brick house in London"), "1357791", "survivals"),
        ("St Augustine's Tower", "Q7592548",
         "All that is left of Hackney's 16th-century parish church, pulled down in 1798. A 16th-century turret clock has "
         "worked on its third floor since at least 1608.",
         "en:St Augustine's Tower, Hackney", ("all that remains", "pulled down in 1798", "16th-century turret clock",
                                              "since at least 1608"), "1265635", "survivals"),
        ("York Watergate", "Q70066448",
         "A gate built around 1626 for York House, opening onto the Thames. Since the Victoria Embankment was built in "
         "the 1860s it has stood in a garden away from the water.",
         "en:York Water Gate", ("around 1626", "York House", "Victoria Embankment in the 1860s"), "1237938", "survivals"),
        ("Strand Lane 'Roman' Bath", "Q7361585",
         "Reputed since the 1830s to be Roman, the bath is in fact part of a cistern built in 1612 to feed a fountain at "
         "Somerset House. It was reused as a cold plunge bath from the 1770s.",
         "en:Roman Baths, Strand Lane", ("since the 1830s", "cistern built in 1612", "Somerset House",
                                         "cold plunge bath"), "1237102", "survivals"),
        ("Brunswick House", "Q23040678",
         "A Georgian mansion of 1758 left standing among the railway and towers of Vauxhall. The London and South Western "
         "Railway bought it in 1854.",
         "en:Brunswick House", ("1758", "Vauxhall", "London and South Western Railway Company in 1854"), "1357952",
         "survivals"),
        ("Brixton Windmill", "Q4804689",
         "Ashby's Mill was built in 1816 and turned by wind until 1862, when the sails were taken off. Restored by the LCC "
         "in 1964, it reopened to the public in 2011.",
         "en:Ashby's Mill", ("built in 1816", "until 1862", "restored in 1964 by London County Council", "2 May 2011"),
         "1080573", "survivals"),
        ("Queen's Tower", "Q7270127",
         "The 287-foot central tower of the Imperial Institute of 1887. A campaign led by John Betjeman saved it when the "
         "rest was demolished; by 1966 it stood alone on new foundations.",
         "en:Queen's Tower, London", ("287-foot", "Imperial Institute", "1887", "John Betjeman", "In 1966"),
         "1231643", "survivals"),
        ("Michael Faraday Memorial", "Q6830208",
         "A stainless steel box of 1961 at the Elephant and Castle, near Faraday's birthplace. Inside is an electrical "
         "substation for the Underground.",
         "en:Michael Faraday Memorial", ("stainless steel", "built in 1961", "Newington Butts", "electrical substation"),
         "1385511", "hidden rooms"),
        ("Pear Tree House", "Q7157970",
         "Eight council flats on the Central Hill Estate, built over a two-storey bunker that was the Civil Defence "
         "control centre for South-East London, planned in the era of the Cuban Missile Crisis.",
         "en:Pear Tree House", ("eight two-bedroom flats", "control centre in the basement", "two-storey bunker",
                                "Civil Defence control centre for South-East London", "Cuban Missile Crisis"), None, "hidden rooms"),
        ("Thames House", "Q198519",
         "Built in 1929–30 for ICI on land cleared after the 1928 Thames flood. MI5 has had its headquarters here since "
         "December 1994.",
         "en:Thames House", ("1929–30", "1928 Thames flood", "Imperial Chemical Industries", "MI5", "December 1994"),
         "1267604", "hidden rooms"),
        ("SIS Building", "Q198536",
         "Terry Farrell's headquarters for MI6 at Vauxhall Cross, completed in April 1994. He drew on 1930s power "
         "stations and Mayan and Aztec temples.",
         "en:SIS Building", ("Terry Farrell", "April 1994", "Mayan and Aztec religious temples",
                             "Bankside and Battersea Power Stations"), None, "hidden rooms"),
        ("50 Berkeley Square", "Q14954837",
         "A Mayfair townhouse, once George Canning's home, known in the late 19th century as the most haunted house in "
         "London. Most versions of the story put the ghost in the attic.",
         "en:50 Berkeley Square", ("most haunted house", "George Canning", "attic room"), "1066467", "odd details"),
        ("Two Temple Place", "Q7859280",
         "A Neo-Tudor estate office built by John Loughborough Pearson in 1895 for William Waldorf Astor, with carving "
         "by George Frampton and William Silver Frith.",
         "en:Two Temple Place", ("John Loughborough Pearson", "William Waldorf Astor, in 1895", "Neo-Tudor",
                                 "Sir George Frampton"), "1234514", "odd details"),
        ("The Tower House", "Q7769735",
         "William Burges's own Gothic house of 1875–81 in Melbury Road. John Betjeman inherited its lease in 1962; the "
         "actor Richard Harris and then Jimmy Page later owned it.",
         "en:The Tower House", ("William Burges", "1875 and 1881", "John Betjeman", "Richard Harris", "Jimmy Page"),
         "1225632", "odd details"),
        ("575 Wandsworth Road", "Q4640792",
         "A small Georgian terraced house that the Kenyan poet Khadambi Asalache bought in 1981 and covered inside with "
         "fretwork. He left it to the National Trust.",
         "en:575 Wandsworth Road", ("Khadambi Asalache", "1981", "fretwork", "National Trust"), None, "odd details"),
        ("St Martin's Theatre", "Q7594202",
         "Agatha Christie's The Mousetrap moved here from the Ambassadors in March 1974, continuing the longest "
         "continuous run of any show in the world.",
         "en:St Martin's Theatre", ("The Mousetrap", "March 1974", "Ambassadors", "longest continuous run"),
         "1379186", "odd details"),
        ("Mount Pleasant Mail Centre", "Q7374422",
         "Once one of the largest sorting offices in the world, on the site of Coldbath Fields Prison. From 1927 to 2003 "
         "it was the hub of the Post Office's underground railway, now a heritage line.",
         "en:Mount Pleasant Mail Centre", ("largest sorting offices in the world", "Coldbath Fields Prison",
                                           "From 1927 to 2003", "London Post Office Railway", "heritage railway"),
         None, "hidden rooms"),
        ("St John's Gate", "Q7593597",
         "Built in 1504 as the south gate of the Clerkenwell priory of the Knights Hospitaller. It was restored so heavily "
         "in the 19th century that the gate today is largely a Victorian recreation.",
         "en:St John's Gate, Clerkenwell", ("built in 1504", "Knights Hospitaller", "Victorian recreation"),
         "1208827", "survivals"),
        ("St Mary Moorfields", "Q2323998",
         "A Catholic church of 1903 squeezed between shop fronts in Eldon Street. Until a boundary change in 1994 it lay in "
         "Hackney, so the City of London had no Catholic church; now it is the only one.",
         "en:St Mary Moorfields", ("opened in 1903", "1994 boundary change", "only Catholic church in the City of London"),
         "1265731", "odd details"),
        ("Crocker's Folly", "Q16707726",
         "A lavish pub of 1898 in St John's Wood with 50 kinds of marble. The story goes that Frank Crocker built it to "
         "serve the new Great Central Railway terminus, which ended up elsewhere.",
         "en:Crocker's Folly", ("built in 1898", "50 different types of marble", "Frank Crocker", "Great Central Railway"),
         "1357150", "odd details"),
        ("The Gatehouse, Highgate", "Q129254730",
         "A pub on the site of the medieval toll gate that gave Highgate its name. Travellers coming through were made to "
         "'swear on the horns'.",
         "en:The Gatehouse, Highgate", ("oldest recorded structure in Highgate Village", "arched gateway",
                                        "Swearing on the Horns"), None, "odd details"),
        ("Schomberg House", "Q7432105",
         "In 1781 the quack doctor James Graham opened a 'Temple of Health and Hymen' here, with a 'celestial bed' fitted "
         "with early electrical devices. Gainsborough lived next door.",
         "en:Schomberg House", ("In 1781", "James Graham", "Temple of Health and Hymen", "celestial bed",
                                "Thomas Gainsborough"), "1225814", "odd details"),
        ("Park Crescent West ice well", "Q61951164",
         "A brick ice well 9.5 metres deep, built in 1780 and later used to store imported Norwegian ice. Covered over in "
         "the 19th century, it was found intact during building work in 2014.",
         "en:Park Crescent West ice well", ("9.5m deep", "in 1780", "Norwegian ice", "rediscovered in good condition",
                                            "2014"), "1427239", "hidden rooms"),
        ("London Silver Vaults", "Q6670775",
         "An underground market of silver dealers off Chancery Lane. A wartime bomb destroyed the building above but not "
         "the vaults; the shops have been underground since 1953.",
         "en:London Silver Vaults", ("subterranean marketplace", "Chancery Lane", "did not damage the vaults",
                                     "since 1953"), None, "hidden rooms"),
        ("Kingsway telephone exchange", "Q6413739",
         "A Cold War telephone exchange in tunnels under Chancery Lane station, first built as an air-raid shelter. In "
         "1956 it became the UK end of TAT-1, the first transatlantic telephone cable.",
         "en:Kingsway telephone exchange", ("Cold War-era", "Chancery Lane tube station", "deep-level air-raid shelter",
                                            "TAT-1", "D-Notice"), None, "hidden rooms"),
        ("St Ermin's Hotel", "Q7593037",
         "A mansion block of 1887–89 turned hotel, used by the intelligence services from the 1930s. The Special "
         "Operations Executive was born here, and Kim Philby and Guy Burgess worked from offices in the building.",
         "en:St. Ermin's Hotel", ("1887–1889", "Special Operations Executive", "Kim Philby, Guy Burgess"),
         "1292333", "hidden rooms"),
        ("Whitehall Court", "Q7995986",
         "A riverside block of luxury flats built from 1884, where George Bernard Shaw and Lord Kitchener lived. Until "
         "the end of the First World War it was also the headquarters of MI6.",
         "en:Whitehall Court", ("1884", "George Bernard Shaw", "Lord Kitchener",
                                "Secret Intelligence Service (MI6) headquarters until the end of the First World War"),
         "1266894", "hidden rooms"),
    ],
}
