#!/usr/bin/env python3
"""The Quest Console -- your grader, cheerleader and quest map.

Run me like this:

    python3 practice.py              # show the quest map
    python3 practice.py next         # jump to the next unfinished quest
    python3 practice.py 7            # grade quest 7
    python3 practice.py 7 --hint     # ask for hints on quest 7
    python3 practice.py 7 --play     # play quest 7 (if it has a game)
    python3 practice.py world 2      # grade every quest in World 2
    python3 practice.py all          # grade everything
    python3 practice.py report       # progress report
    python3 practice.py check        # (grown-ups) prove every answer key works
"""

import argparse
import importlib
import io
import os
import random
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from checks.registry import QUESTS, WORLDS, Approx, quest_ids  # noqa: E402

# --------------------------------------------------------------------------
# Colour, but only when a human is watching.
# --------------------------------------------------------------------------

_USE_COLOUR = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


def _c(code, text):
    if not _USE_COLOUR:
        return text
    return "\033[" + code + "m" + text + "\033[0m"


def bold(t):
    return _c("1", t)


def dim(t):
    return _c("2", t)


def green(t):
    return _c("32", t)


def red(t):
    return _c("31", t)


def yellow(t):
    return _c("33", t)


def cyan(t):
    return _c("36", t)


def magenta(t):
    return _c("35", t)


# --------------------------------------------------------------------------
# Loading a quest
# --------------------------------------------------------------------------


class QuestMissing(Exception):
    pass


def _module_name(quest_id, package):
    spec = QUESTS[quest_id]
    return package + "." + spec["module"]


def load_function(quest_id, package="quests"):
    """Import a quest module fresh and hand back the function under test."""
    spec = QUESTS[quest_id]
    name = _module_name(quest_id, package)
    if name in sys.modules:
        module = importlib.reload(sys.modules[name])
    else:
        try:
            module = importlib.import_module(name)
        except ImportError as exc:
            raise QuestMissing(str(exc))
    try:
        return getattr(module, spec["func"]), module
    except AttributeError:
        raise QuestMissing(
            "Quest " + str(quest_id) + " needs a function called "
            + spec["func"] + "() but I could not find one in " + name + ".py"
        )


# --------------------------------------------------------------------------
# Comparing answers
# --------------------------------------------------------------------------


def values_match(got, want):
    if isinstance(want, Approx):
        return want.matches(got)
    # Keep True/1 and False/0 from being treated as the same answer.
    if isinstance(want, bool) or isinstance(got, bool):
        return isinstance(got, bool) and isinstance(want, bool) and got == want
    if isinstance(want, float) or isinstance(got, float):
        try:
            return abs(got - want) < 1e-9
        except TypeError:
            return False
    return type(got) == type(want) and got == want


def show(value):
    """Print a value the way a kid would recognise it."""
    if isinstance(value, Approx):
        return value.describe()
    if isinstance(value, str):
        if "\n" in value:
            return "\n        " + "\n        ".join(
                repr(line) for line in value.split("\n")
            )
        return repr(value)
    return repr(value)


def call_signature(func_name, args):
    return func_name + "(" + ", ".join(repr(a) for a in args) + ")"


# --------------------------------------------------------------------------
# Friendly error translations
# --------------------------------------------------------------------------

ERROR_HELP = {
    "IndexError": "You reached for a spot in a list or string that is not there. "
    "Remember the first spot is 0 and the last is -1.",
    "TypeError": "You mixed two kinds of things that do not go together -- "
    "like adding text to a number. Try int(), float() or str().",
    "ValueError": "The right kind of thing, but the wrong value -- "
    "for example int('cat') cannot work.",
    "ZeroDivisionError": "Nothing can be divided by zero. Check for 0 before you divide.",
    "NameError": "Python does not know that name. Is it a typo, or did you forget to "
    "create the variable first?",
    "AttributeError": "That method does not exist on that kind of value. "
    "Lists and strings have different powers!",
    "KeyError": "You asked for a key that is not in there.",
    "RecursionError": "Your function keeps calling itself forever. "
    "Does your loop or function ever stop?",
    "UnboundLocalError": "You used a variable inside a function before giving it a value. "
    "If it lives outside the function you may need the global keyword.",
    "IndentationError": "The spaces at the start of your lines do not line up. "
    "Everything inside a loop or function needs the same indent.",
    "SyntaxError": "Python could not read your code. Look for a missing ':' , "
    "quote or bracket on the line it mentions.",
}


