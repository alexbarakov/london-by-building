"""Dates in listing and local-list prose: 'C18', 'Early C19', '1820-25', 'c.1890', '1880s', 'dated 1756'.

parse(text) reads a National Heritage List entry (it skips the legacy header up to the grade); parse_free(text)
reads ordinary prose. Both return (year, lo, hi, kind) for the first dating phrase, or None: the first date in an
entry dates the building, later ones its alterations.
"""
import re

CENT = r"(?:C|c\.?\s?|century\s)?"
PATS = [
    # explicit years and ranges: 1820-25, 1820-1825, c.1890, circa 1890, dated 1756
    (r"\b(?:c\.?|circa|ca\.?)\s?(1[2-9]\d\d)\s?[-–]\s?(\d{2,4})\b", "c_range"),
    (r"\b(?:c\.?|circa|ca\.?)\s?(1[2-9]\d\d)\b", "c_year"),
    (r"\b(1[2-9]\d\d)\s?[-–/]\s?(\d{1,4})\b", "range"),
    (r"\b(?:dated|built|erected|rebuilt|designed|completed)\s(?:in\s)?(1[2-9]\d\d)\b", "verb_year"),
    (r"\b(1[2-9]\d\d)s\b", "decade"),
    (r"\b(early|mid|late)[- ]?C(1[2-9]|20)\b", "qual_century"),
    (r"\bC(1[2-9]|20)\b", "century"),
    (r"\b((?:1[2-9]|20)\d\d)\b", "bare_year"),
]


def body(text):
    """Drop the legacy header (map sheet, file numbers, listing dates) and amendment notes before the grade token."""
    text = re.sub(r"This list entry was subject to a Minor Amendment.*?standards", " ", text)
    text = re.sub(r"\(Formerly [Ll]isted as.*?\)", " ", text)
    text = re.sub(r"\b\d{1,2}[./-]\d{1,2}[./-]\d{2,4}\b|\b\d{2}-[A-Z]{3}-\d{2}\b", " ", text)
    m = re.search(r"(?:\bG\.?V\.?\s+)?\b(?:II\*?|I)\b(?:\s+G\.?V\.?)?(?:\s+2\.)?\s", text[:400])
    return text[m.end():] if m else text


def parse(text):
    """Return (year, lo, hi, kind) for the first dating phrase in the description."""
    text = body(text)
    hits = []
    for pat, kind in PATS:
        for m in re.finditer(pat, text, flags=re.I if kind in ("c_range", "c_year", "verb_year", "qual_century") else 0):
            hits.append((m.start(), kind, m))
    if not hits:
        return None
    # earliest position wins; at the same position prefer the more specific pattern (list order)
    order = {k: i for i, (_, k) in enumerate(PATS)}
    pos, kind, m = sorted(hits, key=lambda h: (h[0], order[h[1]]))[0]
    if kind == "c_year":
        y = int(m.group(1)); return y, y - 5, y + 5, kind
    if kind in ("range", "c_range"):
        a, b = m.group(1), m.group(2)
        b = int(a[: 4 - len(b)] + b) if len(b) < 4 else int(b)
        a = int(a)
        if b < a or b - a > 60:
            return a, a, a, "year"
        return round((a + b) / 2), a, b, kind
    if kind in ("verb_year", "bare_year"):
        y = int(m.group(1)); return y, y, y, kind
    if kind == "decade":
        y = int(m.group(1)); return y + 5, y, y + 9, kind
    if kind == "qual_century":
        q, c = m.group(1).lower(), int(m.group(2))
        s = (c - 1) * 100
        lo, hi = {"early": (s, s + 33), "mid": (s + 33, s + 66), "late": (s + 66, s + 99)}[q]
        return round((lo + hi) / 2), lo, hi, kind
    c = int(m.group(1)); s = (c - 1) * 100
    return s + 50, s, s + 99, kind


ORD = {"twelfth": 12, "thirteenth": 13, "fourteenth": 14, "fifteenth": 15, "sixteenth": 16, "seventeenth": 17,
       "eighteenth": 18, "nineteenth": 19, "twentieth": 20}


def parse_free(text):
    """Free prose (local lists, appraisals): normalise '19th century', 'C 1830', 'twentieth century' to the listing idiom."""
    t = re.sub(r"\b(1[2-9]|20)(?:st|nd|rd|th)[- ]?[Cc](?:entury)?\b", r"C\1", text)
    t = re.sub(r"\b(" + "|".join(ORD) + r")[- ]century\b", lambda m: f"C{ORD[m.group(1).lower()]}", t, flags=re.I)
    t = re.sub(r"\bC\s(1[2-9]\d\d)\b", r"c.\1", t)
    t = re.sub(r"\b(early|mid|late)[- ]to[- ](?:early|mid|late)[- ]C", r"\1 C", t, flags=re.I)
    t = re.sub(r"\b(1[2-9]\d\d|20[0-2]\d)\b", r"\1", t)
    return parse("II " + t)
