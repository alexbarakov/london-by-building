"""Check every 'Did you know' fact against its article and attach it to its building (web/data/facts.json)."""
import json
from pathlib import Path

from .facts import FACTS
from .s08_curated import article, place


def main():
    out, dropped = {}, []
    for ref, en, checks, qid, *nhle in FACTS:
        text, url = article(ref)
        missing = [c for c in checks if c.lower() not in text.lower()]
        bags, how = place(qid, nhle[0] if nhle else None)
        if missing or not bags:
            dropped.append((ref, missing, how))
            continue
        for bag in bags:
            out[bag] = {"en": en, "nl": en, "source": url}
    Path("web/data/facts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"{len(FACTS) - len(dropped)}/{len(FACTS)} facts on {len(out)} buildings")
    for d in dropped:
        print("dropped:", d)


if __name__ == "__main__":
    main()
