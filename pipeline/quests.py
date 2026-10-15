"""Quests: chains of riddles, each solved by finding a building on the map and clicking it.

Every riddle rests on a story of a context layer (checked against Wikipedia by s08_curated) or on the map's own
years. s12_quests.py resolves each answer to its buildings, adds a hint with the answer's direction and distance
from Charing Cross, and checks that every step can be solved.

A step's answer is ("story", layer id, story name) or ("rule", {"before": year}).
Levels: 1 easy (photos, plain hints), 2 medium, 3 hard (the first hint only gives a direction).
"""


def T(en):
    return dict(en=en)


def S(layer, name, riddle, hint, **kw):
    return dict(answer=("story", layer, name), layer=layer, riddle=T(riddle), hints=[T(hint)], **kw)


QUESTS = [
    # ---------- easy ----------
    dict(id="fire", level=1, title=T("After the Great Fire"),
         intro=T("Five buildings that tell how the City burned in 1666 and how it was rebuilt."),
         steps=[
             S("fire", "The Monument",
               "A Doric column, 202 feet tall, standing 202 feet from the spot in Pudding Lane where the fire began.",
               "It is simply called the Monument.", photo=True),
             S("fire", "St Paul's Cathedral",
               "Wren's cathedral replaced the medieval church lost in the fire. Completed in 1710, at 365 feet it "
               "was the tallest building in London until 1963.",
               "The great dome on Ludgate Hill."),
             S("fire", "St Bride's Church",
               "Wren's second highest steeple, 226 feet. Tiered wedding cakes are said to copy its shape.",
               "St Bride's, off Fleet Street."),
             S("fire", "Temple Bar",
               "Wren's gateway once stood where Fleet Street meets the Strand. Taken down in 1878, it spent over a "
               "century in a Hertfordshire park before coming back to the City.",
               "Look by Paternoster Square, beside St Paul's."),
             S("fire", "Prince Henry's Room",
               "A tavern rebuilt in 1610, one of the few City buildings older than the fire. Pepys drank there in 1661.",
               "17 Fleet Street."),
         ]),
    dict(id="power", level=1, title=T("Crown and Parliament"),
         intro=T("Where kings were crowned, kept their jewels and lost their heads."),
         steps=[
             S("power", "White Tower",
               "William the Conqueror built this keep in the early 1080s. It is named after a coat of whitewash "
               "ordered by Henry III in 1240.",
               "The keep of the Tower of London.", photo=True),
             S("power", "Westminster Abbey",
               "Every coronation since 1066 has taken place here: 40 monarchs so far.",
               "The abbey church at Westminster."),
             S("power", "Westminster Hall",
               "Built in 1097 for William II and given its hammerbeam roof in 1393, it survived the fire of 1834 "
               "that destroyed most of the old palace.",
               "The oldest part of the Palace of Westminster."),
             S("power", "Jewel Tower",
               "Built in 1365–1366 to hold the personal treasure of Edward III, one of the few parts of the "
               "medieval palace to survive.",
               "Across the road from the Palace of Westminster."),
             S("power", "Banqueting House",
               "Inigo Jones's hall of 1619–1622 is the only large part left of the Palace of Whitehall. Charles I "
               "was executed outside it.",
               "On Whitehall."),
         ]),
    dict(id="writers", level=1, title=T("Writers' London"),
         intro=T("A dictionary, a detective and a nightingale: five writers' houses."),
         steps=[
             S("writers", "Dr Johnson's House",
               "Samuel Johnson compiled his Dictionary of the English Language here between 1748 and 1759. It is "
               "the only one of his 18 City homes to survive.",
               "17 Gough Square, off Fleet Street."),
             S("writers", "Charles Dickens Museum",
               "His only London house still standing, where he wrote all of Oliver Twist and Nicholas Nickleby.",
               "48 Doughty Street."),
             S("writers", "Keats House",
               "A poet lodged here from 1818 to 1820 and, by his friend's account, wrote an ode to a nightingale "
               "under a plum tree in the garden.",
               "In Hampstead."),
             S("writers", "Sherlock Holmes Museum",
               "A house of 1815 bears the number 221B by permission of the council, although it stands between "
               "237 and 241.",
               "Baker Street."),
             S("writers", "Ye Olde Cheshire Cheese",
               "A Fleet Street pub rebuilt shortly after the Great Fire. Dickens, Chesterton and Mark Twain drank "
               "here, and a swearing grey parrot lived here for about 40 years.",
               "Fleet Street."),
         ]),
    # ---------- medium ----------
    dict(id="music", level=2, title=T("Music London"),
         intro=T("From Handel and the boy Mozart to the Beatles on a roof."),
         steps=[
             S("music", "Handel Hendrix House",
               "Handel lived here from 1723 until 1759. Jimi Hendrix lived next door in 1968–1969.",
               "Brook Street, Mayfair."),
             S("music", "180 Ebury Street",
               "In 1764 an eight-year-old composed his first symphony in this house.",
               "Ebury Street, Belgravia."),
             S("music", "Royal Albert Hall",
               "Queen Victoria opened the hall in 1871; the Proms have been held here every summer since 1941.",
               "South Kensington."),
             S("music", "Abbey Road Studios",
               "The studios opened in 1931. A band named its 1969 album after the road, and fans still cross the "
               "zebra crossing outside.",
               "St John's Wood."),
             S("music", "3 Savile Row",
               "The Beatles' company Apple had its headquarters here, and the band played its last live "
               "performance on the roof on 30 January 1969.",
               "Savile Row, the tailors' street."),
         ]),
    dict(id="railways", level=2, title=T("Tunnels and termini"),
         intro=T("Under the river, under the streets and into the great stations."),
         steps=[
             S("railways", "Brunel Engine House",
               "Marc Brunel built it for the Thames Tunnel, opened in 1843, the first tunnel under a navigable river.",
               "Rotherhithe, on the south bank."),
             S("railways", "Baker Street station",
               "One of the stations of the world's first underground railway, opened on 10 January 1863.",
               "Baker Street."),
             S("railways", "St Pancras station",
               "Its single-span roof made the train shed the largest enclosed space in the world; the undercroft "
               "was laid out for storing beer.",
               "Euston Road."),
             S("railways", "King's Cross station",
               "An extension built in 1972 as a temporary structure hid the front of this terminus for 40 years.",
               "Its neighbour across Pancras Road."),
             S("railways", "Liverpool Street station",
               "Before the Second World War thousands of child refugees of the Kindertransport arrived here.",
               "On the eastern edge of the City."),
         ]),
    dict(id="pubs", level=2, title=T("Coffee, tea and hats"),
         intro=T("The first coffee house, the first tea room and the oldest hat shop."),
         steps=[
             S("pubs", "Jamaica Wine House",
               "A plaque marks the site of London's first coffee house, opened in 1652. Pepys visited in 1660.",
               "In the alleys off Cornhill."),
             S("pubs", "The George Inn",
               "The only galleried coaching inn left in London, rebuilt in 1677.",
               "Borough High Street, Southwark."),
             S("pubs", "Twinings",
               "Britain's first known tea room opened here in 1706, and the firm still trades from the same "
               "premises.",
               "216 Strand."),
             S("pubs", "Lock & Co. Hatters",
               "Founded in 1676 and at this address since 1765: the oldest hat shop in the world.",
               "6 St James's Street."),
             S("pubs", "Lamb and Flag",
               "A pub since 1772 that hosted bare-knuckle fights upstairs and was nicknamed the Bucket of Blood.",
               "Covent Garden."),
         ]),
    dict(id="science", level=2, title=T("Science and medicine"),
         intro=T("A twelfth-century hospital, an operating theatre in an attic and a mould on a plate."),
         steps=[
             S("science", "St Bartholomew's Hospital",
               "Founded in 1123, it is the oldest hospital in Britain still on its original site.",
               "Smithfield."),
             S("science", "Old Operating Theatre",
               "In 1822 part of a church's herb garret became an operating theatre, the oldest surviving one in "
               "Britain.",
               "St Thomas Street, by London Bridge."),
             S("science", "St Mary's Hospital",
               "Alexander Fleming discovered penicillin here in 1928.",
               "Paddington."),
             S("science", "Great Ormond Street Hospital",
               "The Hospital for Sick Children opened in 1852; in 1929 J. M. Barrie gave it the copyright of "
               "Peter Pan.",
               "Bloomsbury."),
             S("science", "John Snow pub",
               "Named after the physician who traced the cholera outbreak of 1854 to a nearby water pump.",
               "Soho."),
         ]),
    # ---------- hard ----------
    dict(id="exiles", level=3, title=T("Exiles and radicals"),
         intro=T("An American printer, a Russian revolutionary, an Austrian doctor. The first hint only gives a "
                 "direction."),
         steps=[
             S("exiles", "Benjamin Franklin House",
               "He lived and worked here from 1757 to 1774. It is the last of his homes still standing.",
               "36 Craven Street."),
             S("exiles", "Marx Memorial Library",
               "Built in 1738 as a Welsh charity school. In 1902–1903 Lenin published seventeen issues of Iskra "
               "here.",
               "Clerkenwell Green."),
             S("exiles", "Freud Museum",
               "He escaped from Vienna in 1938 and spent the last year of his life here, with his analyst's couch.",
               "20 Maresfield Gardens."),
             S("exiles", "Bow Quarter",
               "The matchgirls' strike of 1888 began in this factory, over fourteen-hour days, fines and white "
               "phosphorus.",
               "Bow, in the East End."),
             S("exiles", "Kingsley Hall",
               "A community centre that fed workers in the General Strike of 1926. Gandhi stayed here in 1931.",
               "Bow."),
         ]),
    dict(id="secrets", level=3, title=T("Hidden London"),
         intro=T("A nose on an arch, a spies' letterbox and a war cabinet underground."),
         steps=[
             S("secrets", "Admiralty Arch",
               "On the inside wall of the northernmost arch is a small human nose, put there in 1997 in protest "
               "against surveillance.",
               "Where the Mall meets Trafalgar Square."),
             S("secrets", "Brompton Oratory",
               "During the Cold War, Soviet spies used the gap between the pillars and the wall at the front of "
               "this church as a dead drop.",
               "Brompton Road."),
             S("secrets", "Down Street station",
               "Closed in 1932 for lack of passengers, it became a bunker for Churchill and the war cabinet.",
               "Mayfair."),
             S("secrets", "Winchester Palace",
               "Only part of the great hall and its rose window remain of the bishops' London house of about 1136.",
               "Clink Street, Southwark."),
             S("secrets", "Bromley Hall",
               "A manor house dated by tree rings to about 1485, thought to be the oldest brick house in London.",
               "By the approach road to the Blackwall Tunnel."),
         ]),
    dict(id="blitz", level=3, title=T("The Blitz"),
         intro=T("Towers that stood when the churches burned, and one rule only the map can answer."),
         steps=[
             S("blitz", "Christ Church Greyfriars",
               "A firebomb gutted Wren's church on 29 December 1940; only the tower was kept, and the nave became "
               "a garden.",
               "Newgate Street."),
             S("blitz", "St Dunstan-in-the-East",
               "Wren's tower and spire survived the bombs of 1941, little else did; the ruin is now a public garden.",
               "Near the Tower of London."),
             S("blitz", "St Alban, Wood Street",
               "The church burned out in 1940. Its tower stands alone on a traffic island and is now a private house.",
               "Wood Street."),
             S("blitz", "Café de Paris",
               "A bomb hit this nightclub on 8 March 1941 and killed at least 34 people.",
               "Coventry Street, by Leicester Square."),
             dict(answer=("rule", dict(before=1666)), mode="period",
                  riddle=T("The Great Fire of 1666 destroyed most of the City. Find any building the map dates "
                           "before it."),
                  hints=[T("Colour by period and keep only the oldest one.")]),
         ]),
]
