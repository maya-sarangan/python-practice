"""World 6 -- Treasure Chests. Lists, tuples, indexing, slicing, unpacking."""


def _plain(func, name, cases):
    """Run ordinary (args -> expected) cases and return check tuples."""
    from practice import values_match, call_signature
    out = []
    for args, want in cases:
        label = call_signature(name, args)
        try:
            got = func(*args)
        except NotImplementedError:
            raise
        except Exception as exc:
            out.append((label, False,
                        (type(exc).__name__ + ": " + str(exc),
                         type(exc).__name__),
                        want, True))
            continue
        out.append((label, values_match(got, want), got, want, False))
    return out


_DROP_CASES = [
    ((["sword", "apple", "apple"], "apple"), ["sword", "apple"]),
    ((["sword"], "shield"), ["sword"]),
    ((["a", "b", "c"], "a"), ["b", "c"]),
    (([], "anything"), []),
]


def _check_drop_item(func, module):
    checks = _plain(func, "drop_item", _DROP_CASES)
    original = ["potion", "rope", "potion"]
    func(original, "potion")
    checks.append((
        "the list you were given is left untouched",
        original == ["potion", "rope", "potion"],
        original, ["potion", "rope", "potion"], False,
    ))
    return checks


_SQUAD_CASES = [
    ((["Bo", "Cy"], ["Dee"], "Ana"), ["Ana", "Bo", "Cy", "Dee"]),
    (([], [], "Solo"), ["Solo"]),
    ((["X"], ["Y", "Z"], "Cap"), ["Cap", "X", "Y", "Z"]),
]


def _check_build_squad(func, module):
    checks = _plain(func, "build_squad", _SQUAD_CASES)
    core = ["Bo", "Cy"]
    extras = ["Dee"]
    func(core, extras, "Ana")
    checks.append((
        "the core list is left untouched",
        core == ["Bo", "Cy"], core, ["Bo", "Cy"], False,
    ))
    checks.append((
        "the extras list is left untouched",
        extras == ["Dee"], extras, ["Dee"], False,
    ))
    return checks


