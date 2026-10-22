#!/usr/bin/env python3
"""Fill the Hub process map template with one business's map JSON.

    python3 fill_map.py map.json quoting-map.html

The template (../map-template.html) holds the layout; this only swaps the data block, so every
member's map looks the same. Fields are in ../README.md.
"""
import json
import re
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "map-template.html"
BLOCK = re.compile(r'(<script type="application/json" id="map-data">)(.*?)(</script>)', re.S)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: fill_map.py map.json out.html")
    data = json.loads(Path(sys.argv[1]).read_text())
    if not data.get("steps"):
        raise SystemExit("map.json has no steps")
    payload = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    html = TEMPLATE.read_text()
    if not BLOCK.search(html):
        raise SystemExit("template has no map-data block")
    out = BLOCK.sub(lambda m: m.group(1) + "\n" + payload + "\n" + m.group(3), html, count=1)
    Path(sys.argv[2]).write_text(out)
    print(sys.argv[2])


if __name__ == "__main__":
    main()
