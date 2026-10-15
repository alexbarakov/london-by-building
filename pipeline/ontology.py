"""The city's ontology: people, events and organisations, tied to the buildings where they left a trace.

An entity is linked to a building when its pattern appears in a checked text about that building: a story of a curated
layer (checked by s08_curated) or a 'Did you know' fact (s11_facts). s13_graph.py builds the graph.

(id, type, English label, Dutch label, years, regex on the English text)
"""

PERSON, EVENT, ORG = "person", "event", "organisation"

ENTITIES = [
    # architects and builders
    ("wren", PERSON, "Christopher Wren", "Christopher Wren", "1632–1723", r"\bWren"),
    ("hooke", PERSON, "Robert Hooke", "Robert Hooke", "1635–1703", r"Hooke"),
    ("hawksmoor", PERSON, "Nicholas Hawksmoor", "Nicholas Hawksmoor", "c. 1661–1736", r"Hawksmoor"),
    ("inigojones", PERSON, "Inigo Jones", "Inigo Jones", "1573–1652", r"Inigo Jones"),
    ("nash", PERSON, "John Nash", "John Nash", "1752–1835", r"John Nash|\bNash's"),
    ("adam", PERSON, "Robert Adam", "Robert Adam", "1728–1792", r"Robert Adam"),
    ("brunel", PERSON, "Isambard Kingdom Brunel", "Isambard Kingdom Brunel", "1806–1859", r"Brunel"),
    ("gilbertscott", PERSON, "Giles Gilbert Scott", "Giles Gilbert Scott", "1880–1960", r"Giles Gilbert Scott"),
    ("holden", PERSON, "Charles Holden", "Charles Holden", "1875–1960", r"Charles Holden|Holden's"),
    ("leslie", PERSON, "Leslie Green", "Leslie Green", "1875–1908", r"Leslie Green"),
    ("lubetkin", PERSON, "Berthold Lubetkin and Tecton", "Berthold Lubetkin en Tecton", "1901–1990", r"Lubetkin|Tecton"),
    ("lasdun", PERSON, "Denys Lasdun", "Denys Lasdun", "1914–2001", r"Lasdun"),
    ("goldfinger", PERSON, "Ernő Goldfinger", "Ernő Goldfinger", "1902–1987", r"Goldfinger"),
    ("matcham", PERSON, "Frank Matcham", "Frank Matcham", "1854–1920", r"Matcham"),
    # writers, artists, musicians, scientists
    ("dickens", PERSON, "Charles Dickens", "Charles Dickens", "1812–1870", r"Dickens"),
    ("pepys", PERSON, "Samuel Pepys", "Samuel Pepys", "1633–1703", r"Pepys"),
    ("shakespeare", PERSON, "William Shakespeare", "William Shakespeare", "1564–1616", r"Shakespeare"),
    ("johnson", PERSON, "Samuel Johnson", "Samuel Johnson", "1709–1784", r"Samuel Johnson|Dr Johnson"),
    ("conandoyle", PERSON, "Arthur Conan Doyle", "Arthur Conan Doyle", "1859–1930", r"Conan Doyle|Sherlock"),
    ("orwell", PERSON, "George Orwell", "George Orwell", "1903–1950", r"Orwell"),
    ("wilde", PERSON, "Oscar Wilde", "Oscar Wilde", "1854–1900", r"Oscar Wilde"),
    ("koestler", PERSON, "Arthur Koestler", "Arthur Koestler", "1905–1983", r"Koestler"),
    ("rowling", PERSON, "J.K. Rowling and Harry Potter", "J.K. Rowling en Harry Potter", "", r"Rowling|Harry Potter"),
    ("handel", PERSON, "George Frideric Handel", "Georg Friedrich Händel", "1685–1759", r"Handel"),
    ("mendelssohn", PERSON, "Felix Mendelssohn", "Felix Mendelssohn", "1809–1847", r"Mendelssohn"),
    ("mozart", PERSON, "Wolfgang Amadeus Mozart", "Wolfgang Amadeus Mozart", "1756–1791", r"Mozart"),
    ("chopin", PERSON, "Frédéric Chopin", "Frédéric Chopin", "1810–1849", r"Chopin"),
    ("beatles", ORG, "The Beatles", "The Beatles", "1960–1970", r"Beatles"),
    ("hendrix", PERSON, "Jimi Hendrix", "Jimi Hendrix", "1942–1970", r"Hendrix"),
    ("marley", PERSON, "Bob Marley", "Bob Marley", "1945–1981", r"Bob Marley"),
    ("faraday", PERSON, "Michael Faraday", "Michael Faraday", "1791–1867", r"Faraday"),
    ("freud", PERSON, "Sigmund Freud", "Sigmund Freud", "1856–1939", r"Freud"),
    ("banksy", PERSON, "Banksy", "Banksy", "", r"Banksy"),
    # politics and exile
    ("victoria", PERSON, "Queen Victoria", "Koningin Victoria", "1819–1901", r"Queen Victoria"),
    ("henry8", PERSON, "Henry VIII", "Hendrik VIII", "1491–1547", r"Henry VIII"),
    ("churchill", PERSON, "Winston Churchill", "Winston Churchill", "1874–1965", r"Churchill"),
    ("marx", PERSON, "Karl Marx", "Karl Marx", "1818–1883", r"\bMarx\b"),
    ("lenin", PERSON, "Lenin", "Lenin", "1870–1924", r"Lenin"),
    ("gandhi", PERSON, "Mahatma Gandhi", "Mahatma Gandhi", "1869–1948", r"Gandhi"),
    ("sunyatsen", PERSON, "Sun Yat-sen", "Sun Yat-sen", "1866–1925", r"Sun Yat-sen|Cantlie"),
    ("degaulle", PERSON, "Charles de Gaulle and the Free French", "Charles de Gaulle en de Vrije Fransen", "1890–1970",
     r"de Gaulle|Free French"),
    ("anders", PERSON, "General Anders and the Polish exiles", "Generaal Anders en de Poolse ballingen", "1892–1970",
     r"Anders|Polish Foreign Office|Ognisko"),
    ("mazzini", PERSON, "Giuseppe Mazzini", "Giuseppe Mazzini", "1805–1872", r"Mazzini|Garibaldi"),
    # events
    ("greatfire", EVENT, "The Great Fire of London", "De Grote Brand van Londen", "1666", r"Great Fire|fire of 1666"),
    ("ww1", EVENT, "The First World War", "De Eerste Wereldoorlog", "1914–1918", r"First World War|Zeppelin"),
    ("blitz", EVENT, "The Blitz", "De Blitz", "1940–1941", r"Blitz"),
    ("vweapons", EVENT, "The V-1 and V-2 rockets", "De V-1 en V-2", "1944–1945", r"\bV-[12]\b"),
    ("ww2", EVENT, "The Second World War", "De Tweede Wereldoorlog", "1939–1945", r"Second World War"),
    # organisations and communities
    ("eic", ORG, "East India Company", "Engelse Oost-Indische Compagnie", "1600–1874", r"East India Company"),
    ("boe", ORG, "Bank of England", "Bank of England", "1694–today", r"Bank of England"),
    ("parliament", ORG, "Parliament", "Parlement", "", r"Parliament|House of Commons|House of Lords"),
    ("lcc", ORG, "London County Council", "London County Council", "1889–1965", r"London County Council"),
    ("underground", ORG, "The Underground", "De Underground", "1863–today", r"Underground|Metropolitan Railway"),
    ("huguenots", ORG, "Huguenots", "Hugenoten", "", r"Huguenot"),
    ("chinatown", ORG, "Chinese London", "Chinees Londen", "", r"Chinatown|Chinese|Limehouse"),
]
