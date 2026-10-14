"""DRAFT 'Did you know' facts for inner London: one striking fact per building, shown on its card.

Format: (wikipedia "en:Title", fact in English, checks, wikidata QID). Every string in `checks` appears
(case-sensitive) in the plain-text extract of the article; all checks were run on 2026-10-15. Each QID has P625
inside the nine boroughs (nearest-postcode test via postcodes.io). No building appears twice. Some facts are about
buildings that are also in curated_draft.py, but the facts differ from the layer stories.

Dropped during research:
- Bethlem/'bedlam' (Imperial War Museum): the IWM article does not say the building was known as Bedlam.
- Savoy Court 'traffic drives on the right': not in the Savoy Hotel article.
- Admiralty Arch nose, Marble Arch police station, Brompton Oratory dead drop: used as layer stories in 'secrets'.

Doubts:
- Liberty (Q3237793), Harrods (Q332474) and Bank of England (Q63637740 'bank building'): Liberty and Harrods items
  are the stores, typed as businesses but carrying the building's NHLE number.
- Big Ben (Q41225) is the Elizabeth Tower item; the Palace of Westminster fact (Ayrton Light) is also about the tower
  but is attached to the palace item, so the two facts land on different QIDs.
- Old Bailey: the fact says 'on the dome', which is in the article, though only Lady Justice and 'not blindfolded'
  are in checks.
"""

