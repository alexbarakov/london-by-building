"""DRAFT context layer: Harry Potter's London (films, books, fandom).

Same entry format as pipeline/curated.py: (name, wikidata QID, story, wikipedia "en:Title", checks, NHLE (P1216) or
None, group). Every string in `checks` appears (case-sensitive) in the plain-text extract of the cited en.wikipedia
article (API prop=extracts, explaintext=1, redirects=1); checks were run on 2026-10-15. Each QID was read from
Special:EntityData: it has P625 inside the nine boroughs; NHLE numbers are copied from P1216 where present. Where the
building's own article does not carry the Potter fact, the entry cites the film or book article that names it.

Dropped during research:
- Claremont Square (12 Grimmauld Place, nos. 23-29): the article supports it, but Q16258488 is the square/reservoir and
  no Wikidata item exists for the terrace houses.
- London Zoo Reptile House (Philosopher's Stone python scene): no item for the Reptile House; Q270263 is the whole zoo.
- Great Scotland Yard (Deathly Hallows Part 1; red phone box near Scotland Yard in Order of the Phoenix): the article
  is about the street. A hotel item exists (Q135781383, 3-5 Great Scotland Yard) but no article ties it to the films.
- Millennium Bridge (Half-Blood Prince), Lambeth Bridge (Prisoner of Azkaban): bridges, not buildings.
- Charing Cross Road (Leaky Cauldron in the books), Tottenham Court Road (Deathly Hallows café; also the Burger King
  that inspired the Ministry atrium design), Cecil Court and Goodwin's Court (fan-claimed Diagon Alley inspirations;
  Rowling denied any real model), Trafalgar Square (Deathly Hallows Part 2 premiere), Leicester Square: streets/squares.
- House of MinaLima (Soho): the MinaLima article confirms the shop, but there is no Wikidata building item and the
  article gives no address.
- Harry Potter Shop at Platform 9¾: inside King's Cross; folded into the King's Cross entry.
- St Pancras railway station (Q720102): same coordinates as the hotel item; the hotel article carries the film fact.
- Bloomsbury Publishing, Bedford Square: no item for no. 50; Q2893581 is the square.
- Freemasons' Hall, Piccadilly Circus, Shaftesbury Avenue: their articles do not mention Harry Potter.
- Harry Potter Photographic Exhibition (Covent Garden, 2021-22): closed, no building named.
- Warner Bros. Studio Tour (Leavesden), Black Park, Clapham Junction (Rowling's flat): outside the nine boroughs.

Doubts to check before publishing:
- Westminster tube station (Q1135834) is an underground station item, not a building; its entrance is under Portcullis
  House. Keep only if the map accepts station items, otherwise drop or re-point to Portcullis House (whose article
  does not mention the film).
- Borough Market (Q894072), Natural History Museum, British Library and Abbey Road Studios are institution-type items
  carrying the building's coordinates (all except Borough Market have NHLE numbers).
- Big Ben (Q41225, the Elizabeth Tower) and Buckingham Palace appear only as backdrops in the CGI-assisted Thames
  flight of Order of the Phoenix; weaker than the other film entries.
- Royal Albert Hall: the article only lists "the Harry Potter series" among its film-with-live-orchestra seasons.
- The 'books' group is thin (King's Cross, Euston): most real places in the books are streets (Charing Cross Road,
  Tottenham Court Road). Euston is there for Rowling's own admission that she mixed up the two stations.
- Odeon Leicester Square (Q3349144) has no P1216 on Wikidata.
"""

