"""London periods. Boundaries follow the city's turning points, not decades."""
PERIODS = [
    # (key, label, start, end, colour) — oxblood brick for the oldest, through ochre and green, to slate and violet
    ("p1", "Before 1666, the Great Fire",          1000, 1666, "#4a1410"),
    ("p2", "1667–1713 Rebuilding after the Fire",  1667, 1713, "#8c1c13"),
    ("p3", "1714–1836 Georgian",                   1714, 1836, "#c0462b"),
    ("p4", "1837–1870 Early Victorian",            1837, 1870, "#d97a2b"),
    ("p5", "1871–1901 Late Victorian",             1871, 1901, "#e5b13a"),
    ("p6", "1902–1939 Edwardian and interwar",     1902, 1939, "#8e9f3c"),
    ("p7", "1940–1959 War and rebuilding",         1940, 1959, "#3f8f6b"),
    ("p8", "1960–1979 Estates and towers",         1960, 1979, "#2c7391"),
    ("p9", "1980–1999 Docklands and the City",     1980, 1999, "#3a4f9a"),
    ("p10", "2000– The new skyline",               2000, 2100, "#6a3f8f"),
]
UNKNOWN = ("p0", "Year not known", 0, 0, "#c9ccce")


def period_index(year: int) -> int:
    """Index into PERIODS; len(PERIODS) for a building whose year is not known."""
    if not year:
        return len(PERIODS)
    for i, (_, _, a, b, _) in enumerate(PERIODS):
        if a <= year <= b:
            return i
    return 0
