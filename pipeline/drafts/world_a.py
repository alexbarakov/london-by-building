"""DRAFT context layer 'The world in London', part A: Russia, India, China, Japan, France, Germany, Italy.

Same entry format as pipeline/curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or
None, group), where group is the country key. GROUPS = {country_key: (label, intro_sentence, [entries])}.

Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia article (API
prop=extracts, explaintext=1, redirects=1); checks were run on 2026-10-15. Each QID was read from Special:EntityData:
it has P625, and that point falls inside one of the nine borough polygons in data/raw/boundary.json (a polygon test,
not nearest postcode). NHLE numbers are copied from P1216; None means the item has no P1216. Where the building's own
article does not carry the story, the entry cites the article about the street, person or institution that does, and
the QID is the building item (often an NHLE-import item without an article of its own).

COUNTS: russia 14, india 15, china 10, japan 6, france 18, germany 20, italy 14 (97 entries).

Duplicates with other layers (kept because the story here is about the country, not the theme of the other layer):
- curated.py 'exiles': Marx Memorial Library (Lenin, Iskra), Kingsley Hall (Gandhi), Caxton Hall (Udham Singh),
  St Peter's Italian Church (Italian community). The exiles layer tells the same facts; pick one home for each before
  publishing, or keep both if the map tolerates one building in two layers.
- curated.py 'housing': Bevin Court (Lenin's home site). 'modern': Isokon Flats (Bauhaus emigres).
  'music': Handel Hendrix House. 'railways': Cannon Street station (Steelyard). 'secrets': Michelin House,
  Brompton Oratory (here for its Italian Baroque apostles).
- drafts/blitz.py: St Boniface's German Church, Notre Dame de France.
- drafts/world_b.py (written in parallel; same building, different country): Caxton Hall (there the 1900
  Pan-African Conference), Savoy Theatre (Paul Robeson), Savoy Hotel (peche Melba, Australia), Lancaster House
  (Chopin, Poland), Royal Opera House (Callas, Greece), 38-48 Belgrave Square (there No. 43, the Turkish embassy;
  here No. 39, the Italian Cultural Institute). Fine for a layer grouped by country, but the map will show one
  footprint with two stories; decide whether to merge them into one popup.
- Inside this file: 26-28 Dean Street is used once (germany, Marx) and also carries Quo Vadis, founded by the Italian
  Peppino Leoni; Notre Dame de France (france) mentions Boris Anrep's mosaic, and Anrep also appears under russia.

Dropped during research:
- Outside the nine boroughs: Deptford/Sayes Court (Peter the Great, Lewisham), India House at 65 Cromwell Avenue,
  Highgate (Savarkar; Haringey), Krishna Menon's house (Haringey), Kropotkin's homes (Harrow, Bromley), Anna Pavlova's
  Ivy House (Barnet), Natsume Soseki's lodgings at 81 The Chase are in Lambeth but have no Wikidata item.
- Demolished or no building left: Peter the Great's lodging at 21 Norfolk Street; York House Watergate (where he
  landed) has no Wikidata item found; Chesham House (Russian embassy to 1927); Lenin's 30 Holford Square (Bevin Court
  used instead); Hindoostane Coffee House (1810, 34 George Street, plaque only); Westminster Palace Hotel (India
  Office 1860-67, item typed as destroyed building); Strangers' Home for Asiatics, Limehouse (no evidence the
  building survives); Japanese Village, Knightsbridge (Humphreys' Hall burnt 1885); Steelyard (site only, Cannon
  Street used); Spaghetti House, Knightsbridge (block redeveloped 2015); Wagamama's first site (closed 2016).
- No usable Wikidata building item: 4 Carlton Gardens (de Gaulle's Free French HQ: no item; Carlton Gardens 1-3 have
  items, 4 does not), Ambedkar House (10 King Henry's Road), Sun Yat-sen's 4 Gray's Inn Place, Lao She's 31 St
  James's Gardens (items exist only for other number ranges), Mazzini's school at 5 Greville Street and home at
  183 Gower Street, 8 Royal College Street (Rimbaud and Verlaine), Engels's 122 Regent's Park Road, Tower House
  Fieldgate Street (Stalin), Mazzini Garibaldi Club, Goethe-Institut (item has no en article), Embassy of Germany
  (institution item without coordinates), Embassy of Russia (institution without coordinates; 6-7 KPG used).
- Institution items without NHLE, not used: University College London (Choshu Five, Soseki, Gandhi; Q193196 has no
  building item; the listed Chemistry Laboratory is a 1910s building, not the one they studied in), Inner Temple and
  Lincoln's Inn (Gandhi, Nehru, Jinnah), London School of Economics (Ambedkar), Lord's (India's 1983 World Cup win;
  the Lord's Pavilion article does not tell it).
- Weak or wrong-country ties: Crown Tavern, Clerkenwell Green (Lenin/Stalin legend; Q26536096 coordinate is in
  Yorkshire); Hong Kong Economic and Trade Office (coordinate is in Mayfair, the office is in Bedford Square); Taipei
  Representative Office (left out of the China group on purpose); Carlo Gatti's ice warehouse (London Canal Museum),
  Gatti's Adelphi and Charing Cross arches (Gatti was Swiss, from Ticino; could go to a Switzerland group);
  Royal Exchange (Reuter founded his agency there, but the article does not say he was German-born); Hanover Lodge
  (a third Russian-owner mansion, cut for balance); Royal Opera House for Nureyev (not in its article); Palace
  Theatre for Pavlova (article does not say Russian); Colnaghi (gallery firm, moved premises);
  St Anne and St Agnes (Lutheran use was Estonian/Latvian); Waterloo station (Battle of Waterloo, Eurostar to Paris
  1994-2007; already in drafts/blitz.py); St Pancras (Eurostar; already in 'railways'); Apsley House (Napoleon
  statue; in 'power', and the article does not tell it).

Doubts to check before publishing:
- Institution-type items that carry the building's own coordinates but no NHLE number: Pushkin House, Veeraswamy,
  Radha Krishna Temple, Tamarind, Lee Ho Fook (closed; building at 15-16 Gerrard Street stands), A. Wong, Hakkasan
  (a restaurant-chain item placed at Hanway Place), Kai Mayfair, Shaolin Temple UK, Japan House London, Budokwai
  (club; point is the present dojo), Tokyo Diner, Lycee Francais, The French House, Maison Bertaux, Hotel Cafe Royal,
  Madame Tussauds, Tyburn Nuns (congregation item placed at Tyburn Convent), Warburg Institute, Wiener Holocaust
  Library, German Historical Institute, Belsize Square Synagogue, Deutsche Evangelische Christuskirche, Estorick
  Collection, Royal Mint Court (architectural ensemble; the China embassy plan is a purchase, not a
  built embassy), New Court (building complex), 8 Canada Square, Athlone
  House, The Biltmore Mayfair, Orange Street Congregational Church, Cannon Street station. If the map needs strict
  building items with NHLE, these are the first to re-check.
- Group items covering several houses: 34-52 Portland Place (Q17549821) stands in for No. 49, the Chinese legation;
  38-48 Belgrave Square (Q17527417) for No. 39, the Italian Cultural Institute; 28-32 Welbeck Street for the chapel
  behind No. 32; 1-9 Carlton House Terrace for Nos 7-9 (Prussia House); 14-27 Lisle Street for Chinatown's first
  restaurants; 45 and 46 Berkeley Square for Clive's No. 45. The map will highlight whichever footprint the point
  falls on.
- Address not in the cited article: 41 Craven Street (the India Club article says only "Craven Street"; the NHLE
  list entry 1220948 gives No. 41, 1951-64); 101-104 Piccadilly (the embassy article says "a large Victorian building
  on Piccadilly opposite Green Park"; the address is the embassy's published one); Hamburg Lutheran Church (only one
  sentence, in the Christuskirche article); Italian Hospital (one sentence, in the Queen Square article).
- Marconi House and Bar Italia are Italian through their founders (Marconi; the Polledri family); the Marconi House
  article itself does not say Marconi was Italian.
- The Lubetkin link (Penguin Pool, Bevin Court) rests on "an emigre from Russia" in the Penguin Pool article; he was
  born in Tiflis, now Georgia.
- Oligarch purchases (Witanhurst, Athlone House) are ownership facts from the articles; keep or cut for tone.
- India group includes colonial-era sites (East India Club, Oriental Club, Clive's house, the India Office in the
  Foreign Office building); the label says "India" but these are about British rule in India.
- Japan is thin (6). Candidates that need a building item first: UCL main building (Choshu Five, 1863), 103 Gower
  Street (two of the Five lodged there), 81 The Chase, Clapham (Soseki).
"""