LAYER = dict(
    id="potter", section="Art and letters", title="Harry Potter's London", era="1997–today",
    intro=("J. K. Rowling's first Harry Potter book came out in 1997, and the eight films followed between 2001 "
           "and 2011. Most of the wizarding world was built at Leavesden studios outside London, but the films "
           "borrowed a market hall, a bank interior and a station hotel in the city. King's Cross, where the "
           "Hogwarts Express leaves in the books, now has its own Platform 9¾, and the West End has staged the "
           "eighth story since 2016."),
    entries=[
        # ---- films: buildings that appear on screen ----
        ("Leadenhall Market", "Q961148",
         "Horace Jones's market hall of 1881 stood in for the London streets near the Leaky Cauldron and Diagon "
         "Alley in Harry Potter and the Philosopher's Stone (2001). The market is a Grade II* listed building.",
         "en:Leadenhall Market",
         ("designed in 1881 by Sir Horace Jones", "near the Leaky Cauldron and Diagon Alley",
          "Harry Potter and the Philosopher's Stone (2001)", "Grade II* listed building"),
         "1286182", "films"),
        ("Australia House", "Q38166787",
         "The Australian High Commission on the Strand, opened by George V in 1918. Its grand interior became "
         "Gringotts Wizarding Bank in Harry Potter and the Philosopher's Stone.",
         "en:High Commission of Australia, London",
         ("A major landmark on the Strand", "opened by King George V", "3 August 1918",
          "used as the setting of Gringotts Wizarding Bank in Harry Potter and the Philosopher's Stone"),
         "1357166", "films"),
        ("St Pancras hotel", "Q7590892",
         "Filmmakers used the Gothic hotel and station as the exterior of King's Cross in Chamber of Secrets and "
         "Deathly Hallows – Part 2, judging their architecture more impressive than the real station next door.",
         "en:St Pancras London Hotel",
         ("act as King's Cross station's exteriors for Harry Potter and the Chamber of Secrets",
          "Harry Potter and the Deathly Hallows – Part 2", "Gothic architecture was considered far more impressive"),
         None, "films"),
        ("Westminster tube station", "Q1135834",
         "The crew closed the station on 22 October 2006 to film Arthur Weasley taking Harry to his trial at the "
         "Ministry of Magic in Order of the Phoenix.",
         "en:Harry Potter and the Order of the Phoenix (film)",
         ("closed the Westminster tube station on 22 October 2006",
          "Arthur Weasley accompanying Harry to his trial at the Ministry of Magic"),
         None, "films"),
        ("Borough Market", "Q894072",
         "Prisoner of Azkaban (2004) was the first Potter film to use real locations widely, and parts of it were "
         "shot in and around the market. The Knight Bus sequence took several weeks to film across London.",
         "en:Harry Potter and the Prisoner of Azkaban (film)",
         ("first in the series to extensively use real-life locations", "filmed in and around Borough Market",
          "The Knight Bus sequence was shot over several weeks"),
         None, "films"),
        ("Big Ben", "Q41225",
         "In Order of the Phoenix the Order flies along the Thames to Grimmauld Place, and Dumbledore's Army to the "
         "Ministry, past landmarks that include Big Ben.",
         "en:Harry Potter and the Order of the Phoenix (film)",
         ("the River Thames, used for the flight of the Order of the Phoenix", "flight of Dumbledore's Army",
          "Big Ben"),
         None, "films"),
        ("Buckingham Palace", "Q42182",
         "The palace is one of the landmarks passed in the Thames flight sequence of Order of the Phoenix (2007), "
         "with the London Eye and HMS Belfast.",
         "en:Harry Potter and the Order of the Phoenix (film)",
         ("the London Eye, Canary Wharf, Big Ben, Buckingham Palace, and HMS Belfast",),
         "1239087", "films"),
        ("Abbey Road Studios", "Q209651",
         "The last recording sessions for the Harry Potter films took place here on 27 May 2011, with the London "
         "Symphony Orchestra.",
         "en:Harry Potter (film series)",
         ("final recording sessions for Harry Potter took place on 27 May 2011 at Abbey Road Studios",
          "London Symphony Orchestra"),
         "1393688", "films"),

        # ---- books: real places named in the novels ----
        ("King's Cross station", "Q219867",
         "In the books the Hogwarts Express leaves from Platform 9¾, through the brick barrier between platforms 9 "
         "and 10. The films used the arches between platforms 4 and 5; the station put up a sign by 2003, then a "
         "trolley in the wall and, in 2012, a Harry Potter shop.",
         "en:London King's Cross railway station",
         ("starting point of the Hogwarts Express", "brick wall barrier between platforms 9 and 10",
          "between platforms 4 and 5 were redressed by the film crew", "By 2003, a sign marking Platform 9 3/4",
          "a trolley fixed to the wall", "Harry Potter-themed shop opened nearby in 2012"),
         "1078328", "books"),
        ("Euston station", "Q800751",
         "After the books were published, Rowling realised she had confused the layout of King's Cross with that "
         "of Euston.",
         "en:Places in Harry Potter",
         ("Rowling found that she had confused the layout of King's Cross with that of Euston station",),
         None, "books"),

        # ---- fandom: premieres, the play, exhibitions ----
        ("Palace Theatre", "Q4592132",
         "Richard D'Oyly Carte built it as a home for English grand opera. Harry Potter and the Cursed Child began "
         "previews here in June 2016 and opened on 30 July.",
         "en:Palace Theatre, London",
         ("Richard D'Oyly Carte", "home of English grand opera", "Harry Potter and the Cursed Child",
          "began previews at the theatre in June 2016", "opened on 30 July"),
         "1066339", "fandom"),
        ("Odeon Leicester Square", "Q3349144",
         "Harry Potter and the Philosopher's Stone had its world premiere here on 4 November 2001, with the cinema "
         "dressed to look like Hogwarts.",
         "en:Harry Potter and the Philosopher's Stone (film)",
         ("world premiere at the Odeon Leicester Square in London on 4 November 2001",
          "the cinema arranged to resemble Hogwarts School"),
         None, "fandom"),
        ("Natural History Museum", "Q309388",
         "On the night Deathly Hallows was released in 2007, Rowling held an all-night signing and reading here "
         "for 1,700 guests chosen by ballot.",
         "en:Harry Potter and the Deathly Hallows",
         ("all-night book signing and reading by Rowling at the Natural History Museum",
          "The 1,700 guests in attendance were chosen by ballot"),
         "1080675", "fandom"),
        ("British Library", "Q23308",
         "Harry Potter: A History of Magic opened here in 2017 for the 20th anniversary of the first book. It showed "
         "Rowling's original drafts and drawings next to a Ripley Scroll and Nicolas Flamel's headstone.",
         "en:Harry Potter: A History of Magic",
         ("opened at the British Library in 2017", "20th anniversary",
          "original drafts of the Harry Potter books and original artwork by Rowling", "Ripley Scroll",
          "Nicolas Flamel's headstone"),
         "1426345", "fandom"),
        ("Royal Festival Hall", "Q647390",
         "Fantastic Beasts: The Secrets of Dumbledore, the third and last Fantastic Beasts film, had its premiere "
         "here on 29 March 2022.",
         "en:Fantastic Beasts: The Secrets of Dumbledore",
         ("premiered at the Royal Festival Hall in London on 29 March 2022", "third and final instalment"),
         "1249756", "fandom"),
        ("Royal Albert Hall", "Q193639",
         "Since 2009 the hall has run seasons of films screened with a live orchestra, and the Harry Potter series "
         "is among them.",
         "en:Royal Albert Hall",
         ("Since 2009, the hall has also curated regular seasons of English-language film-and-live-orchestra "
          "screenings", "the Harry Potter series"),
         "1217742", "fandom"),
    ],
)