FACTS = [
    ("en:Monument to the Great Fire of London",
     "Wren and Hooke built the Monument to double as a scientific instrument: its central shaft was meant to "
     "serve as a zenith telescope and for gravity and pendulum experiments.",
     ("zenith telescope", "pendulum experiments"), "Q607700"),
    ("en:Big Ben",
     "Because of the soft ground beneath it, the Elizabeth Tower leans slightly to the north-west, by roughly 230"
     " mm over its 55 m height.",
     ("230 mm", "north-west"), "Q41225"),
    ("en:Palace of Westminster",
     "The Ayrton Light at the top of the clock tower is lit when either House sits after dark. Queen Victoria "
     "asked for it in 1885 so that she could see from Buckingham Palace whether the members were at work.",
     ("Ayrton Light", "1885", "at work"), "Q62408"),
    ("en:Burlington House",
     "The Royal Academy took over the main block in 1867 on a 999-year lease, at a rent of £1 a year.",
     ("1867", "999-year lease", "£1 per year"), "Q225471"),
    ("en:Royal Albert Hall",
     "The hall's echo was so strong that a canvas awning was hung below the dome, and it was said to be the only "
     "place where a British composer could be sure of hearing his work twice.",
     ("canvas awning", "hearing his work twice"), "Q193639"),
    ("en:Tower Bridge",
     "On 30 December 1952 the bridge began to open under a number 78 bus. The driver accelerated and jumped the "
     "gap; he was rewarded with a £10 bonus.",
     ("30 December 1952", "number 78", "£10 bonus"), "Q83125"),
    ("en:Liberty (department store)",
     "The Tudor-style store of 1924 was built from the timbers of two warships, HMS Impregnable and HMS "
     "Hindustan. Its frontage on Great Marlborough Street is as long as the Hindustan.",
     ("1924", "HMS Impregnable", "HMS Hindustan", "Great Marlborough Street"), "Q3237793"),
    ("en:Harrods",
     "On 16 November 1898 Harrods opened England's first escalator. Nervous customers were offered brandy at the "
     "top.",
     ("16 November 1898", "escalator", "brandy"), "Q332474"),
    ("en:Wesley's Chapel",
     "Margaret Thatcher was married in John Wesley's chapel in 1951, and in 1993 she gave it its present "
     "communion rail.",
     ("Margaret Thatcher", "married in the chapel in 1951", "communion rail"), "Q7983825"),
    ("en:Old Bailey",
     "The gilded Lady Justice on the dome holds a sword and scales but is not blindfolded.",
     ("Lady Justice", "not blindfolded"), "Q1194829"),
    ("en:Leadenhall Market",
     "The market stood in for the streets around the Leaky Cauldron and Diagon Alley in the film Harry Potter and"
     " the Philosopher's Stone (2001).",
     ("Diagon Alley", "Harry Potter and the Philosopher's Stone"), "Q961148"),
    ("en:Southwark Cathedral",
     "William Shakespeare's brother Edmund was buried here in 1607. His grave is unmarked, but a stone in the "
     "choir paving remembers him.",
     ("Edmund", "1607", "grave is unmarked"), "Q922967"),
    ("en:Bank of England",
     "The Bank is custodian of the United Kingdom's official gold reserves.",
     ("custodian to the official gold reserves",), "Q63637740"),
    ("en:Horse Guards (building)",
     "Horse Guards was once the entrance to the Palace of Whitehall, which is why the King's Life Guard still "
     "stands guard over it.",
     ("Palace of Whitehall", "King's Life Guard"), "Q492350"),
    ("en:Centre Point",
     "The site was once occupied by a gallows, and the tower stands over the old route of St Giles High Street, "
     "which was moved to make room for it.",
     ("gallows", "St Giles High Street"), "Q2339039"),
    ("en:Buckingham Palace",
     "The palace has 775 rooms, and its garden is the largest private garden in London.",
     ("775 rooms", "largest private garden in London"), "Q42182"),
    ("en:St Paul's Cathedral",
     "In the Whispering Gallery, 99 feet above the floor, a whisper against the wall can be heard by a listener "
     "with an ear to the wall anywhere else around the gallery.",
     ("Whispering Gallery", "99 feet"), "Q173882"),
    ("en:Westminster Abbey",
     "Besides 40 coronations, at least 16 royal weddings have taken place in the abbey since 1100.",
     ("16 royal weddings", "since 1100"), "Q5933"),
    ("en:St Clement Danes",
     "The bells play \"Oranges and Lemons\" every day at 9 am, noon, 3 pm and 6 pm.",
     ("Oranges and Lemons", "9 am, noon, 3pm and 6pm"), "Q2038269"),
    ("en:Banqueting House",
     "The ceiling paintings by Peter Paul Rubens were added in the 1630s. In the 19th century the building was "
     "re-faced in Portland stone.",
     ("Peter Paul Rubens", "1630s", "Portland stone"), "Q642039"),
    ("en:Lloyd's building",
     "The Underwriting Room houses the Lutine Bell, and on the same floor lies the loss book, in which major "
     "losses have been entered by quill for 300 years.",
     ("Lutine Bell", "loss book", "quill"), "Q1814818"),
    ("en:Burlington Arcade",
     "Whistling is banned in the arcade because it was once a signal to pickpockets. Only three people have been "
     "exempted, among them Paul McCartney.",
     ("Whistling is also banned", "pickpockets", "Paul McCartney"), "Q2928520"),
    ("en:Royal Opera House",
     "The present building is the third theatre on the site; fires destroyed the earlier ones in 1808 and 1856.",
     ("third theatre on the site", "1808 and 1856"), "Q55018"),
    ("en:Natural History Museum, London",
     "Waterhouse covered the building inside and out in terracotta tiles to resist the soot of Victorian London, "
     "with reliefs of plants and animals.",
     ("terracotta", "sooty atmosphere", "flora and fauna"), "Q309388"),
    ("en:Royal Exchange, London",
     "The golden grasshopper weathervane was the crest of the founder, Thomas Gresham.",
     ("Gresham Grasshopper", "weathervane"), "Q1241240"),
    ("en:St Pancras railway station",
     "In the late 1960s there were plans to demolish the station entirely; a campaign led by the Victorian "
     "Society and John Betjeman saved it.",
     ("late 1960s", "demolish it entirely", "Victorian Society", "John Betje"), "Q720102"),
    ("en:Westminster Cathedral",
     "The cathedral was dedicated in 1895, but its mosaics are still incomplete; the decoration was left to later"
     " generations.",
     ("1895", "still incomplete, mosaics"), "Q739364"),
    ("en:St Martin-in-the-Fields",
     "James Gibbs's design of 1722–1726 was copied widely; St Michael's Church in Charleston, South Carolina, was"
     " heavily influenced by it.",
     ("James Gibbs", "1722–1726", "Charleston, South Carolina"), "Q1335201"),
    ("en:Savoy Hotel",
     "The extension of 1903–04 pioneered steel-frame construction in London and added Britain's first serviced "
     "apartments.",
     ("1903–04", "steel frame construction in London", "first serviced apartments"), "Q746639"),
    ("en:Mansion House, London",
     "In the most famous Mansion House Speech, in 1911, David Lloyd George warned Germany against opposing "
     "British influence.",
     ("Mansion House Speech of 1911", "David Lloyd George"), "Q1786933"),
]