# --------------------------------------------------------------------------
# Running one quest
# --------------------------------------------------------------------------

CHEERS = [
    "Nailed it!",
    "Flawless.",
    "That is some fine code.",
    "Quest complete!",
    "You made that look easy.",
    "Perfect run!",
]

ALMOST = [
    "So close!",
    "Nearly there!",
    "One more push!",
    "You are on the right track.",
]

JUST_STARTED = [
    "Every expert started here. Read the first failing line carefully.",
    "No shame in a red run -- that is how you find out what to change.",
    "Compare what you gave with what I wanted. The difference is the clue.",
]


class Result(object):
    def __init__(self, quest_id):
        self.quest_id = quest_id
        self.passed = 0
        self.failed = 0
        self.not_started = False
        self.missing = None
        self.lines = []

    @property
    def total(self):
        return self.passed + self.failed

    @property
    def complete(self):
        return self.failed == 0 and self.passed > 0 and not self.not_started

    @property
    def icon(self):
        if self.missing:
            return "🚧"
        if self.not_started:
            return "⬜"
        if self.complete:
            return "✅"
        if self.passed:
            return "🔶"
        return "❌"


def run_quest(quest_id, package="quests", verbose=True, out=None):
    out = out if out is not None else sys.stdout
    spec = QUESTS[quest_id]
    result = Result(quest_id)

    def say(text=""):
        if verbose:
            out.write(text + "\n")

    try:
        func, module = load_function(quest_id, package)
    except QuestMissing as exc:
        result.missing = str(exc)
        say(red("🚧 " + str(exc)))
        return result

    say("")
    say(bold("🎯 Quest " + str(quest_id).zfill(2) + " -- " + spec["title"]))
    say(dim("   " + spec["one_liner"]))
    say("")

    cases = spec["cases"]
    custom = spec.get("custom")
    if custom is not None:
        try:
            checks = custom(func, module)
        except NotImplementedError:
            checks = []
            result.not_started = True
    else:
        checks = []
        for args, want in cases:
            label = call_signature(spec["func"], args)
            try:
                got = func(*args)
            except NotImplementedError:
                result.not_started = True
                break
            except Exception:
                checks.append((label, False, _exception_blurb(), want, True))
                continue
            checks.append((label, values_match(got, want), got, want, False))

    if result.not_started:
        say(yellow("   ⬜ Not started yet."))
        say("")
        say("   Open " + cyan("quests/" + spec["module"] + ".py") + ", delete the")
        say("   " + dim("raise NotImplementedError") + " line, and write your code.")
        say("")
        return result

    for label, ok, got, want, was_error in checks:
        if ok:
            result.passed += 1
            say("   " + green("✅ ") + label + dim("  ->  ") + show(want))
        else:
            result.failed += 1
            say("   " + red("❌ ") + label)
            if was_error:
                say("      " + red("your code crashed: ") + got[0])
                help_text = ERROR_HELP.get(got[1])
                if help_text:
                    say("      " + yellow("💡 " + help_text))
            else:
                say("      " + dim("you gave:  ") + show(got))
                say("      " + dim("I wanted:  ") + show(want))

    say("")
    if result.complete:
        say("   " + green(bold(str(result.passed) + "/" + str(result.total) + " passed"))
            + "  " + green(random.choice(CHEERS)) + " 🎉")
    else:
        mood = ALMOST if result.passed else JUST_STARTED
        say("   " + yellow(bold(str(result.passed) + "/" + str(result.total) + " passed"))
            + "  " + yellow(random.choice(mood)))
        hints = spec.get("hints") or []
        if hints:
            say("")
            say("   " + magenta("💡 Hint: ") + hints[0])
            if len(hints) > 1:
                say("   " + dim("(more hints: python3 practice.py "
                                + str(quest_id) + " --hint)"))
    say("")
    return result