GROUPS = {
    "russia": (
        "Russia",
        "Russian exiles, diplomats and artists have left churches, embassies and a revolutionary newspaper office "
        "across inner London.",
        [
            ("Dormition Cathedral", "Q4478059",
             "An Anglican church of 1848–1849 in Ennismore Gardens, let to the Russian Orthodox Church and consecrated "
             "in December 1956. It is the cathedral of the Diocese of Sourozh; Metropolitan Anthony (Bloom) led it from "
             "1956 to 2002.",
             "en:Dormition Cathedral, London",
             ("1848–1849", "December 1956", "Diocese of Sourozh", "Metropolitan Anthony (Bloom) (1956–2002)"),
             "1066842", "russia"),
            ("13 Kensington Palace Gardens", "Q16149797",
             "Harrington House was offered to the British Crown in 1930 for use as the Soviet Embassy, after relations "
             "with the USSR were restored in 1929. It is now the official residence of the Russian Ambassador.",
             "en:13 Kensington Palace Gardens",
             ("1930 for use as the Soviet Embassy", "1929", "official residence of the Russian Ambassador"),
             "1266971", "russia"),
            ("6 and 7 Kensington Palace Gardens", "Q27080884",
             "These houses hold the Russian Embassy's chancery. The Russian Empire's embassy had been at Chesham Place "
             "in Belgravia; after the break of 1927–1929 the Soviet government moved to Kensington Palace Gardens.",
             "en:Embassy of Russia, London",
             ("6-7 Kensington Palace Gardens", "Chesham Place", "1927–1929"),
             "1223939", "russia"),
            ("28–32 Welbeck Street", "Q26319113",
             "Behind No. 32 is a Russian Orthodox chapel, on the site of the early-19th-century residence of the "
             "Russian Embassy Chaplain. The chapel was rebuilt in 1864 and has a fine iconostasis.",
             "en:Welbeck Street",
             ("Russian Orthodox Chapel at 32 Welbeck Street", "Russian Embassy Chaplain", "rebuilt in 1864",
              "iconostasis"),
             "1066114", "russia"),
            ("Pushkin House", "Q7382027",
             "Founded in 1954 by émigré Russians led by Maria Kullmann, it is the UK's oldest independent Russian "
             "cultural centre. In 2006 it moved to a listed 1740s house in Bloomsbury Square.",
             "en:Pushkin House, London",
             ("1954", "Maria Mikhailovna Kullmann", "oldest independent Russian cultural centre", "until 2006",
              "5, 5a and 6 Bloomsbury Square", "1740s"),
             None, "russia"),
            ("Marx Memorial Library", "Q93844",
             "In 1902–1903 the exiled Lenin worked in this former charity school, publishing seventeen issues of his "
             "newspaper Iskra from inside the building.",
             "en:Marx Memorial Library",
             ("1902–1903", "Vladimir Lenin", "seventeen issues", "Iskra"),
             "1279541", "russia"),
            ("Bevin Court", "Q4899667",
             "Lubetkin's block stands on the site of Lenin's home of 1902–03, where he edited Iskra. It was first to "
             "be called Lenin Court and to take in Lubetkin's Lenin memorial from Holford Square.",
             "en:Bevin Court",
             ("1902–03 home of Lenin", "Iskra", "Lenin Court", "memorial to Lenin", "Holford Square"),
             "1246687", "russia"),
            ("Orsett House", "Q26519750",
             "The Russian political thinker Alexander Herzen lived in this stucco villa from 1860 to 1863; a blue "
             "plaque marks the house.",
             "en:Orsett Terrace",
             ("Orsett House", "Alexander Herzen", "1860 to 1863", "blue plaque"),
             "1225675", "russia"),
            ("Penguin Pool, London Zoo", "Q11350844",
             "Berthold Lubetkin, an émigré from Russia who came to Britain in 1931, designed the pool with the Tecton "
             "Group and the engineer Ove Arup. It was built in 1934.",
             "en:Penguin Pool, London Zoo",
             ("an émigré from Russia who came to Britain in 1931", "Tecton Group", "Ove Arup", "Constructed in 1934"),
             "1225665", "russia"),
            ("National Gallery", "Q180788",
             "Boris Anrep, a Russian mosaicist born in Saint Petersburg, laid the mosaics of the entrance-hall "
             "landings between 1928 and 1952; Greta Garbo appears as the muse Melpomene.",
             "en:Boris Anrep",
             ("Russian artist", "born in 1883 in Saint Petersburg", "National Gallery mosaics (1928–1952)",
              "Melpomene is Greta Garbo"),
             "1066236", "russia"),
            ("Westminster Cathedral", "Q739364",
             "Boris Anrep worked on the cathedral's mosaics for half a century, from the crypt in 1914 to a last "
             "scheme of 1956–63.",
             "en:Boris Anrep",
             ("Russian artist", "1914 Westminster Cathedral crypt", "1956–63 Westminster Cathedral"),
             "1066500", "russia"),
            ("The Biltmore Mayfair", "Q13529145",
             "In 2006, when this Grosvenor Square hotel was the Millennium Hotel London Mayfair, its Pine Bar was the "
             "site of the poisoning of Alexander Litvinenko.",
             "en:The Biltmore Mayfair",
             ("44 Grosvenor Square", "Millennium Hotel London Mayfair", "Pine Bar",
              "poisoning of Alexander Litvinenko in 2006"),
             None, "russia"),
            ("Witanhurst", "Q15979614",
             "The Highgate mansion was bought in 2008 for £50 million, through an offshore company, by the family of "
             "the Russian billionaire Andrey Guryev, and then substantially refurbished.",
             "en:Witanhurst",
             ("Andrey Guryev", "£50 million in 2008", "Safran Holdings", "substantial refurbishment"),
             "1379026", "russia"),
            ("Athlone House", "Q4815607",
             "In 2016 the Russian businessman Mikhail Fridman bought the house for £65 million and restored it as a "
             "family home.",
             "en:Athlone House",
             ("Mikhail Fridman", "£65 million", "modern family home"),
             None, "russia"),
        ]),
    "india": (
        "India",
        "From the East India Company's clubs to the High Commission, a students' hostel and London's oldest Indian "
        "restaurant, India's ties to London are written into its buildings.",
        [
            ("India House", "Q14996965",
             "Designed by Sir Herbert Baker and completed in 1930, it houses the High Commission of India. George V "
             "inaugurated it on 8 July 1930.",
             "en:India House, London",
             ("Sir Herbert Baker", "completed in 1930", "8 July 1930", "High Commission of India"),
             "1066491", "india"),
            ("Indian Students' Union and Hostel", "Q6021671",
             "The Indian National Council of YMCAs founded the hostel in 1920 for Indian students in London. It moved "
             "to this Fitzroy Square building after its Gower Street home was damaged in the Second World War.",
             "en:YMCA Indian Students' Union and Hostel",
             ("1920", "Indian National Council of YMCAs", "Fitzroy Square", "Gower Street", "World War Two"),
             "1113000", "india"),
            ("Veeraswamy", "Q7918202",
             "Edward Palmer, a retired officer of the British Indian Army, opened the restaurant at 99–101 Regent "
             "Street in 1926. By 2006 it was the oldest Indian restaurant in the United Kingdom.",
             "en:Veeraswamy",
             ("Edward Palmer", "British Indian Army", "99–101 Regent Street", "1926",
              "oldest Indian restaurant in the United Kingdom"),
             None, "india"),
            ("41 Craven Street", "Q27080724",
             "The India Club, set up in 1951 by members of the India League under Krishna Menon, met first in Craven "
             "Street; Jawaharlal Nehru was a founding member. It moved to the Strand in 1964 and closed in 2023.",
             "en:India Club, London",
             ("1951", "India League", "Krishna Menon", "Jawaharlal Nehru", "Craven Street", "moving in 1964",
              "September 2023"),
             "1220948", "india"),
            ("Oriental Club", "Q14997016",
             "The Duke of Wellington and Sir John Malcolm founded the club in 1824, when British India was run by the "
             "East India Company. It moved into Stratford House, a Robert Adam building, in 1962.",
             "en:Oriental Club",
             ("1824", "Sir John Malcolm", "East India Company", "Early in 1962", "Robert Adam"),
             "1237107", "india"),
            ("East India Club", "Q615521",
             "Founded in 1849 for officers of the East India Company, the club has its house at 16 St James's Square.",
             "en:East India Club",
             ("founded in 1849", "officers of the East India Company", "16, St James's Square"),
             "1235827", "india"),
            ("8 South Audley Street", "Q27081553",
             "Since 1992 this Mayfair house has held the Nehru Centre, an Indian cultural centre named after the first "
             "prime minister. Its first director was Gopalkrishna Gandhi.",
             "en:Nehru Centre, London",
             ("8 South Audley Street", "founded in 1992", "Gopalkrishna Gandhi (1992–1997)"),
             "1236395", "india"),
            ("Kingsley Hall", "Q6413308",
             "Gandhi lived here for 12 weeks in 1931 while he attended the Round Table Conference on India's future. "
             "The building now houses the Gandhi Foundation.",
             "en:Kingsley Hall",
             ("12 weeks", "1931", "Round Table Conference", "Gandhi Foundation"),
             "1357884", "india"),
            ("Caxton Hall", "Q5055269",
             "In 1940 Udham Singh, a survivor of the 1919 Jallianwala Bagh massacre, shot Michael O'Dwyer, the former "
             "governor of the Punjab, at a meeting in the hall.",
             "en:Caxton Hall",
             ("In 1940", "Udham Singh", "Michael O'Dwyer", "1919 Jallianwala Bagh massacre", "Punjab"),
             "1357266", "india"),
            ("Radha Krishna Temple", "Q17334185",
             "The UK centre of ISKCON, the Hare Krishna movement, moved here off Soho Square in 1979. Its devotees' "
             "single 'Hare Krishna Mantra', recorded with George Harrison, was an international hit in 1969.",
             "en:Radha Krishna Temple",
             ("International Society for Krishna Consciousness", "1979", "Soho Square", "Hare Krishna Mantra",
              "George Harrison"),
             None, "india"),
            ("National Liberal Club", "Q1807425",
             "By the late 1880s the club had a large membership in India and among Indians in London. The independence "
             "leader Gopal Krishna Gokhale was a member, and Gandhi visited as his guest.",
             "en:National Liberal Club",
             ("late 1880s", "Indian nationals resident in London", "Gopal Krishna Gokhale", "Gokhale's guest"),
             "1066072", "india"),
            ("Liberty", "Q3237793",
             "Arthur Liberty's shop specialised in imported Indian silks. In November 1885 he brought forty-two "
             "villagers from India to stage a living village of Indian artisans.",
             "en:Liberty (department store)",
             ("Indian silks", "November 1885", "forty-two villagers from India"),
             "1357064", "india"),
            ("45 and 46 Berkeley Square", "Q17527079",
             "Robert Clive, 'Clive of India', bought No. 45 in 1761 and died there in 1774.",
             "en:Berkeley Square",
             ("Robert Clive of India", "No.45 in 1761", "died in 1774"),
             "1218401", "india"),
            ("Foreign Office building", "Q58212077",
             "George Gilbert Scott's building, finished in 1868, was built for four government departments, one of "
             "them the India Office. The India Office was merged into the Commonwealth Relations Office in 1947.",
             "en:Foreign, Commonwealth and Development Office",
             ("George Gilbert Scott", "finished in 1868", "the India Office", "the India Office in 1947"),
             "1066102", "india"),
            ("Tamarind", "Q28178875",
             "Opened in Mayfair in 1995, it was one of the first Indian restaurants in London to win a Michelin star, "
             "in 2001 under the chef Atul Kochhar.",
             "en:Tamarind (restaurant)",
             ("opened in 1995", "first Indian restaurants in London to receive a Michelin star", "2001",
              "Atul Kochhar"),
             None, "india"),
        ]),
    "china": (
        "China",
        "China's first legation abroad, the Chinatown that moved from Limehouse to Soho, and a bank born in Hong "
        "Kong all have buildings in inner London.",
        [
            ("34–52 Portland Place", "Q17549821",
             "No. 49, leased in 1877, became China's first permanent diplomatic mission abroad. The Qing legation "
             "held the revolutionary Sun Yat-sen here until his friend James Cantlie got him released.",
             "en:Embassy of China, London",
             ("49 Portland Place", "1877", "first permanent overseas diplomatic mission", "Sun Yat-sen",
              "James Cantlie"),
             "1227025", "china"),
            ("Royal Mint Court", "Q140783459",
             "The Royal Mint worked here from 1809 until 1967. In May 2018 the site was sold to China for a new "
             "London embassy.",
             "en:Royal Mint Court",
             ("1809 until 1967", "May 2018", "sold to China", "new London embassy"),
             None, "china"),
            ("Wong Kei", "Q839257",
             "Once called 'the rudest restaurant in London', it seats about 500 at 41–43 Wardour Street, a building "
             "put up in 1904–05 for the theatrical wig-maker Willy Clarkson.",
             "en:Wong Kei",
             ("rudest restaurant in London", "around 500 diners", "41–43 Wardour Street", "Willy Clarkson", "1904",
              "1905"),
             "1357341", "china"),
            ("Lee Ho Fook", "Q104841098",
             "At 15–16 Gerrard Street, it became in 1974 the first Chinese restaurant in the UK with a Michelin star. "
             "Warren Zevon named it in 'Werewolves of London' (1978).",
             "en:Lee Ho Fook",
             ("15–16 Gerrard Street", "In 1974", "first Chinese restaurant in the United Kingdom to be awarded a "
              "Michelin Star", "Werewolves of London", "Warren Zevon"),
             None, "china"),
            ("14–27 Lisle Street", "Q27080776",
             "Lisle Street, parallel to Gerrard Street, probably had Soho's first Chinese restaurants, among them the "
             "Kowloon. The present Chinatown was recognised as such by the 1970s, after the first one in Limehouse "
             "had faded.",
             "en:Chinatown, London",
             ("first Chinese restaurants opened in Lisle Street", "Kowloon Restaurant", "by the 1970s",
              "Limehouse"),
             "1222102", "china"),
            ("A. Wong", "Q110442435",
             "In January 2021 Andrew Wong's Pimlico restaurant became the first Chinese restaurant outside Asia to "
             "hold two Michelin stars.",
             "en:A. Wong",
             ("Pimlico", "January 2021", "first Chinese restaurant outside Asia to achieve two Michelin stars"),
             None, "china"),
            ("Hakkasan", "Q5640540",
             "Alan Yau opened the first Hakkasan in Hanway Place in April 2001. In 2003 it became one of the first "
             "Chinese restaurants in London to win a Michelin star.",
             "en:Hakkasan",
             ("April 2001 at Hanway Place", "Alan Yau", "In 2003",
              "one of the first Chinese restaurants in London to win a Michelin Star"),
             None, "china"),
            ("Kai Mayfair", "Q6347452",
             "Opened in 1993 at 65 South Audley Street, it served Chinese cooking from the Nanyang region and held a "
             "Michelin star from 2009 until 2025.",
             "en:Kai Mayfair",
             ("65 South Audley Street", "1993", "Nanyang region", "awarded it one star", "2025 Michelin Guide"),
             None, "china"),
            ("8 Canada Square", "Q572887",
             "The global headquarters of HSBC, a bank with Hong Kong roots. Norman Foster got the commission partly "
             "because he had designed HSBC's head office in Hong Kong; the tower opened in 2003.",
             "en:8 Canada Square",
             ("global headquarters of HSBC", "Norman Foster", "head office in Hong Kong", "2 April 2003"),
             None, "china"),
            ("Shaolin Temple UK", "Q7489179",
             "Founded in 2000 by the Shaolin monk Shi Yanzi, it is an official emissary of the Shaolin Temple in "
             "Henan, teaching Gong Fu, Qigong and Chan meditation.",
             "en:Shaolin Temple UK",
             ("founded in 2000", "Shi Yanzi", "official emissary", "Henan Province", "Qigong"),
             None, "china"),
        ]),
    "japan": (
        "Japan",
        "Japanese diplomats, bankers, martial artists and cooks have made a home in London since the opera that "
        "first put Japan on a London stage.",
        [
            ("101–104 Piccadilly", "Q27083212",
             "The Embassy of Japan occupies this Victorian building opposite Green Park. It was built for the Junior "
             "Constitutional Club, the first building in London with its exterior entirely clad in marble.",
             "en:Embassy of Japan, London",
             ("Piccadilly opposite Green Park", "Junior Constitutional Club",
              "first building in London to have its exterior entirely clad in marble"),
             "1265714", "japan"),
            ("Japan House London", "Q50359562",
             "A cultural centre on Kensington High Street run under a programme of Japan's Ministry of Foreign "
             "Affairs. It opened in June 2018, after Japan Houses in Los Angeles and São Paulo.",
             "en:Japan House London",
             ("Kensington High Street", "Ministry of Foreign Affairs", "June 2018", "Japan House Los Angeles"),
             None, "japan"),
            ("Savoy Theatre", "Q2165797",
             "Gilbert and Sullivan's The Mikado, set in Japan, opened here on 14 March 1885 and ran for 672 "
             "performances, at a time when a Japanese Village was on show in Knightsbridge.",
             "en:The Mikado",
             ("14 March 1885", "ran at the Savoy Theatre for 672 performances", "Japanese Village"),
             "1236724", "japan"),
            ("Bracken House", "Q17549117",
             "The former Financial Times building was redeveloped by Japan's Obayashi Corporation between 1988 and "
             "1992 as the European head office of the Industrial Bank of Japan.",
             "en:Bracken House, London",
             ("Obayashi Corporation between 1988 and 1992", "Industrial Bank of Japan"),
             "1262582", "japan"),
            ("Budokwai", "Q3646473",
             "Gunji Koizumi founded the club in 1918 to teach judo, kendo and other Japanese arts. It is the oldest "
             "Japanese martial arts club in Europe and was its first judo club.",
             "en:Budokwai",
             ("1918", "Gunji Koizumi", "oldest Japanese martial arts club in Europe", "first judo club in Europe"),
             None, "japan"),
            ("Tokyo Diner", "Q14955161",
             "Richard Hills, who had learned Japanese, turned a vacant launderette on the corner of Newport Place and "
             "Lisle Street into this Japanese diner in December 1992.",
             "en:Tokyo Diner",
             ("Newport Place and Lisle Street", "launderette", "December 1992"),
             None, "japan"),
        ]),
    "france": (
        "France",
        "Huguenot refugees, émigré priests, Free French soldiers and French chefs, cooks and companies have all "
        "left buildings in inner London.",
        [
            ("French Protestant Church of London", "Q3586104",
             "Founded by a charter of Edward VI on 24 July 1550, it is the last Huguenot church in London. Aston Webb "
             "built its Soho Square church in 1891–1893.",
             "en:French Protestant Church of London",
             ("24 July 1550", "Edward VI", "last remaining Huguenot church of London", "Aston Webb", "1891–1893"),
             "1236283", "france"),
            ("Notre Dame de France", "Q20713125",
             "The Marist Fathers turned a circular building off Leicester Square into a church for the French "
             "community in 1865. After bomb damage in 1940 it was rebuilt; Jean Cocteau painted the Lady Chapel murals "
             "in 1960.",
             "en:Notre Dame de France",
             ("Marist Fathers", "25 March 1865", "circular building off Leicester Square", "murals by Jean Cocteau "
              "(1960)"),
             "1376623", "france"),
            ("Orange Street Congregational Church", "Q140165788",
             "Founded in 1693 as a French Reformed (Huguenot) chapel near Leicester Fields by refugees from the "
             "Revocation of the Edict of Nantes. The Huguenot congregation gave up the building in 1776.",
             "en:Orange Street Congregational Church",
             ("Founded in 1693 as a French Reformed (Huguenot) chapel", "Revocation of the Edict of Nantes", "1776"),
             None, "france"),
            ("St Mary's Church, Hampstead", "Q7594337",
             "The Abbé Jean-Jacques Morel, a refugee from the French Revolution, opened this chapel in Holly Place in "
             "August 1816. General de Gaulle was a parishioner during the Second World War.",
             "en:St Mary's Church, Hampstead",
             ("Jean-Jacques Morel", "refugee from the French Revolution", "August 1816",
              "General Charles de Gaulle"),
             "1379106", "france"),
            ("Lycée Français Charles de Gaulle", "Q3269062",
             "Founded in 1915 for refugee children of the First World War, the school's South Kensington buildings "
             "became offices for de Gaulle's Free French government in exile.",
             "en:Lycée Français Charles de Gaulle",
             ("1915", "World War I refugees", "Free French government in exile", "Cromwell Road"),
             None, "france"),
            ("The French Institute", "Q27081138",
             "The Institut français was founded in 1910 by Marie d'Orliac. Its listed building in Queensberry Place "
             "holds the Ciné Lumière cinema and a French library.",
             "en:Institut français du Royaume-Uni",
             ("Founded in 1910", "Marie d'Orliac", "Queensberry Place", "Ciné Lumière"),
             "1226079", "france"),
            ("The French House", "Q7735253",
             "Victor Berlemont bought the Dean Street pub in 1914 and his son Gaston ran it until 1989. Its shelves of "
             "Pernod and Suze gave it the name of a French auberge.",
             "en:The French House, Soho",
             ("49 Dean Street", "Victor Berlemont", "until his retirement in 1989", "French auberge", "Pernod"),
             None, "france"),
            ("Broadcasting House", "Q2914560",
             "On 18 June 1940 Charles de Gaulle's appeal to the French was broadcast over BBC radio from Broadcasting "
             "House. It is often seen as the start of the French Resistance.",
             "en:Appeal of 18 June",
             ("Broadcasting House", "beginning of the French Resistance", "10 pm BST"),
             "1265570", "france"),
            ("Michelin House", "Q6836880",
             "Built as the first permanent UK headquarters of the French tyre company Michelin, to a design by "
             "François Espinasse of Clermont-Ferrand. It opened on 20 January 1911.",
             "en:Michelin House",
             ("first permanent UK headquarters", "French multinational tyre company Michelin", "François Espinasse",
              "Clermont-Ferrand", "20 January 1911"),
             "1080656", "france"),
            ("Savoy Hotel", "Q746639",
             "César Ritz managed the hotel after it opened in 1889, with Auguste Escoffier as chef. Escoffier "
             "recruited French cooks and reorganised the kitchens.",
             "en:Savoy Hotel",
             ("6 August 1889", "César Ritz", "Auguste Escoffier", "Escoffier recruited French cooks"),
             "1236709", "france"),
            ("Sketch", "Q14955160",
             "In the mid-20th century 9 Conduit Street was Christian Dior's London atelier. Since 2003 it has housed "
             "Sketch, whose cooking is adapted from Pierre Gagnaire's Paris restaurant.",
             "en:Sketch (restaurant)",
             ("9 Conduit Street", "Christian Dior's London atelier", "2003", "Gagnaire"),
             "1219898", "france"),
            ("Maison Bertaux", "Q24890428",
             "Founded in 1871 at 28 Greek Street by a communard from Paris named Bertaux, it is the oldest pâtisserie "
             "in London, in what was then the heart of the French community.",
             "en:Maison Bertaux",
             ("1871", "French communard from Paris", "28 Greek Street", "oldest pâtisserie in London",
              "heart of the French community"),
             None, "france"),
            ("Hotel Café Royal", "Q5017262",
             "The Café Royal was set up in 1865 by Daniel Nicholas Thévenon, a French wine merchant who changed his "
             "name to Daniel Nicols.",
             "en:Café Royal",
             ("1865", "Daniel Nicholas Thévenon", "French wine merchant", "Daniel Nicols"),
             None, "france"),
            ("Madame Tussauds", "Q186309",
             "Marie Tussaud, a wax sculptor born in Strasbourg, founded the museum in London in 1835. Its galleries on "
             "Marylebone Road opened on 14 July 1884.",
             "en:Madame Tussauds",
             ("1835", "Marie Tussaud", "Strasbourg", "14 July 1884", "Marylebone Road"),
             None, "france"),
            ("St Pancras Old Church", "Q3495349",
             "Its churchyard was one of the few places in London where Catholics could be buried. Many French émigrés, "
             "especially priests who had fled the Revolution, lie here, as does the Chevalier d'Éon.",
             "en:St Pancras Old Church",
             ("French refugees (émigrés)", "especially priests", "fled the Revolution", "Chevalier d'Éon"),
             "1113246", "france"),
            ("Former French Protestant Hospital", "Q26263465",
             "The French Hospital, founded in 1718 for poor French Protestants, moved in 1865 into this building by "
             "Robert Lewis Roumieu, said to be modelled on the Château de Chambord.",
             "en:French Hospital (La Providence)",
             ("1718", "French Protestants", "Robert Lewis Roumieu", "opened in 1865", "Château de Chambord"),
             "1235554", "france"),
            ("Tyburn Convent", "Q1773594",
             "The Adorers of the Sacred Heart of Montmartre left Paris after the French law of 1901 on associations "
             "and moved in 1903 to this convent on Bayswater Road, near the site of the Tyburn gallows.",
             "en:Tyburn Nuns",
             ("Waldeck-Rousseau Law of Associations", "relocated the congregation to London in 1903",
              "Tyburn Convent in Bayswater Road"),
             None, "france"),
            ("Hertford House", "Q18462636",
             "Home of the Wallace Collection, whose main strength is 18th-century French art. It is among the largest "
             "collections of French 18th-century decorative art in the world.",
             "en:Wallace Collection",
             ("Hertford House", "18th-century French art",
              "largest, most important collections of French 18th-century decorative arts"),
             "1239252", "france"),
        ]),
    "germany": (
        "Germany",
        "Sugar refiners, gymnasts, courtiers, bankers and refugees from Nazi Germany built churches, a hospital and "
        "institutes across inner London.",
        [
            ("St George's German Lutheran Church", "Q15059607",
             "Founded in 1762, it served German Lutherans until 1995, many of them sugar refiners in Whitechapel's "
             "'Little Germany'. It is the oldest surviving German Lutheran church building in Britain.",
             "en:St George's German Lutheran Church",
             ("1762 until 1995", "sugar refiners", "Little Germany",
              "oldest surviving German Lutheran church building in the United Kingdom"),
             "1065325", "germany"),
            ("St George's German and English Schools", "Q27081802",
             "The church's English and German School was founded in 1805 and taught boys and girls in both languages. "
             "It closed in 1917 when its last German-speaking teacher was ordered to leave the country.",
             "en:St George's German Lutheran Church",
             ("English and German School which had been founded in 1805", "bi-lingual elementary education",
              "close in 1917"),
             "1242120", "germany"),
            ("St Boniface's German Church", "Q54006848",
             "London's German Catholic Mission, founded in 1809 for immigrants working in sugar refining, moved to "
             "Adler Street in 1862. Its church was destroyed in 1940 and replaced by a Modernist building.",
             "en:St Boniface's German Church, Whitechapel",
             ("founded in East London in 1809", "sugar refining", "Adler Street", "September 1940"),
             "1445649", "germany"),
            ("Deutsche Evangelische Christuskirche", "Q20711816",
             "Built in 1904–05 for the congregation of the German Chapel Royal, it has been called the most "
             "significant German church in London.",
             "en:Deutsche Evangelische Christuskirche",
             ("German Chapel Royal", "1904 to 1905", "most significant German church in London"),
             None, "germany"),
            ("Queen's Chapel", "Q7269945",
             "In 1718 the chapel was given over to the German courtiers who had come to England with George I, and it "
             "became known as the German Chapel.",
             "en:Queen's Chapel",
             ("In 1718", "German courtiers of George I", "The chapel was then called the German Chapel"),
             "1273605", "germany"),
            ("Savoy Chapel", "Q64636",
             "From 1694 the German Lutheran congregation of Westminster worshipped here, in the Marienkirche or "
             "German Church of St Mary-le-Savoy.",
             "en:Savoy Chapel",
             ("German Lutheran congregation of Westminster", "1694", "Marienkirche"),
             "1264731", "germany"),
            ("Hamburg Lutheran Church", "Q26555544",
             "A German Lutheran congregation that had met in the City until the 1860s later worshipped in this "
             "church beside the German Hospital in Dalston.",
             "en:Deutsche Evangelische Christuskirche",
             ("Hamburg Lutheran Church, alongside the German Hospital in Dalston", "until the 1860s"),
             "1264907", "germany"),
            ("German Hospital", "Q26529077",
             "Founded in 1845 to give free treatment to London's German-speaking community. Its German staff were "
             "interned in the Second World War, and the hospital closed in 1987.",
             "en:German Hospital, Dalston",
             ("established in 1845", "German-speaking community", "interned during the Second World War",
              "closed in 1987"),
             "1235777", "germany"),
            ("German Gymnasium", "Q5551117",
             "Built in 1864–65 for the German Gymnastics Society, founded in London in 1861 by Ernst Ravenstein. It is "
             "now a German-themed bar and restaurant.",
             "en:German Gymnasium, London",
             ("1864–65", "German Gymnastics Society", "1861", "Ernst Ravenstein", "German-themed bar and restaurant"),
             "1113243", "germany"),
            ("26–28 Dean Street", "Q86600116",
             "Karl Marx and his family lived in two small rooms at No. 28 from 1851 to 1856. The houses were listed "
             "Grade I for that reason; the Quo Vadis restaurant has been here since 1926.",
             "en:Quo Vadis (restaurant)",
             ("Karl Marx and his family lived in two small rooms", "between 1851 and 1856", "Grade I listed",
              "founded in 1926"),
             "1290584", "germany"),
            ("46 Grafton Terrace", "Q17542339",
             "Marx lived here from 1856. Jenny Marx called the eight-room house 'a truly princely dwelling' compared "
             "with the rooms they had left.",
             "en:Kentish Town",
             ("46 Grafton Terrace from 1856", "eight-room house", "A truly princely dwelling"),
             "1113066", "germany"),
            ("1–9 Carlton House Terrace", "Q17527061",
             "Nos 7–9, known as Prussia House, were the Prussian and then German Embassy until 1939. Ambassador "
             "Leopold von Hoesch's dog Giro is buried in the garden of No. 9.",
             "en:Carlton House Terrace",
             ("Prussia House", "until 1939", "Leopold von Hoesch", "Giro", "Albert Speer"),
             "1209780", "germany"),
            ("Handel Hendrix House", "Q2920095",
             "The German-born composer George Frideric Handel rented 25 Brook Street from 1723 until his death there "
             "in 1759, and wrote almost all his later works in the house.",
             "en:Handel Hendrix House",
             ("German-born", "25 Brook Street", "1723 until his death there in 1759"),
             "1066382", "germany"),
            ("Cannon Street station", "Q800615",
             "The station was built on the site of the Steelyard, the London base of the merchants of the Hanseatic "
             "League until 1598.",
             "en:Cannon Street station",
             ("Steelyard", "Hanseatic League", "1598"),
             None, "germany"),
            ("Isokon Flats", "Q3296317",
             "The Bauhaus émigrés Walter Gropius, Marcel Breuer and László Moholy-Nagy lived in these flats; a blue "
             "plaque to them went up in 2018.",
             "en:Isokon Flats",
             ("Bauhaus émigrés Walter Gropius, Marcel Breuer, and László Moholy-Nagy", "blue plaque was fixed in 2018"),
             "1379280", "germany"),
            ("Warburg Institute", "Q683095",
             "Aby Warburg's library left Hamburg for London in 1933, under the shadow of Nazism. It joined the "
             "University of London in 1944 and moved to its present building in 1958.",
             "en:Warburg Institute",
             ("Hamburg", "under the shadow of Nazism", "1944", "current home at the university in 1958"),
             None, "germany"),
            ("Wiener Holocaust Library", "Q2569007",
             "Alfred Wiener, a German Jew, started documenting Nazi persecution in 1933. His archive came to Britain "
             "after Kristallnacht and is now in Russell Square.",
             "en:Wiener Holocaust Library",
             ("German Jew", "1933", "Kristallnacht", "Russell Square"),
             None, "germany"),
            ("Belsize Square Synagogue", "Q15198326",
             "Founded in 1939 by refugees, mainly from Germany, it keeps the worship and music of German Liberal "
             "Judaism.",
             "en:Belsize Square Synagogue",
             ("founded in 1939 by refugees, mainly from Germany", "German Liberal Judaism"),
             None, "germany"),
            ("German Historical Institute London", "Q1205699",
             "Funded by the German government, the institute opened on 4 November 1976 at 17 Bloomsbury Square, with "
             "a public library of German history.",
             "en:German Historical Institute London",
             ("4 November 1976", "17 Bloomsbury Square", "German history"),
             None, "germany"),
            ("New Court", "Q77242291",
             "Nathan Mayer Rothschild, who had left Frankfurt, took a lease at New Court in 1809. The Rothschild bank "
             "is still on the site, in the fourth building at the same address.",
             "en:New Court",
             ("Frankfurt", "1809", "fourth incarnation of the Rothschild offices"),
             None, "germany"),
        ]),
    "italy": (
        "Italy",
        "Italian exiles, opera, painters, cafés and a hospital: inner London has kept the buildings of its "
        "Italian community since the 18th century.",
        [
            ("St Peter's Italian Church", "Q16900510",
             "Built for Italian immigrants with help from Giuseppe Mazzini and consecrated on 16 April 1863, it is the "
             "centre of Clerkenwell's Little Italy and its July procession.",
             "en:St Peter's Italian Church",
             ("Giuseppe Mazzini", "16 April 1863", "Little Italy", "processione"),
             "1356763", "italy"),
            ("Italian Hospital", "Q27082031",
             "The former Italian Hospital at the south end of Queen Square is now part of Great Ormond Street "
             "Hospital.",
             "en:Queen Square, London",
             ("former Italian Hospital", "Great Ormond Street Hospital"),
             "1245486", "italy"),
            ("22 Frith Street", "Q26319701",
             "The Polledri family opened Bar Italia here in 1949 and still own it. In 1926 John Logie Baird gave the "
             "first public demonstration of television in the same building.",
             "en:Bar Italia",
             ("1949 by the Polledri family", "John Logie Baird", "22 Frith Street"),
             "1066803", "italy"),
            ("41 and 43 Beak Street", "Q27080629",
             "The Venetian painter Canaletto lived at No. 41 between 1749 and 1752, during the decade he spent "
             "painting views of London.",
             "en:Canaletto",
             ("number 41 Beak Street", "between 1749 and 1752", "1746 to 1756"),
             "1218109", "italy"),
            ("4 Grosvenor Square", "Q20010239",
             "The Italian ambassador's residence, built about 1728. The embassy had used 19–20 Grosvenor Square from "
             "1887 until that building was demolished in 1933.",
             "en:Embassy of Italy, London",
             ("4 Grosvenor Square", "about 1728", "19/20 Grosvenor Square since 1887", "demolished in 1933"),
             "1066736", "italy"),
            ("38–48 Belgrave Square", "Q17527417",
             "No. 39 houses the Italian Cultural Institute, the Istituto Italiano di Cultura.",
             "en:Italian Cultural Institute, London",
             ("Istituto Italiano di Cultura", "39 Belgrave Square"),
             "1292022", "italy"),
            ("Lancaster House", "Q1146311",
             "As Stafford House, home of the Dukes of Sutherland, it received the Italian revolutionary leader "
             "Giuseppe Garibaldi among its guests.",
             "en:Lancaster House",
             ("Stafford House", "Italian revolutionary leader Giuseppe Garibaldi"),
             "1236546", "italy"),
            ("Aubrey House", "Q4819127",
             "Peter and Clementia Taylor, supporters of Italian unification, made it a haunt of exiles. Mazzini was a "
             "frequent visitor, and Garibaldi stayed for a few days in 1864.",
             "en:Aubrey House",
             ("movement for Italian unification", "Giuseppe Mazzini was a frequent visitor", "Garibaldi stayed",
              "1864"),
             "1188804", "italy"),
            ("Royal Opera House", "Q55018",
             "For decades it was the Royal Italian Opera, where every opera was sung in Italian until 1892.",
             "en:Royal Opera House",
             ("Royal Italian Opera", "presented all operas in Italian", "until 1892"),
             "1066392", "italy"),
            ("His Majesty's Theatre", "Q1155331",
             "The first theatre on this site opened in 1705 with Italian singers and was given over to Italian opera "
             "after 1709. Handel's Rinaldo, the first Italian opera written for London, opened here in 1711.",
             "en:His Majesty's Theatre, London",
             ("April 1705 with imported Italian singers", "devoted to Italian opera", "Rinaldo",
              "first Italian opera composed specifically for the London stage"),
             "1357090", "italy"),
            ("E. Pellicci", "Q27087072",
             "Tuscan immigrants opened the café in 1900; it is named after Priamo Pellicci and his wife Elide. The "
             "building and its Art Deco interior were listed in 2005.",
             "en:E. Pellicci",
             ("1900 by Tuscan immigrants", "Priamo Pellicci", "Elide", "Grade II listed in 2005"),
             "1391332", "italy"),
            ("Marconi House", "Q27081587",
             "Headquarters of the Marconi Companies from 1912 to 1933. The first programmes of the 2LO radio station "
             "were broadcast from its seventh floor in 1922 and 1923.",
             "en:Marconi House",
             ("headquarters of the Marconi Companies", "1912 to 1933", "2LO", "seventh floor"),
             "1236757", "italy"),
            ("Estorick Collection of Modern Italian Art", "Q5401727",
             "Britain's only gallery devoted to modern Italian art, strong in the Futurists. Since 1998 it has been "
             "in Northampton Lodge, a listed Georgian house that was Basil Spence's home.",
             "en:Estorick Collection of Modern Italian Art",
             ("only gallery devoted to modern Italian art", "Futurist", "Northampton Lodge", "Basil Spence", "1998"),
             None, "italy"),
            ("Brompton Oratory", "Q1769288",
             "Its twelve apostles by Giuseppe Mazzuoli came from Siena Cathedral in 1895, and an Italian architect "
             "led the decoration of 1927–32.",
             "en:Brompton Oratory",
             ("Giuseppe Mazzuoli", "Siena Cathedral in 1895", "1927–32", "Italian architect"),
             "1358123", "italy"),
        ]),
}
