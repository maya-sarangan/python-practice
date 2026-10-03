"""The quest registry: worlds, titles, test cases and hints.

Grown-ups: this is the answer-checking data. One entry per quest:

    7: {
        "world":     which world it belongs to,
        "title":     the quest name shown to the student,
        "one_liner": a single sentence describing the job,
        "module":    file name inside quests/ and solutions/ (no .py),
        "func":      the function the student must write,
        "cases":     list of (args_tuple, expected_value),
        "hints":     list of hint strings, gentlest first,
        "playable":  True if quests/<module>.py also has a demo() to play,
        "custom":    optional checker(func, module) -> list of check tuples,
    }

A "custom" checker returns tuples of
    (label, passed, got, want, was_error)
so a quest can test things a simple input/output table cannot -- such as
"did you leave the original list alone?".

After editing anything in here, run `python3 practice.py check`. It runs every
worked solution against every case and must report N/N.
"""


class Approx(object):
    """Wrap an expected number when tiny floating point wobble is fine."""

    def __init__(self, value, tolerance=1e-6):
        self.value = value
        self.tolerance = tolerance

    def matches(self, got):
        try:
            return abs(got - self.value) <= self.tolerance
        except TypeError:
            return False

    def describe(self):
        return repr(self.value) + " (about)"


WORLDS = [
    {
        "number": 1,
        "name": "The Wizard's Backpack",
        "badge": "🎒",
        "teaches": "variables, data types, type casting, f-strings",
    },
    {
        "number": 2,
        "name": "Word Wizardry",
        "badge": "🔤",
        "teaches": "slicing, string methods, ord() and chr()",
    },
    {
        "number": 3,
        "name": "Number Ninjas",
        "badge": "🔢",
        "teaches": "// and %, **, round(), abs(), number formatting",
    },
    {
        "number": 4,
        "name": "True or False Island",
        "badge": "🧭",
        "teaches": "comparisons, if/elif/else, and/or/not, truthy and falsy",
    },
    {
        "number": 5,
        "name": "The Function Factory",
        "badge": "🏭",
        "teaches": "parameters, return values, defaults, local vs global scope",
    },
    {
        "number": 6,
        "name": "Treasure Chests",
        "badge": "🧰",
        "teaches": "lists, tuples, indexing, slicing, unpacking, list methods",
    },
    {
        "number": 7,
        "name": "The Loop Lair",
        "badge": "🌀",
        "teaches": "for, while, range(), break, continue, for/else, nesting",
    },
    {
        "number": 8,
        "name": "Power-Up Palace",
        "badge": "⚡",
        "teaches": "enumerate(), zip(), comprehensions, map, filter, sum, lambda",
    },
]


def _build():
    from checks import world1, world2, world3, world4
    from checks import world5, world6, world7, world8

    quests = {}
    for module in (world1, world2, world3, world4,
                   world5, world6, world7, world8):
        for quest_id, spec in module.QUESTS.items():
            if quest_id in quests:
                raise RuntimeError("duplicate quest id " + str(quest_id))
            quests[quest_id] = spec
    return quests


QUESTS = _build()


def quest_ids():
    return sorted(QUESTS)
