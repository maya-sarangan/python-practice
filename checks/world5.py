"""World 5 -- The Function Factory. Parameters, returns, defaults, scope."""


def _check_spend(func, module):
    """Quest 43 needs more than input/output: the global must really change."""
    checks = []

    def record(label, got, want):
        ok = got == want and isinstance(got, type(want))
        checks.append((label, ok, got, want, False))

    start = getattr(module, "coins", None)
    checks.append((
        "the module starts with coins = 100",
        start == 100, start, 100, False,
    ))

    got = func(30)
    record("spend(30) returns the new balance", got, 70)
    record("after spend(30), coins is also 70", getattr(module, "coins", None), 70)

    got = func(70)
    record("spend(70) returns the new balance", got, 0)
    record("after spend(70), coins is also 0", getattr(module, "coins", None), 0)

    return checks


QUESTS = {
    38: {
        "world": 5,
        "title": "Greeter With a Spare Setting",
        "one_liner": "A greeting that works with one argument or two.",
        "module": "q38_greet",
        "func": "greet",
        "cases": [
            (("Zara",), "Hello, Zara!"),
            (("Zara", "Yo"), "Yo, Zara!"),
            (("Bo", "Greetings"), "Greetings, Bo!"),
            (("Ada",), "Hello, Ada!"),
        ],
        "hints": [
            "A default value goes in the function line itself: "
            "def greet(name, greeting=\"Hello\"):",
            "If the caller gives a second argument it wins. "
            "If not, Python quietly uses your default.",
        ],
    },
    39: {
        "world": 5,
        "title": "How Much Pizza Is That?",
        "one_liner": "Measure a pizza by area, not by width. Return the number.",
        "module": "q39_pizza_area",
        "func": "pizza_area",
        "cases": [
            ((10,), 78.54),
            ((12,), 113.1),
            ((2,), 3.14),
            ((0,), 0.0),
        ],
        "hints": [
            "The radius is half the diameter.",
            "Area is PI * radius ** 2. Use PI = 3.14159.",
            "return the number -- do not print it. "
            "A function that only prints returns None!",
        ],
    },
    40: {
        "world": 5,
        "title": "Discount Machine",
        "one_liner": "Knock a percentage off a price and hand back the new price.",
        "module": "q40_apply_discount",
        "func": "apply_discount",
        "cases": [
            ((100, 25), 75.0),
            ((59.99, 10), 53.99),
            ((40, 15), 34.0),
            ((20, 0), 20.0),
            ((80, 100), 0.0),
        ],
        "hints": [
            "25% off means you pay 75% of the price.",
            "percent / 100 turns 25 into 0.25. Then 1 - 0.25 is what you pay.",
            "Round the final answer to 2 decimal places.",
        ],
    },
    41: {
        "world": 5,
        "title": "Biggest of Three (No Cheating)",
        "one_liner": "Find the largest of three numbers without using max().",
        "module": "q41_biggest_of_three",
        "func": "biggest_of_three",
        "cases": [
            ((3, 9, 2), 9),
            ((10, 1, 1), 10),
            ((1, 2, 2), 2),
            ((4, 4, 4), 4),
            ((-5, -1, -9), -1),
            ((0, 0, -1), 0),
        ],
        "hints": [
            "Start by assuming a is the biggest, then see if anything beats it.",
            "biggest = a, then if b > biggest: biggest = b, "
            "then the same for c.",
            "Negative numbers must work too, so do not start from 0!",
        ],
    },
    42: {
        "world": 5,
        "title": "RPG Character Card",
        "one_liner": "Build a four-line hero card with bar graphs made of blocks.",
        "module": "q42_character_card",
        "func": "character_card",
        "cases": [
            (("zara", "knight", 3, 2),
             "=== ZARA the Knight ===\nSTR ■■■\nSPD ■■\nPower level: 12"),
            (("bolt", "SPEED DEMON", 1, 9),
             "=== BOLT the Speed Demon ===\nSTR ■\nSPD ■■■■■■■■■\n"
             "Power level: 29"),
            (("rock", "tank", 10, 1),
             "=== ROCK the Tank ===\nSTR ■■■■■■■■■■\nSPD ■\nPower level: 23"),
        ],
        "playable": True,
        "hints": [
            "The name is SHOUTED with .upper() and the role is Title Cased "
            "with .title().",
            "\"■\" * strength draws the bar for you.",
            "Power level is strength * 2 + speed * 3.",
            "Four lines means three \\n characters -- none at the very end.",
        ],
    },
    43: {
        "world": 5,
        "title": "The Global Coin Purse",
        "one_liner": "Change a variable that lives OUTSIDE your function. Needs a magic word.",
        "module": "q43_spend",
        "func": "spend",
        "cases": [],
        "custom": _check_spend,
        "preamble": "coins = 100",
        "examples": [
            "spend(30)   ->  70    (and the global coins is now 70 as well)",
            "spend(70)   ->  0     (and the global coins is now 0 as well)",
        ],
        "hints": [
            "coins is created outside the function, so it is a global variable.",
            "Normally a function can read a global but not change it. "
            "Try it without the magic word and read the error!",
            "Write global coins as the first line inside the function. "
            "Then coins -= amount really does change it.",
            "Finish by returning the new value of coins.",
        ],
    },
}