def _exception_blurb():
    exc_type, exc_value, _tb = sys.exc_info()
    name = exc_type.__name__
    return (name + ": " + str(exc_value), name)


# --------------------------------------------------------------------------
# Quiet status, used by the map and the report
# --------------------------------------------------------------------------


def quiet_result(quest_id, package="quests"):
    sink = io.StringIO()
    try:
        return run_quest(quest_id, package=package, verbose=False, out=sink)
    except Exception:
        result = Result(quest_id)
        result.missing = "could not run"
        return result


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------


def cmd_map():
    results = {}
    for qid in quest_ids():
        results[qid] = quiet_result(qid)

    done = sum(1 for r in results.values() if r.complete)
    total = len(results)

    print("")
    print(bold("  🐍  P Y T H O N   Q U E S T   M A P"))
    print("")
    print("  " + progress_bar(done, total) + "  "
          + bold(str(done) + "/" + str(total)) + " quests complete")

    for world in WORLDS:
        ids = [q for q in quest_ids() if QUESTS[q]["world"] == world["number"]]
        world_done = sum(1 for q in ids if results[q].complete)
        header = ("  " + world["badge"] + "  World " + str(world["number"]) + ": "
                  + world["name"])
        tally = " (" + str(world_done) + "/" + str(len(ids)) + ")"
        print("")
        print(bold(header) + dim(tally))
        print("     " + dim(world["teaches"]))
        for qid in ids:
            spec = QUESTS[qid]
            r = results[qid]
            line = ("     " + r.icon + " " + str(qid).zfill(2) + "  "
                    + spec["title"])
            if spec.get("playable"):
                line += dim("  🎮")
            print(line)

    print("")
    print(dim("  ✅ done   🔶 partly   ❌ failing   ⬜ not started   🎮 playable"))
    print("  Next up: " + cyan("python3 practice.py next"))
    print("")
    return 0


def progress_bar(done, total, width=24):
    if total == 0:
        return ""
    filled = int(round(width * done / float(total)))
    bar = "█" * filled + "░" * (width - filled)
    pct = int(round(100 * done / float(total)))
    return green(bar) + " " + str(pct).rjust(3) + "%"


def cmd_next():
    for qid in quest_ids():
        r = quiet_result(qid)
        if not r.complete:
            spec = QUESTS[qid]
            print("")
            print(bold("  Next quest: " + str(qid).zfill(2) + " -- " + spec["title"]))
            print("  " + spec["one_liner"])
            print("")
            print("  File:  " + cyan("quests/" + spec["module"] + ".py"))
            print("  Grade: " + cyan("python3 practice.py " + str(qid)))
            print("")
            return 0
    print("")
    print(green(bold("  🏆 Every quest complete. You are a Python wizard.")))
    print("")
    return 0


def cmd_one(quest_id, hint=False, play=False, solution=False):
    if quest_id not in QUESTS:
        print(red("There is no quest " + str(quest_id) + " yet."))
        return 2
    spec = QUESTS[quest_id]

    if hint:
        hints = spec.get("hints") or ["No hints for this one -- you have got this!"]
        print("")
        print(bold("💡 Hints for quest " + str(quest_id).zfill(2)
                   + " -- " + spec["title"]))
        for i, h in enumerate(hints, 1):
            print("   " + str(i) + ". " + h)
        print("")
        return 0

    if play:
        if not spec.get("playable"):
            print("Quest " + str(quest_id) + " is not a playable one. "
                  "Look for 🎮 on the map.")
            return 2
        try:
            _func, module = load_function(quest_id)
        except QuestMissing as exc:
            print(red(str(exc)))
            return 2
        demo = getattr(module, "demo", None)
        if demo is None:
            print(red("That quest has no demo() function."))
            return 2
        try:
            demo()
        except NotImplementedError:
            print(yellow("Finish the quest first, then come back and play it!"))
            return 1
        except KeyboardInterrupt:
            print("\nBye!")
        return 0

    package = "solutions" if solution else "quests"
    result = run_quest(quest_id, package=package)
    return 0 if result.complete else 1


