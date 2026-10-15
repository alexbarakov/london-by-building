"""DRAFT context layer 'The world in London', part B: buildings tied to other countries and regions.

Same entry format as pipeline/curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or
None, group). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia
article (API prop=extracts, explaintext=1, redirects=1); checks were run on 2026-10-15. Each QID was read from
Special:EntityData: it has P625, the point falls inside one of the nine borough polygons in data/raw/boundary.json,
and no P576 is set. NHLE numbers are copied from P1216 where present. Where the building's own article does not
carry the tie to the country, the entry cites the article of the person, event or institution that names it.

Counts: caribbean 10, africa 11, ireland 13, usa 18, poland 11, greece 9, commonwealth 9, middleeast 12 (93).

Duplicates with curated.py (kept because the story here is about the country; drop one side before merging):
- Benjamin Franklin House (Q4888645, 'exiles'): same building, story here is the same Franklin fact told for the US.
- Caxton Hall (Q5055269, 'exiles', Udham Singh): here the 1900 Pan-African Conference.
- Guildhall (Q81279, 'blitz'): here Chopin's last public concert, for Polish refugees.
- Euston station (Q800751, 'railways'): here the Matthew Flinders statue and grave.
Also overlaps the Harry Potter draft: Australia House (Q38166787), there as Gringotts, here as the High Commission.

Dropped during research:
- East London Mosque (curated 'eastend'), Leighton House Arab Hall (curated 'writers'/'houses' story already names
  the Arab Hall), West India Quay warehouses (curated 'port' already tells the slave-trade link): not repeated.
- Bangladesh: left to the East End layer, as asked.
- Mangrove restaurant (8 All Saints Road), Claudia Jones's West Indian Gazette office (250 Brixton Road), Marcus
  Garvey (Talgarth Road, Hammersmith - outside), C. L. R. James (Railton Road), Harold Moody (Peckham), Olive Morris:
  no Wikidata building items.
- Basing Street Studios (Island Records, Notting Hill): item has no coordinates.
- Una Marson at the BBC: her article does not name Broadcasting House.
- Clapham South deep shelter (Windrush arrivals 1948): no item for the shelter; the station item lies in Wandsworth.
- Jamaica High Commission (Prince Consort Road), Kenya High Commission (45 Portland Place, inside the Polish embassy's
  listed block), Nigeria House (Northumberland Avenue, Q27081036 exists but no article ties it to Nigeria),
  Ethiopian legation, Cyprus High Commission, Greek embassy (Holland Park; old residence 51 Upper Brook Street),
  Hungarian embassy (35 Eaton Place), Czech and Slovak embassy (Kensington Palace Gardens): no usable building item or
  no article text.
- ANC London office, 28 Penton Street (bombed 1982): no building item. Nkrumah (Burghley Road), Kenyatta
  (95 Cambridge Street): no items.
- West African Students' Union hostels (Camden Square, Chelsea Embankment): no items.
- Cromwell House, Highgate (Ghana High Commission annexe): in Haringey.
- Macdonald House (1 Grosvenor Square; US embassy 1938-60, Canadian HC 1961-2014): demolished behind a rebuilt facade.
- Dwight Moody's 1875 meetings at the Agricultural Hall: the Business Design Centre article does not mention them.
- Mark Twain (Tedworth Square), Sylvia Plath and W. B. Yeats (23 Fitzroy Road), Ezra Pound, Kossuth (Chepstow
  Villas), Joseph Conrad (Gillingham Street), Stoker (St Leonard's Terrace), Beaverbrook (Stornoway House):
  no item or no article text linking person and building.
- Eisenhower's 20 Grosvenor Square and Norfolk House: no item for the present buildings (Norfolk House item is the
  demolished 18th-century house).
- Sheridan's house in Savile Row: articles disagree on the number (14 vs 17).
- Hellenic Centre (Paddington Street): the item is the charity, without coordinates.
- Fazl Mosque, Kilburn's Irish churches on the Brent side: outside the nine boroughs.
- Lyceum Theatre used for Bob Marley (Caribbean) rather than Bram Stoker (Ireland); Royal Court for Wole Soyinka
  (Africa) rather than Shaw; Lancaster House for Chopin (Poland) rather than the 1979 Zimbabwe agreement; Lord's for
  the West Indies rather than the Ashes urn; the Dorchester for Eisenhower rather than its Brunei owners.

Doubts to check before publishing:
- Institution-type items carrying the building's coordinates (no separate building item found): Brixton Market,
  Keskidee Centre (the building burned in 2012; unclear how much stands), London Irish Centre, Aggrey House (a hostel at
  47 Doughty Street), St Thomas' Hospital (story is the Seacole statue at its entrance), HM Prison Pentonville, HM
  Prison Brixton, Polish Institute and Sikorski Museum, Royal College of Music, Ismaili Centre, Finsbury Park Mosque,
  Shacklewell Lane, Suleymaniye and Aziziye mosques, Garden Museum, Rubens at the Palace (hotel), London Central
  Mosque, British Museum (has NHLE), Harrods (has NHLE).
- Block or terrace items: 14-25 Princes Gate (Iranian embassy at no. 16), 49-58 Princes Gate (Polish Hearth at 55),
  41-47 Portland Place (Polish embassy at 47), 37-43 Eaton Place (no. 43), 13-23 Belgrave Square (Ghana at 13),
  38-48 Belgrave Square (Turkey at 43), 20-32 Fitzroy Square (Shaw at 29), 1-9 Woburn Walk (Yeats at 5),
  43-47 Harley Street (Queen's College). The map will highlight whichever building the point falls on.
- The Sikorski Museum (20 Princes Gate) sits inside the 14-25 Princes Gate block used for the Iranian embassy; the two
  QIDs are different but their points are about 40 m apart.
- The Oval (Q1155836) is a ground, not a building, and has no NHLE; Lord's uses the Pavilion item (Q6678854).
- St Patrick's, Soho Square: its article never says 'Irish'; the story relies on the dedication and Father O'Leary.
- Uganda House and the Ghana entry are thin (address and shared use only).
- Lots Road: the article calls Yerkes's company the builder but does not say Yerkes was American; true, but unchecked.
- Mercury Theatre: the building is now a private house; Marie Rambert's Polish birth is in her own article, not cited.
- 'middleeast' mixes Arab states, Iran, Turkey and Turkish Cypriot mosques; Israel is not covered.
- The Mayflower pub building dates from the 1950s; the tie is the name and the 1620 sailing from Rotherhithe.
"""

