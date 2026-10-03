#!/usr/bin/env python3
"""Pull the real concept list for a freeCodeCamp section, straight from source.

The freeCodeCamp website is rendered by JavaScript, so fetching the /learn/
URL gives you nothing useful. The curriculum itself lives in the public
freeCodeCamp repository, and every module ends with a "review" block that
lists every concept that module taught. That review block is the single best
description of what a student is now allowed to be asked about.

    python3 tools/fcc_lesson.py modules
        List every module of the python-v9 certification and its blocks,
        so you can see which review block belongs to which lesson.

    python3 tools/fcc_lesson.py review review-dictionaries-and-sets
        Print the full review markdown for one block.

    python3 tools/fcc_lesson.py concepts review-dictionaries-and-sets
        Print just the concept headings and bullet titles -- the compact
        inventory to paste into CURRICULUM.md.

Needs network access to raw.githubusercontent.com and api.github.com.
"""

import json
import sys
import urllib.request

RAW = "https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/"
API = "https://api.github.com/repos/freeCodeCamp/freeCodeCamp/contents/"
SUPERBLOCK = "curriculum/structure/superblocks/python-v9.json"
BLOCKS = "curriculum/challenges/english/blocks/"


def fetch(url):
    request = urllib.request.Request(
        url, headers={"User-Agent": "python-practice-lesson-tool"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def cmd_modules():
    data = json.loads(fetch(RAW + SUPERBLOCK))
    for chapter in data.get("chapters", []):
        for module in chapter.get("modules", []):
            print(module["dashedName"])
            for block in module.get("blocks", []):
                marker = "  <-- review block" if block.startswith("review-") else ""
                print("    " + block + marker)
            print("")
    return 0


def _review_url(block):
    listing = json.loads(fetch(API + BLOCKS + block))
    if not isinstance(listing, list) or not listing:
        raise SystemExit("no files found for block " + block)
    return listing[0]["download_url"]


def cmd_review(block):
    print(fetch(_review_url(block)))
    return 0


def cmd_concepts(block):
    text = fetch(_review_url(block))
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("## "):
            print("")
            print(stripped)
        elif stripped.startswith("- **"):
            # "- **append()**: Used to add..." -> "    - append()"
            name = stripped[4:].split("**", 1)[0]
            print("    - " + name)
    print("")
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    command = argv[0]
    if command == "modules":
        return cmd_modules()
    if command in ("review", "concepts"):
        if len(argv) < 2:
            print("which block? e.g. review-loops-and-sequences")
            return 2
        return cmd_review(argv[1]) if command == "review" \
            else cmd_concepts(argv[1])
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
