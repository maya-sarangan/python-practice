"""World 3 -- Number Ninjas. Floor division, modulo, powers, rounding."""

QUESTS = {
    20: {
        "world": 3,
        "title": "Pizza Party Planner",
        "one_liner": "Work out how many whole pizzas to order so nobody goes hungry.",
        "module": "q20_pizzas_needed",
        "func": "pizzas_needed",
        "cases": [
            ((10, 3, 8), 4),
            ((8, 2, 8), 2),
            ((1, 1, 8), 1),
            ((4, 2, 8), 1),
            ((0, 3, 8), 0),
            ((100, 4, 12), 34),
        ],
        "hints": [
            "First find the total number of slices everyone wants.",
            "// divides and throws away the leftovers, so 30 // 8 is 3 -- "
            "but 3 pizzas is not enough for 30 slices!",
            "Trick of the trade: add (slices_per_pizza - 1) to the total "
            "BEFORE you use //. That rounds up.",
        ],
    },
    21: {
        "world": 3,
        "title": "Bill Splitter 3000",
        "one_liner": "Add a tip, split between friends, round to the nearest cent.",
        "module": "q21_split_the_bill",
        "func": "split_the_bill",
        "cases": [
            ((100, 20, 4), 30.0),
            ((47.5, 10, 3), 17.42),
            ((10, 0, 3), 3.33),
            ((60, 15, 2), 34.5),
        ],
        "hints": [
            "A 20% tip means you pay 120% of the bill, which is total * 1.2.",
            "tip_percent / 100 turns 20 into 0.2.",
            "round(number, 2) keeps two digits after the dot.",
        ],
    },
    22: {
        "world": 3,
        "title": "The Change Machine",
        "one_liner": "Break a pile of cents into quarters, dimes, nickels and pennies.",
        "module": "q22_change_machine",
        "func": "change_machine",
        "cases": [
            ((87,), (3, 1, 0, 2)),
            ((41,), (1, 1, 1, 1)),
            ((99,), (3, 2, 0, 4)),
            ((25,), (1, 0, 0, 0)),
            ((4,), (0, 0, 0, 4)),
            ((0,), (0, 0, 0, 0)),
        ],
        "playable": True,
        "hints": [
            "A quarter is 25, a dime is 10, a nickel is 5, a penny is 1.",
            "cents // 25 is how many quarters fit. "
            "cents % 25 is what is left over.",
            "Keep going with the leftover: take out dimes, then nickels, "
            "and whatever remains is pennies.",
            "Return all four numbers in one tuple: "
            "return (quarters, dimes, nickels, pennies)",
        ],
    },
    23: {
        "world": 3,
        "title": "Minutes Into Clock Time",
        "one_liner": "Turn a pile of minutes into hours and minutes, with a leading zero.",
        "module": "q23_time_travel",
        "func": "time_travel",
        "cases": [
            ((125,), "2h 05m"),
            ((60,), "1h 00m"),
            ((7,), "0h 07m"),
            ((0,), "0h 00m"),
            ((1439,), "23h 59m"),
        ],
        "hints": [
            "Hours are total_minutes // 60 and spare minutes are "
            "total_minutes % 60.",
            "f\"{minutes:02d}\" pads a number out to two digits, "
            "so 7 becomes 07.",
        ],
    },
    24: {
        "world": 3,
        "title": "Freezing or Frying?",
        "one_liner": "Convert Celsius to Fahrenheit and judge the weather.",
        "module": "q24_freezing_or_frying",
        "func": "freezing_or_frying",
        "cases": [
            ((0,), "32.0 deg F -> FREEZING 🥶"),
            ((100,), "212.0 deg F -> FRYING 🥵"),
            ((20,), "68.0 deg F -> just fine 😎"),
            ((35,), "95.0 deg F -> FRYING 🥵"),
            ((-40,), "-40.0 deg F -> FREEZING 🥶"),
        ],
        "hints": [
            "Fahrenheit is celsius * 9 / 5 + 32.",
            "Round to one decimal place with round(f, 1) so you get 32.0.",
            "0 or below is FREEZING 🥶, 35 or above is FRYING 🥵, "
            "everything between is just fine 😎.",
        ],
    },
    25: {
        "world": 3,
        "title": "Dog Years Calculator",
        "one_liner": "The first two years count double-ish. After that, four each.",
        "module": "q25_dog_years",
        "func": "dog_years",
        "cases": [
            ((0,), 0.0),
            ((1,), 10.5),
            ((2,), 21.0),
            ((5,), 33.0),
            ((11,), 57.0),
        ],
        "hints": [
            "For the first 2 human years, each one is worth 10.5 dog years.",
            "After year 2 you already have 21 dog years banked. "
            "Every extra human year adds 4 more.",
            "So for 5 years: 21 + (5 - 2) * 4.",
        ],
    },
    26: {
        "world": 3,
        "title": "Bouncy Ball Physics",
        "one_liner": "Each bounce reaches 60% of the height before it.",
        "module": "q26_bounce_height",
        "func": "bounce_height",
        "cases": [
            ((100, 0), 100.0),
            ((100, 1), 60.0),
            ((100, 2), 36.0),
            ((100, 3), 21.6),
            ((50, 2), 18.0),
        ],
        "hints": [
            "** raises a number to a power: 2 ** 3 is 8.",
            "After 3 bounces the ball keeps 0.6 * 0.6 * 0.6 of its height, "
            "which is 0.6 ** 3.",
            "Multiply the start height by that, then round to 2 places.",
        ],
    },
    27: {
        "world": 3,
        "title": "Pack the Chest",
        "one_liner": "Items stack 64 to a slot. How many full stacks, how many loose?",
        "module": "q27_pack_the_chest",
        "func": "pack_the_chest",
        "cases": [
            ((200,), "3 full stacks + 8 extra"),
            ((64,), "1 full stacks + 0 extra"),
            ((5,), "0 full stacks + 5 extra"),
            ((1000,), "15 full stacks + 40 extra"),
            ((0,), "0 full stacks + 0 extra"),
        ],
        "hints": [
            "// gives you how many whole 64s fit.",
            "% gives you what is left over after the full stacks.",
            "Drop both numbers into one f-string.",
        ],
    },
    28: {
        "world": 3,
        "title": "Who Won, and By How Much?",
        "one_liner": "Compare two scores and report the winner and the gap.",
        "module": "q28_score_gap",
        "func": "score_gap",
        "cases": [
            ((10, 3), "Team A by 7"),
            ((3, 10), "Team B by 7"),
            ((0, 12), "Team B by 12"),
            ((5, 5), "Draw"),
            ((21, 20), "Team A by 1"),
        ],
        "hints": [
            "abs(number) throws away the minus sign, so abs(-7) is 7.",
            "Work out the gap once with abs(team_a - team_b), then decide "
            "who to name.",
            "Equal scores get the single word \"Draw\" with no number.",
        ],
    },
}
