"""World 4 -- True or False Island. Comparisons, if/elif/else, truthiness."""

QUESTS = {
    29: {
        "world": 4,
        "title": "Leap Year Detector",
        "one_liner": "Three sneaky rules decide whether February gets a 29th day.",
        "module": "q29_leap_year",
        "func": "is_leap_year",
        "cases": [
            ((2024,), True),
            ((2023,), False),
            ((1900,), False),
            ((2000,), True),
            ((2100,), False),
            ((1600,), True),
        ],
        "hints": [
            "A year is a leap year if it divides by 4 with no remainder: "
            "year % 4 == 0.",
            "BUT years that divide by 100 are not leap years... "
            "unless they also divide by 400.",
            "You can write it as one line with and / or, "
            "or as nested if statements. Both are fine!",
        ],
    },
    30: {
        "world": 4,
        "title": "The Bouncer",
        "one_liner": "Decide who gets into the gig based on their age.",
        "module": "q30_bouncer",
        "func": "bouncer",
        "cases": [
            ((18,), "Welcome in! 🎉"),
            ((25,), "Welcome in! 🎉"),
            ((17,), "Bring a grown-up 🧑"),
            ((13,), "Bring a grown-up 🧑"),
            ((12,), "Nope, too young 🚫"),
            ((0,), "Nope, too young 🚫"),
        ],
        "hints": [
            "18 and over gets straight in. 13 to 17 needs a grown-up. "
            "Under 13 is turned away.",
            "Check the biggest age first with if, then elif, then else. "
            "Only one branch ever runs.",
        ],
    },
    31: {
        "world": 4,
        "title": "Report Card Grader",
        "one_liner": "Turn a score out of 100 into a letter grade, and spot bad scores.",
        "module": "q31_grade",
        "func": "grade",
        "cases": [
            ((100,), "A"),
            ((95,), "A"),
            ((90,), "A"),
            ((89,), "B"),
            ((80,), "B"),
            ((79,), "C"),
            ((70,), "C"),
            ((69,), "D"),
            ((60,), "D"),
            ((59,), "F"),
            ((0,), "F"),
            ((101,), "Invalid"),
            ((-1,), "Invalid"),
        ],
        "hints": [
            "90+ is A, 80+ is B, 70+ is C, 60+ is D, below that is F.",
            "Guard first! If the score is below 0 or above 100, "
            "return \"Invalid\" straight away.",
            "Because elif only runs when the ones above failed, "
            "you only need to check one side of each range.",
        ],
    },
    32: {
        "world": 4,
        "title": "Cinema Ticket Till",
        "one_liner": "Price a ticket from the customer's age and the hour of the show.",
        "module": "q32_ticket_price",
        "func": "ticket_price",
        "cases": [
            ((30, 10), 5),
            ((65, 10), 5),
            ((8, 9), 5),
            ((30, 20), 12),
            ((65, 20), 8),
            ((8, 19), 7),
            ((12, 17), 7),
            ((13, 17), 12),
        ],
        "hints": [
            "Any show before 17:00 is the cheap daytime price of 5 for "
            "absolutely everybody.",
            "In the evening: 60 and over pays 8, under 13 pays 7, "
            "everyone else pays 12.",
            "Deal with the time first, then worry about age inside the "
            "evening branch.",
        ],
    },
    33: {
        "world": 4,
        "title": "Password Strength Meter",
        "one_liner": "A strong password is long, has a digit and has a capital letter.",
        "module": "q33_is_strong",
        "func": "is_strong",
        "cases": [
            (("abcdefgH1",), True),
            (("Dragon2024",), True),
            (("short1A",), False),
            (("alllower1",), False),
            (("NoDigitsHere",), False),
            (("",), False),
        ],
        "hints": [
            "Three things must ALL be true, so join them with and.",
            "len(password) >= 8 covers the length.",
            "any(c.isdigit() for c in password) is True if at least one "
            "character is a digit. The same trick works with c.isupper().",
        ],
    },
    34: {
        "world": 4,
        "title": "Rock Paper Scissors Referee",
        "one_liner": "Two throws come in, one verdict goes out.",
        "module": "q34_rock_paper_scissors",
        "func": "rock_paper_scissors",
        "cases": [
            (("rock", "scissors"), "Player 1 wins!"),
            (("paper", "rock"), "Player 1 wins!"),
            (("scissors", "paper"), "Player 1 wins!"),
            (("rock", "paper"), "Player 2 wins!"),
            (("paper", "scissors"), "Player 2 wins!"),
            (("scissors", "rock"), "Player 2 wins!"),
            (("paper", "paper"), "Tie!"),
            (("ROCK", "scissors"), "Player 1 wins!"),
        ],
        "playable": True,
        "hints": [
            "Lowercase both throws first so ROCK and rock behave the same.",
            "Check the tie before anything else -- it is the easiest case.",
            "There are only three ways Player 1 can win. "
            "List them with or, and let else handle Player 2.",
        ],
    },
    35: {
        "world": 4,
        "title": "FizzBuzz, One Number at a Time",
        "one_liner": "The world's most famous interview question, shrunk to one number.",
        "module": "q35_fizz_buzz_word",
        "func": "fizz_buzz_word",
        "cases": [
            ((3,), "Fizz"),
            ((9,), "Fizz"),
            ((5,), "Buzz"),
            ((10,), "Buzz"),
            ((15,), "FizzBuzz"),
            ((0,), "FizzBuzz"),
            ((30,), "FizzBuzz"),
            ((7,), "7"),
            ((1,), "1"),
        ],
        "hints": [
            "n % 3 == 0 means n divides evenly by 3.",
            "Check FizzBuzz FIRST. If you check Fizz first, "
            "15 will never reach the FizzBuzz branch.",
            "For the leftovers, return str(n) -- the answer must be text, "
            "not a number.",
        ],
    },
    36: {
        "world": 4,
        "title": "Is It Empty-ish?",
        "one_liner": "Python quietly thinks some values are already False. Find them.",
        "module": "q36_looks_empty",
        "func": "looks_empty",
        "cases": [
            ((0,), True),
            ((0.0,), True),
            (("",), True),
            (([],), True),
            ((None,), True),
            ((False,), True),
            (("no",), False),
            ((5,), False),
            (([0],), False),
            ((" ",), False),
        ],
        "hints": [
            "Python calls these falsy: 0, 0.0, \"\", [], None and False. "
            "Everything else is truthy.",
            "not value flips truthy into False and falsy into True.",
            "This whole quest fits on one line. Watch out: a list "
            "holding a zero is NOT empty!",
        ],
    },
    37: {
        "world": 4,
        "title": "Divide Without Exploding",
        "one_liner": "Dividing by zero crashes Python. Catch it before it happens.",
        "module": "q37_safe_divide",
        "func": "safe_divide",
        "cases": [
            ((10, 4), 2.5),
            ((1, 3), 0.33),
            ((-9, 2), -4.5),
            ((0, 5), 0.0),
            ((7, 0), "Cannot divide by zero!"),
            ((0, 0), "Cannot divide by zero!"),
        ],
        "hints": [
            "Check b == 0 BEFORE you try the division. "
            "That is called a guard clause.",
            "If b is zero, return the warning text instead of a number.",
            "Otherwise return round(a / b, 2).",
        ],
    },
}