GROUPS = {
    "caribbean": (
        "The Caribbean",
        "Migrants from the West Indies, many of them arriving after the Empire Windrush docked in 1948, settled in "
        "Brixton, Notting Hill and north London, and built the archives, markets, halls and venues listed here.",
        [
            ("Raleigh Hall (Black Cultural Archives)", "Q23302047",
             "Two houses of 1824 on Windrush Square, long derelict, became the home of the Black Cultural Archives in "
             "2014. The archive was founded in 1981 by the historian Len Garrison and others.",
             "en:Black Cultural Archives",
             ("founded in 1981, by educationalist and historian Len Garrison", "the former Raleigh Hall",
              "1 Windrush Square", "officially opened on 24 July 2014"),
             "1358256"),
            ("Brixton Market", "Q15030874",
             "The street market and its 1920s-30s arcades are best known for African and Caribbean produce. The "
             "arcades were listed in 2010 partly as one of the principal hearts of the Afro-Caribbean community.",
             "en:Brixton Market",
             ("best known for its African and Caribbean produce",
              "one of the principal hearts of the Afro-Caribbean community in London", "Granville Arcade"),
             None),
            ("The Tabernacle, Notting Hill", "Q7673024",
             "A church of 1887 in Powis Square. Carnival committees used it every year in the weeks before the "
             "Notting Hill Carnival, with bands such as the Mangrove steel band.",
             "en:The Tabernacle, Notting Hill",
             ("built in 1887 as a church", "the weeks leading up to the Notting Hill Carnival",
              "Mangrove steel band"),
             "1265586"),
            ("Camden Town Hall (St Pancras Town Hall)", "Q5025822",
             "On 30 January 1959 Claudia Jones organised a 'Caribbean Carnival' here in response to the 1958 Notting "
             "Hill race riots. It is counted as a precursor of the Notting Hill Carnival.",
             "en:Camden Town Hall",
             ("a precursor of the Notting Hill Carnival", "held on 30 January 1959 in the town hall",
              "organised by activist Claudia Jones", "1958 Notting Hill race riots"),
             "1379162"),
            ("Lambeth Town Hall", "Q23663120",
             "In 1998 Sam King, a former mayor of Southwark, led the 50th anniversary celebrations of the Empire "
             "Windrush's arrival, and a plaque was put up in the town hall.",
             "en:Lambeth Town Hall",
             ("Sam King", "HMT Empire Windrush", "a plaque was erected in the town hall to commemorate the event"),
             "1080534"),
            ("Lyceum Theatre", "Q1661445",
             "Bob Marley and the Wailers' album Live! was recorded at the Lyceum in July 1975, using the Rolling "
             "Stones Mobile Studio.",
             "en:Live! (Bob Marley and the Wailers album)",
             ("recorded live in concert during July 1975 at the Lyceum Theatre, London",
              "Rolling Stones Mobile Studio"),
             "1066119"),
            ("Rainbow Theatre", "Q3288732",
             "The former Finsbury Park Astoria of 1930. Bob Marley and the Wailers played four nights here in June "
             "1977 on the Exodus tour.",
             "en:Rainbow Theatre",
             ("Finsbury Park Astoria", "Bob Marley & the Wailers played on 1, 2, 3 and 4 June 1977",
              "Exodus Tour"),
             "1297977"),
            ("Keskidee Centre", "Q16988953",
             "Britain's first arts centre for the Black community, opened in 1971 in a Victorian mission hall by the "
             "Guyanese architect Oscar Abrams. Linton Kwesi Johnson developed dub poetry here.",
             "en:Keskidee Centre",
             ("Britain's first arts centre for the Black community, founded in 1971",
              "Guyanese architect and cultural activist Oscar Abrams",
              "It was at the Keskidee Centre that Johnson developed dub poetry"),
             None),
            ("St Thomas' Hospital", "Q1143779",
             "A statue of the Jamaican nurse Mary Seacole, who cared for soldiers in the Crimean War, was unveiled "
             "at the hospital's entrance on 30 June 2016.",
             "en:Mary Seacole",
             ("was a Jamaican nurse and businesswoman", "statue of Seacole at St Thomas' Hospital",
              "30 June 2016"),
             None),
            ("Lord's Pavilion", "Q6678854",
             "The West Indies played their first Test at Lord's in 1928, and won the first two men's World Cup "
             "finals here, in 1975 and 1979.",
             "en:Lord's",
             ("The West Indies under the captaincy of Karl Nunes played their first Test match at Lord's in 1928",
              "with the West Indies triumphing over Australia", "the final of the 1979 World Cup"),
             "1235992"),
        ],
    ),
    "africa": (
        "Africa",
        "Students, exiles and diplomats from Africa met, organised and protested in these buildings, from the "
        "first Pan-African Conference in 1900 to the vigil outside South Africa House in the 1980s.",
        [
            ("South Africa House", "Q141349573",
             "Herbert Baker's building on Trafalgar Square opened in 1933. In the 1980s a four-year non-stop vigil "
             "outside demanded the release of political prisoners, and Nelson Mandela appeared on its balcony in 1996.",
             "en:High Commission of South Africa, London",
             ("designed by Sir Herbert Baker", "opened in 1933", "four-year non-stop vigil",
              "Nelson Mandela appeared on the balcony of South Africa House in 1996"),
             "1066238"),
            ("Zimbabwe House", "Q133574839",
             "Charles Holden's building for the British Medical Association became Rhodesia House in 1935. After "
             "Rhodesia's declaration of independence in 1965 it lost diplomatic status until the country became "
             "Zimbabwe in 1980.",
             "en:Embassy of Zimbabwe, London",
             ("designed by architect Charles Holden in 1907–08",
              "acquisition of the building by the Government of Southern Rhodesia in 1935",
              "Unilateral Declaration of Independence on 11 November 1965", "until the country became Zimbabwe in 1980"),
             "1237039"),
            ("Uganda House", "Q27083300",
             "The Ugandan High Commission at 58-59 Trafalgar Square, which it shares with the Embassy of Burundi; "
             "diaspora protests have been held outside it.",
             "en:High Commission of Uganda, London",
             ("58-59 Trafalgar Square", "shares the building with the Embassy of Burundi"),
             "1266213"),
            ("38 King Street, Covent Garden (Africa Centre)", "Q27083662",
             "A former banana warehouse given by the Catholic Church 'to the people of Africa'. Kenneth Kaunda "
             "opened the Africa Centre here in 1964; it stayed until 2013.",
             "en:Africa Centre, London",
             ("banana warehouse in the 18th century", "given by the Catholic Church in perpetuity to the people of Africa",
              "officiated by Kenneth Kaunda", "Archbishop Desmond Tutu used to meet Thabo Mbeki at the bar"),
             "1275120"),
            ("Africa House, Kingsway", "Q27086661",
             "An office block completed in 1922. Its pediment carries Benjamin Clemens's carving of Britannia with "
             "African workers and animals.",
             "en:Africa House, London",
             ("Completed in 1922", "Britannia with African workers and animals by Benjamin Clemens"),
             "1379261"),
            ("Aggrey House, 47 Doughty Street", "Q81419064",
             "A Colonial Office hostel for African students, opened in 1934 next to Dickens's old home. George "
             "Padmore and Jomo Kenyatta spoke here.",
             "en:Aggrey House",
             ("established in London, England, in 1934", "47 Doughty Street",
              "George Padmore and Jomo Kenyatta were among notable figures"),
             None),
            ("St Margaret's, Westminster", "Q823412",
             "Olaudah Equiano, who bought his freedom and became a leading abolitionist, was christened here as "
             "Gustavus on 9 February 1759.",
             "en:St Margaret's, Westminster",
             ("Olaudah Equiano", "christened as Gustavus on 9 February 1759"),
             "1226286"),
            ("Caxton Hall", "Q5055269",
             "As Westminster Town Hall it hosted the first Pan-African Conference, 23-25 July 1900, organised by "
             "Henry Sylvester Williams. Its address spoke of 'the problem of the colour-line'.",
             "en:1900 Pan-African Conference",
             ("from 23 to 25 July 1900", "Westminster Town Hall (now Caxton Hall)",
              "Trinidadian barrister Henry Sylvester Williams",
              "The problem of the Twentieth Century is the problem of the colour-line"),
             "1357266"),
            ("Royal Court Theatre", "Q1169370",
             "The Nigerian writer Wole Soyinka worked as a play reader here, and his play The Invention was "
             "produced here in 1957.",
             "en:Wole Soyinka",
             ("worked as a play reader for the Royal Court Theatre",
              "In 1957, his play, The Invention, was produced at London's Royal Court Theatre"),
             "1226628"),
            ("13-23 Belgrave Square", "Q17527029",
             "No. 13 houses one of the two London offices of the High Commission of Ghana.",
             "en:High Commission of Ghana, London",
             ("13 Belgrave Square",),
             "1066457"),
            ("Royal College of Music", "Q304985",
             "Samuel Coleridge-Taylor, son of a doctor from Sierra Leone, won a scholarship here at 15; his "
             "Hiawatha's Wedding Feast followed in 1898.",
             "en:Samuel Coleridge-Taylor",
             ("a Creole man from Sierra Leone", "awarded a scholarship to study at the Royal College of Music from the age of 15",
              "Hiawatha's Wedding Feast"),
             None),
        ],
    ),
    "ireland": (
        "Ireland",
        "Irish writers, workers and rebels came to London for two centuries; their churches, theatres, prisons "
        "and the bomb sites of the Troubles are all still standing.",
        [
            ("London Irish Centre", "Q6670524",
             "Opened in Camden Square in 1955 as a hostel and job centre, close to Euston, where Irish arrivals "
             "came in on the trains from Holyhead.",
             "en:London Irish Centre",
             ("has served the Irish community since 1955",
              "proximity to Euston Station, where Irish people disembarked their trains from Holyhead Ferry Port",
              "Mary Robinson (in 1993)"),
             None),
            ("St Patrick's Church, Soho Square", "Q7595060",
             "Father Arthur O'Leary's chapel here, consecrated in 1792, was one of the first Catholic buildings "
             "allowed after the Reformation. The present church of 1891-93 quotes St Patrick over its door.",
             "en:St Patrick's Church, Soho Square",
             ("29 September 1792", "one of the first Catholic buildings allowed in Great Britain after the Reformation",
              "Father Arthur O'Leary", "It is a quotation taken from the writings of St. Patrick"),
             "1236286"),
            ("17 Grosvenor Place (Embassy of Ireland)", "Q26319638",
             "A French Renaissance-style mansion of 1868, once leased by Ernest Guinness. After he gave it up in 1948 "
             "the lease passed to Ireland's Commissioners of Public Works, and it is now the Irish embassy.",
             "en:Embassy of Ireland, London",
             ("The embassy is located in 17 Grosvenor Place", "Built in 1868", "Ernest Guinness",
              "Commissioners of Public Works in Ireland"),
             "1066733"),
            ("Theatre Royal, Drury Lane", "Q1756626",
             "The Irish playwright Richard Brinsley Sheridan bought Drury Lane from Garrick and premiered The School "
             "for Scandal here in 1777. His theatre burned in 1809; the present one opened in 1812.",
             "en:Theatre Royal, Drury Lane",
             ("the Irish playwright Richard Brinsley Sheridan",
              "Sheridan premiered his own comedy of manners The School for Scandal in 1777",
              "the theatre burned down", "The building that stands today opened in 1812"),
             "1357276"),
            ("Theatre Royal Haymarket", "Q540426",
             "Oscar Wilde premiered A Woman of No Importance here in 1893 and An Ideal Husband in 1895. A plaque "
             "to him hangs in the theatre.",
             "en:Theatre Royal Haymarket",
             ("Oscar Wilde premiered his comedy A Woman of No Importance in April 1893",
              "In January 1895 Wilde's An Ideal Husband was first performed at the theatre",
              "There is a memorial plaque to Wilde at the theatre"),
             "1066641"),
            ("34 Tite Street", "Q27081279",
             "Oscar Wilde's house from his marriage in 1884 until his arrest in 1895.",
             "en:Tite Street",
             ("Oscar Wilde lived here from his marriage in 1884 until his arrest in 1895",),
             "1227010"),
            ("20-32 Fitzroy Square", "Q17542322",
             "No. 29 was George Bernard Shaw's home from 1887 until his marriage in 1898; Virginia Woolf lived "
             "there later.",
             "en:Fitzroy Square",
             ("29 was the home of George Bernard Shaw from 1887 until his marriage in 1898",),
             "1112996"),
            ("1-9 Woburn Walk", "Q17548869",
             "W. B. Yeats lived in the house that is now 5 Woburn Walk.",
             "en:Woburn Walk",
             ("Yeats lived at what is today 5 Woburn Walk",),
             "1379209"),
            ("HM Prison Pentonville", "Q1504639",
             "The model prison of 1842 where the Irish revolutionary Roger Casement was hanged on 3 August 1916. "
             "Éamon de Valera was held here in 1917.",
             "en:HM Prison Pentonville",
             ("completed in 1842", "Irish revolutionary Roger Casement was hanged there on 3 August 1916",
              "1917: Éamon de Valera"),
             None),
            ("HM Prison Brixton", "Q1764624",
             "Terence MacSwiney, Lord Mayor of Cork, died here on hunger strike in 1920. Two IRA prisoners escaped "
             "in 1991.",
             "en:HM Prison Brixton",
             ("Terence MacSwiney, former Lord Mayor of Cork", "went on hunger strike and died at the prison",
              "two Provisional IRA prisoners"),
             None),
            ("St George's Cathedral, Southwark", "Q1451262",
             "Pugin's cathedral of 1848 was built because Irish immigrants had outgrown the old chapel. MacSwiney's "
             "funeral Mass was held here in 1920, and its east and west windows are by Harry Clarke of Dublin.",
             "en:St George's Cathedral, Southwark",
             ("the arrival of Irish immigrants in the area necessitated the construction of a larger house of worship",
              "funeral Mass of Irish nationalist Terence MacSwiney", "Harry Clarke of Dublin"),
             "1385643"),
            ("St Giles in the Fields", "Q3495322",
             "The parish of the St Giles Rookery, where thousands of poor Irish Catholic immigrants were buried in "
             "the churchyard.",
             "en:St Giles in the Fields",
             ("St Giles Rookery", "many thousands of poor and nameless Irish Catholic immigrants to London"),
             "1245864"),
            ("St Ethelburga's, Bishopsgate", "Q7593042",
             "The medieval church was half destroyed by the IRA's Bishopsgate bomb in 1993. Rebuilt, it reopened as "
             "a Centre for Reconciliation and Peace.",
             "en:St Ethelburga's Bishopsgate",
             ("a massive IRA bomb exploded 7 metres from the church", "Centre for Reconciliation and Peace"),
             "1191603"),
        ],
    ),
    "usa": (
        "The United States",
        "From the Pilgrim Fathers' captain and John Harvard to Eisenhower's wartime Mayfair, American history "
        "runs through these London buildings.",
        [
            ("Southwark Cathedral", "Q922967",
             "John Harvard, whose bequest founded Harvard University, was baptised here on 29 November 1607. Harvard "
             "alumni paid for the Harvard Chapel in the north transept.",
             "en:Southwark Cathedral",
             ("baptised in the church on 29 November 1607", "Harvard Chapel in the north transept"),
             "1378460"),
            ("St Mary's Church, Rotherhithe", "Q7590184",
             "Christopher Jones, captain of the Mayflower that took the Pilgrim Fathers to America in 1620, is "
             "buried here.",
             "en:St Mary's Church, Rotherhithe",
             ("Christopher Jones, captain of the Mayflower", "Pilgrim Fathers"),
             "1385867"),
            ("The Mayflower, Rotherhithe", "Q135762993",
             "The Mayflower sailed from Rotherhithe in July 1620. The riverside pub named after it looks older but "
             "dates from the 1950s.",
             "en:Rotherhithe",
             ("In July 1620, the Mayflower sailed from Rotherhithe",
              "The Mayflower pub, despite external and interior appearances, dates only from the 1950s"),
             None),
            ("Benjamin Franklin House", "Q4888645",
             "Franklin lived and worked at 36 Craven Street from 1757 to 1774, as agent for the American colonies. "
             "The house opened as a museum in 2006.",
             "en:Benjamin Franklin House",
             ("36 Craven Street", "Franklin lived and worked there from 1757 to 1774",
              "The museum opened to the public on 17 January 2006"),
             "1066930"),
            ("9 Grosvenor Square", "Q27080594",
             "John Adams opened the first American legation in London here in 1785, two years after the end of "
             "the War of Independence.",
             "en:Embassy of the United States, London",
             ("John Adams was the first minister to open an American legation in London, in 1785 at 9 Grosvenor Square",),
             "1214440"),
            ("Former US Embassy, Grosvenor Square", "Q55517890",
             "Eero Saarinen's chancery opened in 1960, with Theodore Roszak's gilded eagle on the roof. It saw the "
             "anti-Vietnam War marches of 1968 and reopened in 2025 as a hotel.",
             "en:Embassy of the United States, London",
             ("Finnish American modernist architect Eero Saarinen", "opening in 1960",
              "gilded aluminum bald eagle by Theodore Roszak", "against US involvement in the Vietnam War",
              "The Chancery Rosewood"),
             "1393496"),
            ("Grosvenor Chapel", "Q5610634",
             "In the Second World War American servicemen and women came to this Mayfair chapel for Sunday services, "
             "as a tablet on its west wall records.",
             "en:Grosvenor Chapel",
             ("men and women of the American armed forces were welcomed to the chapel for their Sunday services",
              "US General Dwight D"),
             "1236429"),
            ("The Dorchester", "Q2749941",
             "Eisenhower took a first-floor suite in 1942, trusting the hotel's concrete frame, and in 1944 made it "
             "his headquarters.",
             "en:The Dorchester",
             ("Eisenhower took a suite on the first floor (now the Eisenhower Suite) in 1942",
              "in 1944 he made it his headquarters"),
             "1225963"),
            ("Selfridges", "Q7448348",
             "The American retailer Harry Gordon Selfridge opened his Oxford Street store on 15 March 1909. Daniel "
             "Burnham of Chicago designed it, bringing American steel-frame construction.",
             "en:Selfridges",
             ("American retail magnate Harry Gordon Selfridge", "opened on 15 March 1909",
              "The original London store was designed by Daniel Burnham"),
             "1357436"),
            ("Bush House", "Q852282",
             "Built by the American Irving T. Bush as a trade centre, to designs by Harvey Wiley Corbett, and "
             "inscribed 'To the friendship of English speaking peoples'. Later the BBC World Service's home.",
             "en:Bush House",
             ("American industrialist Irving T", "American architect Harvey Wiley Corbett",
              "To the friendship of English speaking peoples", "headquarters of the BBC World Service"),
             "1066492"),
            ("Lots Road Power Station", "Q1871101",
             "Built by Charles Yerkes's company to power the Underground, it began working on 1 February 1905 and "
             "was claimed as the largest power station ever built.",
             "en:Lots Road Power Station",
             ("Charles Yerkes' Metropolitan District Electric Traction Company", "operational on 1 February 1905",
              "the largest power station ever built"),
             None),
            ("The Old Vic", "Q868806",
             "In 1825 Ira Aldridge, an 18-year-old Black American actor, played here, then the Royal Coburg, in "
             "The Revolt of Surinam.",
             "en:The Old Vic",
             ("Royal Coburg Theatre", "In 1825 an 18-year-old black American actor, Ira Aldridge, played here",
              "The Revolt of Surinam"),
             "1068710"),
            ("Savoy Theatre", "Q2165797",
             "Paul Robeson played Othello here in 1930 opposite Peggy Ashcroft, the first Black actor in the role in "
             "Britain since Ira Aldridge.",
             "en:Paul Robeson",
             ("Robeson then returned to the Savoy Theatre in London's West End to play the title role of Othello",
              "Robeson was the first black actor to play Othello in Britain since Ira Aldridge"),
             "1236724"),
            ("St George's, Hanover Square", "Q3495317",
             "Theodore Roosevelt, aged 28, married Edith Carow here on 2 December 1886.",
             "en:St George's, Hanover Square",
             ("Theodore Roosevelt, future United States President, aged 28, and Edith Carow, aged 25, on 2 December 1886",),
             "1235638"),
            ("Lindsey House", "Q6552886",
             "James McNeill Whistler lived at what is now 96 Cheyne Walk from 1866 to 1878 and painted the river "
             "from here.",
             "en:Lindsey House",
             ("James McNeill Whistler between 1866 and 1878 at 2 Lindsey Row (now 96 Cheyne Walk)",),
             "1189891"),
            ("31 Tite Street", "Q27081278",
             "The home of the American portrait painter John Singer Sargent, with his studio next door at no. 33.",
             "en:Tite Street",
             ("No 31 (residence) & 33 (formerly 13) (studio)", "John Singer Sargent, American portrait painter"),
             "1227009"),
            ("Carlyle Mansions", "Q5043142",
             "The Chelsea flats of 1886 where the American-born writers Henry James and T. S. Eliot both lived.",
             "en:Carlyle Mansions",
             ("Built in 1886", "Henry James, American novelist", "T. S. Eliot, American-British poet and writer"),
             None),
            ("American International Church", "Q19587074",
             "The church for Americans in London grew out of wartime services at Grosvenor Chapel. Since 1972 it has "
             "met in the Whitefield Memorial Church, rebuilt after the last V-2 to fall on London.",
             "en:American International Church",
             ("established to cater for American expatriates resident in London",
              "Since 1972, the chapel has been the home of the American International Church",
              "destroyed by the last V-2 rocket to fall on London"),
             None),
        ],
    ),
    "poland": (
        "Poland and Central Europe",
        "London was the seat of Poland's government in exile from 1940, and Polish, Ukrainian and Lithuanian "
        "communities kept their own churches and clubs; Chopin gave his last concerts here in 1848.",
        [
            ("Lancaster House", "Q1146311",
             "Chopin gave a recital here, then Stafford House, in 1848 in the presence of Queen Victoria.",
             "en:Lancaster House",
             ("Chopin gave a recital there in 1848 in the presence of Queen Victoria", "Stafford House"),
             "1236546"),
            ("Guildhall", "Q81279",
             "Chopin's last public concert, on 16 November 1848, was played here for the benefit of Polish refugees.",
             "en:Frédéric Chopin",
             ("Chopin made his last public appearance on a concert platform at London's Guildhall on 16 November 1848",
              "for the benefit of Polish refugees"),
             "1064675"),
            ("41-47 Portland Place (Embassy of Poland)", "Q17550398",
             "Poland's legation opened at no. 47 in 1929. From 1940 it was the nerve centre of the whole Polish "
             "Foreign Office in exile, until Britain recognised the communist government in 1945.",
             "en:Embassy of Poland, London",
             ("it was not until 1929 that the first Polish legation was sent", "number 47, Portland Place",
              "the entire Polish Foreign Office"),
             "1265549"),
            ("37-43 Eaton Place", "Q27080414",
             "After 1945 the Polish government in exile moved to no. 43, the president's private residence, and "
             "stayed until 1990.",
             "en:Eaton Place",
             ("43, which had been the president's personal residence, where it stayed until 1990",),
             "1211057"),
            ("Rubens at the Palace", "Q111368942",
             "The hotel opposite the Royal Mews where the Polish government in exile under General Sikorski was "
             "based in the war.",
             "en:Ivan Maisky",
             ("Sikorski invited Maisky to see him at the Rubens Hotel, where the Polish government-in-exile was based",),
             None),
            ("Polish Hearth Club (49-58 Princes Gate)", "Q26319723",
             "Ognisko Polskie at no. 55, founded by the British and Polish governments in 1939 and opened in July "
             "1940. General Anders had his own table in its restaurant.",
             "en:Polish Hearth Club",
             ("at 55 Princes Gate, Exhibition Road", "On 16 July 1940 the club was formally inaugurated",
              "General Władysław Anders had his own table in the restaurant"),
             "1066826"),
            ("Polish Institute and Sikorski Museum", "Q7209930",
             "Founded on 2 May 1945 at 20 Prince's Gate to keep the records of Poland's wartime forces and "
             "underground state.",
             "en:Polish Institute and Sikorski Museum",
             ("housed at 20 Prince's Gate", "on 2 May 1945", "Polish Underground State"),
             None),
            ("Our Lady of Czestochowa and St Casimir, Devonia Road", "Q26580986",
             "London's first Polish church, bought in 1928.",
             "en:Poles in the United Kingdom",
             ("The original Polish church in London in Devonia Road, Islington was bought in 1928",),
             "1293022"),
            ("Mercury Theatre, Notting Hill Gate", "Q6818655",
             "A Sunday school of 1851 turned into a theatre in 1933 by Ashley Dukes for the ballet company of his "
             "wife, the Warsaw-born Marie Rambert. Ballet Rambert's school used it until 1987.",
             "en:Mercury Theatre, Notting Hill Gate",
             ("built in 1851 as a Sunday school", "opened in 1933 by Ashley Dukes", "run by his wife Marie Rambert",
              "closed in 1987"),
             None),
            ("Ukrainian Catholic Cathedral of the Holy Family", "Q2942529",
             "Alfred Waterhouse's King's Weigh House chapel of 1891, sold to the Ukrainian Catholics in 1967. It "
             "became a rallying point for Ukrainians in Britain in 2022.",
             "en:Ukrainian Catholic Cathedral of the Holy Family in Exile",
             ("designed by Alfred Waterhouse in 1891", "sold it to the Ukrainian Catholics in 1967",
              "rallying point for the British Ukrainian community during the 2022 Russian invasion of Ukraine"),
             "1210923"),
            ("St Casimir's Lithuanian Church", "Q20713028",
             "The Lithuanian mission's church in Bethnal Green, opened in 1912. A statue of St Casimir by the "
             "Lithuanian sculptor Antanas Žukauskas was added in 2009.",
             "en:St Casimir's Lithuanian Church",
             ("opened by Cardinal Bourne on 10 March 1912", "Antanas Žukauskas"),
             None),
        ],
    ),
    "greece": (
        "Greece and Cyprus",
        "Greek merchants built a cathedral in Bayswater in the 1870s, and Greek Cypriots who came after the war "
        "took over Victorian churches in Camden; Greek models also shaped London's Greek Revival buildings.",
        [
            ("St Sophia's Cathedral, Bayswater", "Q3464425",
             "Paid for by London's Greek merchants, who raised £50,000 in three years, and consecrated in 1882. In "
             "the Second World War it served the Greek government in exile.",
             "en:Saint Sophia Cathedral, London",
             ("consecrated as the Church of the Holy Wisdom on 5 February 1882",
              "The cost of £50,000 was raised in three years by the Greek community",
              "seat of the Greek government in exile"),
             "1223553"),
            ("All Saints Cathedral, Camden Town", "Q2942605",
             "A church of 1822-24 whose tower imitates the Choragic Monument of Lysicrates in Athens. It became Greek "
             "Orthodox in 1948 and serves a community mostly from Cyprus.",
             "en:All Saints Cathedral, Camden Street",
             ("Choragic Monument of Lysicrates", "All Saints became a Greek Orthodox church", "mostly from Cyprus"),
             "1244162"),
            ("Greek Orthodox Cathedral of St Andrew, Kentish Town", "Q27086646",
             "Built in 1884-85 as St Barnabas; Greek Orthodox use began in 1957, and it was bought with help from the "
             "Papathomas family of Cyprus.",
             "en:Greek Orthodox Cathedral of St Andrew the Apostle",
             ("built between 1884–85 to a design by Ewan Christian",
              "In 1957, the cathedral began to be used by the Greek Orthodox Church", "Papathomas family of Cyprus"),
             "1379241"),
            ("St Mary's Greek Orthodox Cathedral, Camberwell", "Q25404042",
             "One of the borough of Southwark's three cathedrals, alongside the Anglican and Roman Catholic ones.",
             "en:London Borough of Southwark",
             ("Saint Mary's Cathedral (Greek Orthodox)",),
             None),
            ("Theatro Technis", "Q71433207",
             "A Greek Cypriot theatre founded in 1957 by George Eugeniou, in an old church in Camden since 1978. It "
             "also runs an advice service for the Greek Cypriot community.",
             "en:Theatro Technis",
             ("founded in 1957 by George Eugeniou", "in 1978, it finally found its permanent home in an old Church building",
              "citizens advisory service for the local Greek Cypriot community"),
             None),
            ("British Museum (Duveen Gallery)", "Q6373",
             "Lord Elgin removed the Parthenon sculptures from Athens; they have been shown in the Duveen Gallery "
             "since 1962. Greece claims their return.",
             "en:British Museum",
             ("removed the large collection of marble sculptures from the Parthenon",
              "In 1962 the Duveen Gallery was finally restored", "claimed by Greece"),
             "1130404"),
            ("Royal Opera House", "Q55018",
             "Maria Callas, born in New York to Greek parents, made her London debut here in 1952 and ended her "
             "stage career here as Tosca on 5 July 1965.",
             "en:Maria Callas",
             ("to Greek parents", "In 1952, she made her London debut at the Royal Opera House in Norma",
              "on July 5, 1965, Callas ended her stage career in the role of Tosca"),
             "1066392"),
            ("St Pancras New Church", "Q7595040",
             "The Inwoods based this church of 1819-22 on the Erechtheum and the Tower of the Winds in Athens; "
             "caryatids copied from the Erechtheum stand at the east end.",
             "en:St Pancras New Church",
             ("the Erechtheum and the Tower of the Winds, both in Athens", "caryatids"),
             "1379062"),
            ("Athenaeum Club", "Q492758",
             "Decimus Burton's clubhouse of 1830 is named after Athena, whose statue stands over the door. Its "
             "frieze copies the Panathenaic procession from the Parthenon.",
             "en:Athenaeum Club, London",
             ("statue of the classical goddess of wisdom, Athena",
              "depicting the Panathenaic procession, a copy of the marbles from the Parthenon in Athens"),
             "1225842"),
        ],
    ),
    "commonwealth": (
        "Australia, New Zealand and Canada",
        "The dominions built grand high commissions in the West End between 1918 and 1963; Australians and "
        "New Zealanders also left their mark on London's cricket grounds, hotels and colleges.",
        [
            ("Australia House", "Q38166787",
             "Begun in 1913 and opened by George V in 1918, with marbles and timbers from every Australian state. It "
             "is usually the largest single polling station in Australian federal elections.",
             "en:High Commission of Australia, London",
             ("construction on the building by the Dove Brothers commenced in 1913", "opened by King George V",
              "3 August 1918", "Buchan marble from Victoria",
              "single largest polling station in Australian federal elections"),
             "1357166"),
            ("New Zealand House", "Q27081857",
             "Robert Matthew's tower on the site of the bombed Carlton Hotel, opened by Elizabeth II in 1963, was a "
             "break from the stone palaces of the other Commonwealth missions.",
             "en:High Commission of New Zealand, London",
             ("previously occupied by the Carlton Hotel, destroyed by a bomb during the Blitz",
              "designed by Sir Robert Matthew", "opened by Queen Elizabeth II in 1963"),
             "1242616"),
            ("Canada House", "Q195905",
             "Smirke's Union Club of 1824-27, bought by Canada in 1923 and opened by George V as the High "
             "Commission on 29 June 1925.",
             "en:Canada House",
             ("built between 1824 and 1827 to designs by Sir Robert Smirke", "acquired the Union Club in 1923",
              "officially opened on 29 June 1925 by King George V"),
             "1217724"),
            ("One Canada Square", "Q503477",
             "Canary Wharf was developed by the Canadian company Olympia & York from 1988; its tower, finished in "
             "1991, was the UK's tallest building.",
             "en:Canary Wharf",
             ("sold to the Canadian company Olympia & York",
              "including One Canada Square, which became the UK's tallest building at the time"),
             None),
            ("The Oval", "Q1155836",
             "England and Australia played the first Test in England here in 1880. Australia's win here in 1882 "
             "prompted the mock obituary that created the Ashes.",
             "en:The Oval",
             ("the first Test match in England was played at The Oval in 1880 between England and Australia",
              "In 1882, Australia won the Test by seven runs within two days", "creation of the Ashes trophy"),
             None),
            ("Savoy Hotel", "Q746639",
             "Escoffier created the pêche Melba here in 1893 for the Australian singer Nellie Melba, and Melba "
             "toast in 1897.",
             "en:Savoy Hotel",
             ("he invented the pêche Melba in honour of the Australian singer Nellie Melba, and in 1897, Melba toast",),
             "1236709"),
            ("Garden Museum (St Mary-at-Lambeth)", "Q15221398",
             "William Bligh of the Bounty, later Governor of New South Wales, was buried here in 1817; the church is "
             "now the Garden Museum.",
             "en:William Bligh",
             ("Governor of New South Wales", "Mary's, Lambeth (this church is now the Garden Museum)"),
             None),
            ("Euston station", "Q800751",
             "A statue of Matthew Flinders, who charted Australia, was unveiled here in 2014; his grave was found "
             "behind the station in 2019 during HS2 works.",
             "en:Euston railway station",
             ("a statue of navigator and cartographer Matthew Flinders", "charted Australia",
              "in 2019 was found behind the station during excavation work for the HS2 line"),
             None),
            ("Queen's College, 43-47 Harley Street", "Q99857958",
             "Katherine Mansfield came from Wellington in 1903 to study here with her sisters.",
             "en:Katherine Mansfield",
             ("She moved to London in 1903, where she attended Queen's College with her sisters", "Wellington"),
             "1066671"),
        ],
    ),
    "middleeast": (
        "The Middle East and the Muslim world",
        "Embassies of Arab states, Iran and Turkey cluster in Mayfair, Belgravia and Knightsbridge, while mosques "
        "from Regent's Park to Hackney serve London's Muslim communities.",
        [
            ("London Central Mosque", "Q1811339",
             "George VI gave the site in exchange for land in Cairo for an Anglican cathedral, and opened the "
             "Islamic Cultural Centre in 1944. Frederick Gibberd's mosque, partly funded by Saudi Arabia, followed "
             "in 1977.",
             "en:London Central Mosque",
             ("donation of land in Cairo by King Farouk of Egypt and Sudan", "officially opened by King George VI in 1944",
              "designed by Sir Frederick Gibberd, completed in 1977", "King Faisal Bin Abdul Aziz Al-Saud of Saudi Arabia"),
             "1452906"),
            ("Ismaili Centre", "Q6084925",
             "Hugh Casson's centre for the Ismaili Muslims in South Kensington, opened in 1985 by Margaret Thatcher "
             "with the Aga Khan.",
             "en:Ismaili Centre, London",
             ("by then Prime Minister Margaret Thatcher, in the presence of His Highness the Aga Khan",
              "Sir Hugh Casson, eventually designed the Ismaili Centre"),
             None),
            ("Finsbury Park Mosque", "Q1328033",
             "The five-storey mosque opened in 1994 with funds from King Fahd of Saudi Arabia. After the 2017 van "
             "attack on worshippers nearby it began an annual street iftar.",
             "en:Finsbury Park Mosque",
             ("In 1994, a new five-storey mosque building was officially opened",
              "King Fahd of Saudi Arabia who had contributed funds for the building", "Street Iftar"),
             None),
            ("Shacklewell Lane Mosque", "Q7460188",
             "Founded by Turkish Cypriots in 1977 in the former New Dalston Synagogue, it was the first Turkish "
             "mosque in Britain.",
             "en:Shacklewell Lane Mosque",
             ("the first ever Turkish mosque in the United Kingdom", "New Dalston Synagogue"),
             None),
            ("Suleymaniye Mosque", "Q2381974",
             "An Ottoman-style mosque on Kingsland Road for Hackney's Turkish-speaking community, opened in 1999. "
             "Its 66-metre minaret is the tallest in the UK.",
             "en:Suleymaniye Mosque (London)",
             ("opened to the public in October 1999", "The minaret reaches a height of 66 metres",
              "Turkish speaking community"),
             None),
            ("Aziziye Mosque", "Q793894",
             "The Apollo Picture House of 1913 in Stoke Newington, converted into a Turkish mosque from 1983.",
             "en:Aziziye Mosque (London)",
             ("Apollo Picture House", "UK Turkish Islamic Association", "conversion began in 1983"),
             None),
            ("14-25 Princes Gate (Iranian Embassy)", "Q141712936",
             "Six gunmen held the Iranian embassy at no. 16 from 30 April to 5 May 1980 until the SAS stormed it. "
             "The fire-damaged embassy reopened in 1993.",
             "en:Iranian Embassy siege",
             ("from 30 April to 5 May 1980", "Operation Nimrod", "the embassy building did not reopen until 1993"),
             "1265482"),
            ("5 St James's Square", "Q17550355",
             "A townhouse of 1748-51 that in 1984 was the Libyan People's Bureau, from which the shots that killed "
             "WPC Yvonne Fletcher were fired.",
             "en:5, St James's Square",
             ("built 1748–1751", "Libyan Peoples' Bureau", "murder of Yvonne Fletcher"),
             "1264938"),
            ("Crewe House", "Q17549509",
             "A detached Georgian mansion of 1730 in Mayfair, now the Embassy of Saudi Arabia.",
             "en:Embassy of Saudi Arabia, London",
             ("The embassy is situated in Crewe House", "Edward Shepherd in 1730"),
             "1066942"),
            ("38-48 Belgrave Square", "Q17527417",
             "The Ottoman Empire opened an embassy in London in 1793; its successor, the Turkish embassy, has had "
             "its chancellery at no. 43 since 1954.",
             "en:Embassy of Turkey, London",
             ("embassy of the Ottoman Empire in London dating from 1793",
              "1954: The embassy chancellery moves to 43 Belgrave Square"),
             "1292022"),
            ("75 South Audley Street (Bute House)", "Q27081560",
             "The residence of the Egyptian ambassador; its first Egyptian occupant was Aziz Ezzat Pasha.",
             "en:Embassy of Egypt, London",
             ("75 South Audley Street", "Aziz Ezzat Pasha"),
             "1236476"),
            ("Harrods", "Q332474",
             "Bought in 1985 by the Egyptian Fayed brothers, the store was sold in 2010 to the Qatar Investment "
             "Authority, Qatar's sovereign wealth fund.",
             "en:Harrods",
             ("acquired by the Fayed brothers",
              "sold to the Qatar Investment Authority, the sovereign wealth fund of Qatar, in 2010"),
             "1294346"),
        ],
    ),
}
