"""Local lists: buildings a borough values though the State has not listed them (Open Government Licence).
Lambeth publishes the description in its GIS layer; Southwark one PDF per entry, fetched here (one a second, cached
in data/raw/ages/southwark/) and turned to text with pdftotext. Camden's and Hackney's lists carry no dates."""
import json
import subprocess
import time
from pathlib import Path

import requests

from .city import UA

OUT = Path("data/raw/ages/southwark")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    feats = json.load(open("data/raw/ages/southwark_local_list.geojson"))["features"]
    for f in feats:
        url, nid = f["properties"].get("Local_List"), f["properties"]["ID"]
        txt = OUT / f"{nid}.txt"
        if not url or txt.exists():
            continue
        r = requests.get(url.replace(" ", "%20"), headers=UA, timeout=60)
        if r.ok and r.content[:4] == b"%PDF":
            pdf = OUT / f"{nid}.pdf"
            pdf.write_bytes(r.content)
            subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=False)
            pdf.unlink()
        time.sleep(1.0)
    print(len(list(OUT.glob("*.txt"))), "Southwark entries as text")


if __name__ == "__main__":
    main()
