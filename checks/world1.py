"""World 1 -- The Wizard's Backpack. Variables, types, casting, f-strings."""

QUESTS = {
    1: {
        "world": 1,
        "title": "Name Tag Machine",
        "one_liner": "Build a sparkly name tag out of a name and an age.",
        "module": "q01_name_tag",
        "func": "make_name_tag",
        "cases": [
            (("Zara", 11), "⭐ ZARA (11) ⭐"),
            (("raj kumar", 9), "⭐ RAJ KUMAR (9) ⭐"),
            (("Ada", 36), "⭐ ADA (36) ⭐"),
        ],
        "hints": [
            "An f-string lets you drop a variable straight into text: "
            "f\"Hi {name}\".",
            "name.upper() hands you back a SHOUTING copy of the name.",
            "The stars and the brackets are just ordinary characters -- "
            "type them inside the f-string.",
        ],
    },
    2: {
        "world": 1,
        "title": "Type Detective",
        "one_liner": "Look at any value and name what kind of thing it is.",
        "module": "q02_type_detective",
        "func": "friendly_type",
        "cases": [
            ((True,), "yes-or-no"),
            ((False,), "yes-or-no"),
            ((7,), "whole number"),
            ((-100,), "whole number"),
            ((7.0,), "decimal number"),
            ((3.14,), "decimal number"),
            (("7",), "text"),
            (("",), "text"),
            (([7, 8],), "list"),
            (([],), "list"),
            ((None,), "mystery"),
        ],
        "hints": [
            "isinstance(value, int) asks 'is this a whole number?'",
            "Careful! Python thinks True is a kind of int. "
            "So test for bool BEFORE you test for int.",
            "Finish with a plain else that returns \"mystery\".",
        ],
    },
    3: {
        "world": 1,
        "title": "Potion Label Printer",
        "one_liner": "Print a tidy potion label with the power to one decimal place.",
        "module": "q03_potion_label",
        "func": "potion_label",
        "cases": [
            (("dragon fire", 3, 7.0), "Dragon Fire: 3 drops, power 7.0"),
            (("ICE BLAST", 12, 3.456), "Ice Blast: 12 drops, power 3.5"),
            (("slime", 1, 10.0), "Slime: 1 drops, power 10.0"),
            (("midnight moon dew", 40, 0.91), "Midnight Moon Dew: 40 drops, power 0.9"),
        ],
        "hints": [
            "name.title() Makes Every Word Start With A Capital.",
            "Inside an f-string you can say how to show a number: "
            "f\"{power:.1f}\" means one digit after the dot.",
        ],
    },
    4: {
        "world": 1,
        "title": "Repair the Broken Add",
        "one_liner": "Text plus a number explodes. Cast it and make the total work.",
        "module": "q04_total_message",
        "func": "total_message",
        "cases": [
            (("7", 3), "The total is 10"),
            (("100", -1), "The total is 99"),
            (("0", 0), "The total is 0"),
            (("42", 8), "The total is 50"),
        ],
        "hints": [
            "\"7\" is text, not a number. int(\"7\") turns it into 7.",
            "Add first, then drop the answer into an f-string.",
        ],
    },
    5: {
        "world": 1,
        "title": "How Many Seconds Old Are You?",
        "one_liner": "Turn an age in years into a giant number of seconds.",
        "module": "q05_seconds_alive",
        "func": "seconds_alive",
        "cases": [
            ((1,), 31536000),
            ((11,), 346896000),
            ((0,), 0),
            ((100,), 3153600000),
        ],
        "hints": [
            "Work outwards: years -> days -> hours -> minutes -> seconds.",
            "365 days, 24 hours, 60 minutes, 60 seconds. Multiply them all.",
        ],
    },
    6: {
        "world": 1,
        "title": "Emoji Health Bar",
        "one_liner": "Draw a health bar with red hearts for health and black for damage.",
        "module": "q06_health_bar",
        "func": "health_bar",
        "cases": [
            ((3, 5), "❤️❤️❤️🖤🖤"),
            ((0, 3), "🖤🖤🖤"),
            ((4, 4), "❤️❤️❤️❤️"),
            ((1, 10), "❤️🖤🖤🖤🖤🖤🖤🖤🖤🖤"),
        ],
        "playable": True,
        "hints": [
            "In Python \"ab\" * 3 gives you \"ababab\". Strings can be multiplied!",
            "How many black hearts? That is max_hp minus hp.",
            "Glue the two pieces together with +.",
        ],
    },
    7: {
        "world": 1,
        "title": "Mad Lib Story Machine",
        "one_liner": "Eight words in, one ridiculous three-line story out.",
        "module": "q07_mad_lib",
        "func": "mad_lib",
        "cases": [
            (
                ("Zara", "goat", "library", "pizza", 7, "dance", "soggy", "MOO"),
                "One soggy morning, Zara found 7 goats in the library.\n"
                "They all shouted 'MOO!' and started to dance.\n"
                "Zara fed them pizza and became their leader forever.",
            ),
            (
                ("Mr Bean", "robot", "swimming pool", "jam", 1, "sing",
                 "sparkly", "beep"),
                "One sparkly morning, Mr Bean found 1 robots in the swimming pool.\n"
                "They all shouted 'beep!' and started to sing.\n"
                "Mr Bean fed them jam and became their leader forever.",
            ),
        ],
        "playable": True,
        "hints": [
            "The story is three lines. End the first two lines with \\n.",
            "You can glue f-strings together by putting them next to each other "
            "inside brackets, one per line.",
            "The sound needs single quotes around it inside the text.",
        ],
    },
}