def cmd_many(ids, solution=False, title="Grading"):
    package = "solutions" if solution else "quests"
    results = []
    for qid in ids:
        results.append(run_quest(qid, package=package))
    done = [r for r in results if r.complete]
    print(bold("  " + title + " summary: ")
          + str(len(done)) + "/" + str(len(results)) + " quests fully passing")
    print("")
    return 0 if len(done) == len(results) else 1


def cmd_report():
    results = {}
    for qid in quest_ids():
        results[qid] = quiet_result(qid)
    done = [q for q in results if results[q].complete]
    started = [q for q in results if not results[q].complete
               and not results[q].not_started]
    print("")
    print(bold("  📊 Progress report"))
    print("")
    print("  " + progress_bar(len(done), len(results)))
    print("")
    print("  Complete:     " + str(len(done)))
    print("  In progress:  " + str(len(started)))
    print("  Not started:  " + str(len(results) - len(done) - len(started)))
    if started:
        print("")
        print("  Stuck on:")
        for qid in started:
            r = results[qid]
            print("     🔶 " + str(qid).zfill(2) + "  " + QUESTS[qid]["title"]
                  + dim("  (" + str(r.passed) + "/" + str(r.total) + ")"))
    print("")
    for world in WORLDS:
        ids = [q for q in quest_ids() if QUESTS[q]["world"] == world["number"]]
        wd = sum(1 for q in ids if results[q].complete)
        print("  " + world["badge"] + " World " + str(world["number"]) + " "
              + world["name"].ljust(26) + " "
              + progress_bar(wd, len(ids), width=12))
    print("")
    return 0


def cmd_check():
    """Grown-up gate: every answer key must pass every check."""
    bad = []
    for qid in quest_ids():
        sink = io.StringIO()
        try:
            r = run_quest(qid, package="solutions", verbose=False, out=sink)
        except Exception:
            print(red("💥 quest " + str(qid) + " blew up while checking:"))
            traceback.print_exc()
            bad.append(qid)
            continue
        if not r.complete:
            bad.append(qid)
            print(red("❌ quest " + str(qid).zfill(2) + " "
                      + QUESTS[qid]["title"]))
            run_quest(qid, package="solutions", verbose=True)
    total = len(quest_ids())
    if bad:
        print(red(bold("ANSWER KEY BROKEN: " + str(len(bad)) + " of "
                       + str(total) + " quests fail -> " + repr(bad))))
        return 1
    print(green(bold("✅ answer key verified: " + str(total) + "/" + str(total)
                     + " quests pass all checks")))
    missing = _missing_quest_files()
    if missing:
        print(red("Missing quest stubs: " + repr(missing)))
        return 1
    print(green("✅ all " + str(total) + " quest stubs present"))
    return 0


def _missing_quest_files():
    missing = []
    for qid in quest_ids():
        path = os.path.join(HERE, "quests", QUESTS[qid]["module"] + ".py")
        if not os.path.exists(path):
            missing.append(qid)
    return missing


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("target", nargs="*", default=[])
    parser.add_argument("--hint", action="store_true")
    parser.add_argument("--play", action="store_true")
    parser.add_argument("--solution", action="store_true")
    parser.add_argument("-h", "--help", action="store_true")
    args = parser.parse_args(argv)

    if args.help:
        print(__doc__)
        return 0

    target = args.target
    if not target:
        return cmd_map()

    head = target[0].lower()

    if head in ("map", "quests", "list"):
        return cmd_map()
    if head == "next":
        return cmd_next()
    if head == "report":
        return cmd_report()
    if head == "check":
        return cmd_check()
    if head == "all":
        return cmd_many(quest_ids(), solution=args.solution, title="Full run")
    if head == "world":
        if len(target) < 2 or not target[1].isdigit():
            print("Which world? e.g. python3 practice.py world 2")
            return 2
        number = int(target[1])
        ids = [q for q in quest_ids() if QUESTS[q]["world"] == number]
        if not ids:
            print("There is no world " + str(number) + ".")
            return 2
        return cmd_many(ids, solution=args.solution,
                        title="World " + str(number))
    if head.isdigit():
        return cmd_one(int(head), hint=args.hint, play=args.play,
                       solution=args.solution)

    print("I did not understand that. Try: python3 practice.py --help")
    return 2


if __name__ == "__main__":
    sys.exit(main())
