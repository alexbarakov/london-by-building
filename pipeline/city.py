"""The city this build is for. Everything city-specific that is not a story lives here."""
SLUG = "london"
NAME = "London"
CRS = 27700                       # British National Grid, metres
ORIGIN = (530050.0, 180380.0)     # Charing Cross, the point London's distances are measured from
BOROUGHS = ["City of London", "Westminster", "Camden", "Islington", "Kensington and Chelsea", "Southwark",
            "Lambeth", "Tower Hamlets", "Hackney"]
SITE = "https://stop-token.com/lab/london/"
UA = {"User-Agent": f"{SLUG}-by-building/0.1 ({SITE})"}
WIKIDATA = "Q84"                  # London, for P131* (located in)
