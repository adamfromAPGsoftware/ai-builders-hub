"""Copy the shared process map into every mapping skill that uses it.

Run from the repo root after changing anything in plugins/trade-intake/shared/map/:

    python3 tools/sync_map.py          # copy
    python3 tools/sync_map.py --check  # exit 1 if any copy is out of date

A skill can be added to Claude on its own (as a zip), so each one carries its own copy in
<skill>/map/. Edit plugins/trade-intake/shared/map/, never a copy.
"""
import filecmp
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "plugins" / "trade-intake" / "shared" / "map"
SKILLS = ROOT / "plugins" / "trade-intake" / "skills"
USERS = ["map-leads", "map-customer-service", "map-admin"]   # add each mapping skill as it moves to the shared map
SKIP = {"examples", "__pycache__"}


def files(base):
    return sorted(p.relative_to(base) for p in base.rglob("*")
                  if p.is_file() and not SKIP.intersection(p.relative_to(base).parts))


def stale(dest):
    want, have = files(SHARED), files(dest) if dest.exists() else []
    if want != have:
        return True
    return any(not filecmp.cmp(SHARED / f, dest / f, shallow=False) for f in want)


def main():
    check = "--check" in sys.argv
    bad = []
    for name in USERS:
        dest = SKILLS / name / "map"
        if not stale(dest):
            continue
        if check:
            bad.append(name)
            continue
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SHARED, dest, ignore=shutil.ignore_patterns(*SKIP))
        print(f"copied the map into {name}/map")
    if bad:
        print("out of date: " + ", ".join(bad) + ". Run python3 tools/sync_map.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
