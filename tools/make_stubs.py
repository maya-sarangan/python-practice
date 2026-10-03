#!/usr/bin/env python3
"""Generate the student-facing quest stubs in quests/ from the registry.

Why a generator? Because the examples printed in a quest file must never
disagree with the examples the grader actually checks. Both come from
checks/world*.py, so they cannot drift apart.

    python3 tools/make_stubs.py              # create any missing stubs
    python3 tools/make_stubs.py --force      # rewrite every stub (DESTRUCTIVE:
                                             # this wipes student answers)
    python3 tools/make_stubs.py 69 70 71     # only these quest numbers

Existing files are never touched unless you pass --force.
"""

import inspect
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import importlib  # noqa: E402

from checks.registry import QUESTS, WORLDS, Approx, quest_ids  # noqa: E402
from checks.stories import STORIES  # noqa: E402

QUEST_DIR = os.path.join(HERE, "quests")
SOLUTION_DIR = os.path.join(HERE, "solutions")

WORLD_BY_NUMBER = dict((w["number"], w) for w in WORLDS)


def wrap(text, width, indent):
    """Dependency-free paragraph wrapper (textwrap would also be fine)."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if len(candidate) > width and current:
            lines.append(indent + current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(indent + current)
    return lines


def render_example(func_name, args, want):
    call = func_name + "(" + ", ".join(repr(a) for a in args) + ")"
    if isinstance(want, Approx):
        shown = repr(want.value) + "  (close enough is fine)"
    else:
        shown = repr(want)
    return call + "  ->  " + shown


def multiline_preview(want):
    """For answers that are several lines, show what they actually look like."""
    if not isinstance(want, str) or "\n" not in want:
        return []
    out = ["", "    which looks like this:", ""]
    for line in want.split("\n"):
        out.append("        " + line)
    return out


def example_block(spec):
    lines = []
    custom_examples = spec.get("examples")
    if custom_examples:
        for example in custom_examples:
            lines.append("    " + example)
        return lines

    rendered = [render_example(spec["func"], args, want)
                for args, want in spec["cases"][:5]]
    # Line the arrows up so the examples read as a table.
    widest = max(len(r.split("  ->  ")[0]) for r in rendered)
    for row in rendered:
        call, shown = row.split("  ->  ", 1)
        lines.append("    " + call.ljust(widest) + "  ->  " + shown)

    preview = [c for c in spec["cases"]
               if isinstance(c[1], str) and "\n" in c[1]]
    if preview:
        lines.extend(multiline_preview(preview[0][1]))
    return lines


def solution_pieces(spec):
    """Signature and demo() source, read straight from the answer key."""
    module = importlib.import_module("solutions." + spec["module"])
    func = getattr(module, spec["func"])
    signature = str(inspect.signature(func))
    demo_source = None
    if spec.get("playable"):
        demo = getattr(module, "demo", None)
        if demo is not None:
            demo_source = inspect.getsource(demo)
    return signature, demo_source


def build_stub(quest_id):
    spec = QUESTS[quest_id]
    world = WORLD_BY_NUMBER[spec["world"]]
    signature, demo_source = solution_pieces(spec)

    number = str(quest_id).zfill(2)
    header = ("Quest " + number + " -- " + spec["title"]
              + "   [World " + str(world["number"]) + ": " + world["name"] + "]")

    lines = ["@@DOCSTRING_OPEN@@" + header, ""]
    lines.extend(wrap(STORIES[quest_id], 72, ""))
    lines.append("")
    lines.append("YOUR MISSION")
    lines.extend(wrap(spec["one_liner"], 68, "    "))
    lines.append("")
    lines.append("EXAMPLES")
    lines.extend(example_block(spec))
    lines.append("")
    lines.append("WHEN YOU ARE READY")
    lines.append("    python3 practice.py " + str(quest_id)
                 + "            grade it")
    lines.append("    python3 practice.py " + str(quest_id)
                 + " --hint     ask for a nudge")
    if spec.get("playable"):
        lines.append("    python3 practice.py " + str(quest_id)
                     + " --play     play with it once it works 🎮")
    lines.append('"""')

    preamble = spec.get("preamble")
    if preamble:
        lines.append("")
        lines.append(preamble)

    lines.append("")
    lines.append("")
    lines.append("def " + spec["func"] + signature + ":")
    lines.append("    # 👇 Delete the line below, then write your answer here.")
    lines.append("    raise NotImplementedError")

    if demo_source:
        lines.append("")
        lines.append("")
        lines.append("# This part is a gift -- it is already written for you.")
        lines.append("# Finish the function above, then run it with --play.")
        lines.append(demo_source.rstrip())

    body = "\n".join(lines) + "\n"
    # A raw docstring keeps escape sequences such as \n visible to the student
    # instead of letting Python turn them into real newlines.
    opener = 'r"""' if "\\" in body.split('"""')[0] else '"""'
    return body.replace("@@DOCSTRING_OPEN@@", opener, 1)


def main(argv):
    force = "--force" in argv
    wanted = [int(a) for a in argv if a.isdigit()]
    targets = wanted if wanted else quest_ids()

    if not os.path.isdir(QUEST_DIR):
        os.makedirs(QUEST_DIR)

    written = 0
    skipped = 0
    for quest_id in targets:
        spec = QUESTS[quest_id]
        path = os.path.join(QUEST_DIR, spec["module"] + ".py")
        if os.path.exists(path) and not force:
            skipped += 1
            continue
        with open(path, "w") as handle:
            handle.write(build_stub(quest_id))
        written += 1

    print("wrote " + str(written) + " stub(s), left " + str(skipped)
          + " existing file(s) alone")
    if skipped and not force:
        print("(pass --force to overwrite -- that erases student answers)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