QUESTS = {
    44: {
        "world": 6,
        "title": "First and Last",
        "one_liner": "Return the first and last item of a list as a tuple.",
        "module": "q44_top_and_bottom",
        "func": "top_and_bottom",
        "cases": [
            ((["a", "b", "c"],), ("a", "c")),
            ((["solo"],), ("solo", "solo")),
            (([1, 2, 3, 4, 5],), (1, 5)),
        ],
        "hints": [
            "items[0] is the first one.",
            "items[-1] is the last one, however long the list is.",
            "Return them both at once: return (items[0], items[-1])",
        ],
    },
    45: {
        "world": 6,
        "title": "The Second Half",
        "one_liner": "Slice off the back half of a list. Odd lengths lean right.",
        "module": "q45_second_half",
        "func": "second_half",
        "cases": [
            (([1, 2, 3, 4],), [3, 4]),
            (([1, 2, 3],), [2, 3]),
            (([1, 2, 3, 4, 5, 6],), [4, 5, 6]),
            ((["a"],), ["a"]),
            (([],), []),
        ],
        "hints": [
            "len(items) // 2 is the middle, rounded down.",
            "items[3:] means 'from spot 3 all the way to the end'.",
            "Put those two ideas together in one slice.",
        ],
    },
    46: {
        "world": 6,
        "title": "Skip a Step",
        "one_liner": "Take every other item, starting with the very first.",
        "module": "q46_every_other",
        "func": "every_other",
        "cases": [
            (([1, 2, 3, 4, 5],), [1, 3, 5]),
            ((["a", "b", "c", "d"],), ["a", "c"]),
            (([7],), [7]),
            (([],), []),
        ],
        "hints": [
            "A slice has a third part: items[start:stop:step].",
            "A step of 2 hops over every second item.",
            "Leave start and stop empty to cover the whole list.",
        ],
    },
    47: {
        "world": 6,
        "title": "Potion Swap",
        "one_liner": "Hand back two values in the opposite order. One line is enough.",
        "module": "q47_swap_potions",
        "func": "swap_potions",
        "cases": [
            ((1, 2), (2, 1)),
            (("red", "blue"), ("blue", "red")),
            ((True, False), (False, True)),
        ],
        "hints": [
            "A tuple is just values separated by commas: (b, a).",
            "You do not need a temporary variable. Python can do it in one go.",
        ],
    },
    48: {
        "world": 6,
        "title": "Drop One Item",
        "one_liner": "Remove the first matching item, but leave the original list alone.",
        "module": "q48_drop_item",
        "func": "drop_item",
        "cases": [],
        "custom": _check_drop_item,
        "examples": [
            "drop_item(['sword', 'apple', 'apple'], 'apple')  ->  ['sword', 'apple']",
            "drop_item(['sword'], 'shield')                   ->  ['sword']",
            "drop_item([], 'anything')                        ->  []",
            "...and the list you were handed must NOT change.",
        ],
        "hints": [
            "inventory[:] or list(inventory) makes a fresh copy of the list.",
            "Only remove if the item is actually in there -- "
            "use if item in copy.",
            ".remove() takes out the FIRST match and changes the list "
            "in place, so call it on your copy, not the original.",
        ],
    },
    49: {
        "world": 6,
        "title": "Leaderboard",
        "one_liner": "Put the scores in order, highest first, as a brand new list.",
        "module": "q49_leaderboard",
        "func": "leaderboard",
        "cases": [
            (([3, 9, 1],), [9, 3, 1]),
            (([2, 2, 1],), [2, 2, 1]),
            (([5],), [5]),
            (([],), []),
            (([-1, -5, 0],), [0, -1, -5]),
        ],
        "hints": [
            "sorted(scores) builds a NEW sorted list and leaves the old one "
            "alone. scores.sort() changes the original.",
            "sorted() takes an extra setting: reverse=True flips the order.",
        ],
    },
    50: {
        "world": 6,
        "title": "Chest Inspector",
        "one_liner": "Report how many of an item are in the chest and where the first one sits.",
        "module": "q50_inventory_report",
        "func": "inventory_report",
        "cases": [
            ((["apple", "sword", "apple"], "apple"),
             "2 x apple, first one at slot 0"),
            ((["a", "b", "c"], "c"), "1 x c, first one at slot 2"),
            ((["apple", "sword"], "shield"), "No shield in the chest."),
            (([], "gold"), "No gold in the chest."),
        ],
        "hints": [
            "item in inventory tells you whether it is there at all. "
            "Deal with the missing case first.",
            "inventory.count(item) counts the copies.",
            "inventory.index(item) finds the slot of the first one -- "
            "but it crashes if the item is missing, which is exactly why "
            "you check first.",
        ],
    },
    51: {
        "world": 6,
        "title": "X Marks the Spot",
        "one_liner": "Dig into a list of lists and bring back one square of the map.",
        "module": "q51_dig_here",
        "func": "dig_here",
        "cases": [
            (([["a", "b"], ["c", "d"]], 1, 0), "c"),
            (([[1, 2, 3], [4, 5, 6]], 0, 2), 3),
            (([["x"]], -1, -1), "x"),
            (([["sand", "sand"], ["sand", "gold"]], 1, 1), "gold"),
        ],
        "hints": [
            "grid[row] hands you a whole row, which is itself a list.",
            "So put a second pair of brackets straight after it to pick "
            "one square out of that row.",
        ],
    },
    52: {
        "world": 6,
        "title": "Assemble the Squad",
        "one_liner": "Leader at the front, extras on the end, originals untouched.",
        "module": "q52_build_squad",
        "func": "build_squad",
        "cases": [],
        "custom": _check_build_squad,
        "examples": [
            "build_squad(['Bo', 'Cy'], ['Dee'], 'Ana')  ->  ['Ana', 'Bo', 'Cy', 'Dee']",
            "build_squad([], [], 'Solo')                ->  ['Solo']",
            "...and neither list you were handed may change.",
        ],
        "hints": [
            "Start with a copy: squad = list(core).",
            "squad.insert(0, leader) pushes the leader into the front spot.",
            ".extend(extras) adds every extra on the end. "
            "(.append(extras) would bury the whole list inside as one item!)",
            "Remember to return squad at the end.",
        ],
    },
    53: {
        "world": 6,
        "title": "Unpack the Profile",
        "one_liner": "Pull a nested profile apart into named variables, then describe it.",
        "module": "q53_unpack_profile",
        "func": "unpack_profile",
        "cases": [
            ((["Zara", 11, ["python", "art"]],),
             "Zara (11) likes python and art"),
            ((["Bo", 9, ["football", "chess"]],),
             "Bo (9) likes football and chess"),
            ((["Ada", 36, ["maths", "machines"]],),
             "Ada (36) likes maths and machines"),
        ],
        "hints": [
            "You can unpack a list straight into variables: "
            "name, age, hobbies = profile",
            "hobbies is itself a list of two things, so you can unpack "
            "that too: first, second = hobbies",
            "Then build the sentence with an f-string.",
        ],
    },
    54: {
        "world": 6,
        "title": "Captain and the Rest",
        "one_liner": "Split a team into its captain and everybody else.",
        "module": "q54_rest_of_the_team",
        "func": "rest_of_the_team",
        "cases": [
            ((["Ana", "Bo", "Cy"],), ("Ana", ["Bo", "Cy"])),
            ((["Solo"],), ("Solo", [])),
            (([1, 2, 3, 4],), (1, [2, 3, 4])),
        ],
        "hints": [
            "The star operator scoops up everything left over: "
            "captain, *rest = players",
            "rest is always a list, even when it ends up empty.",
            "Return the two of them as a tuple.",
        ],
    },
}
