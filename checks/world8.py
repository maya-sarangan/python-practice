"""World 8 -- Power-Up Palace. enumerate, zip, comprehensions, map/filter/sum."""

QUESTS = {
    69: {
        "world": 8,
        "title": "Numbered List Maker",
        "one_liner": "Number a list of items starting at 1, one per line.",
        "module": "q69_numbered_list",
        "func": "numbered_list",
        "cases": [
            ((["apple", "banana"],), "1. apple\n2. banana"),
            ((["solo"],), "1. solo"),
            ((["a", "b", "c"],), "1. a\n2. b\n3. c"),
            (([],), ""),
        ],
        "hints": [
            "enumerate(items) hands you the position AND the item together.",
            "It normally counts from 0, but enumerate(items, start=1) "
            "counts from 1 instead -- no +1 needed anywhere.",
            "Collect the lines, then join them with \"\\n\".",
        ],
    },
    70: {
        "world": 8,
        "title": "Medal Table",
        "one_liner": "Walk two lists side by side and pair them up.",
        "module": "q70_medal_table",
        "func": "medal_table",
        "cases": [
            ((["Ana", "Bo"], ["gold", "silver"]), "Ana: gold\nBo: silver"),
            ((["Ana", "Bo", "Cy"], ["gold"]), "Ana: gold"),
            ((["X"], ["bronze"]), "X: bronze"),
            (([], []), ""),
        ],
        "hints": [
            "zip(names, medals) marches through both lists at the same time.",
            "for name, medal in zip(names, medals): gives you both at once.",
            "zip stops as soon as the shorter list runs out -- which is "
            "exactly what the third test wants.",
        ],
    },
    71: {
        "world": 8,
        "title": "Square Factory (One Line)",
        "one_liner": "Build a list of square numbers using a list comprehension.",
        "module": "q71_squares_up_to",
        "func": "squares_up_to",
        "cases": [
            ((5,), [1, 4, 9, 16, 25]),
            ((1,), [1]),
            ((3,), [1, 4, 9]),
            ((0,), []),
        ],
        "hints": [
            "A list comprehension looks like "
            "[something for item in sequence].",
            "You want [i * i for i in range(1, n + 1)].",
            "No empty list, no .append(), no loop body. One line.",
        ],
    },
    72: {
        "world": 8,
        "title": "Shout Every Word",
        "one_liner": "Uppercase every word and give it an exclamation mark. One line.",
        "module": "q72_shout_all",
        "func": "shout_all",
        "cases": [
            ((["hi", "go"],), ["HI!", "GO!"]),
            ((["Wow"],), ["WOW!"]),
            ((["a", "b", "c"],), ["A!", "B!", "C!"]),
            (([],), []),
        ],
        "hints": [
            "Inside a comprehension you can call methods: "
            "[w.upper() for w in words].",
            "Then glue \"!\" on the end of each one.",
        ],
    },
    73: {
        "world": 8,
        "title": "Filter the Long Words",
        "one_liner": "Keep only the words that are long enough, using filter() and a lambda.",
        "module": "q73_only_long_words",
        "func": "only_long_words",
        "cases": [
            ((["tree", "sky", "mountain"], 4), ["tree", "mountain"]),
            ((["a", "bb", "ccc"], 3), ["ccc"]),
            ((["hi", "yo"], 1), ["hi", "yo"]),
            (([], 2), []),
        ],
        "hints": [
            "A lambda is a tiny nameless function: lambda w: len(w) >= 2",
            "filter(test, words) keeps only the items where test is True.",
            "filter gives back a lazy filter object, so wrap it in list().",
        ],
    },
    74: {
        "world": 8,
        "title": "Convert the Whole Forecast",
        "one_liner": "Turn a whole list of Celsius readings into Fahrenheit with map().",
        "module": "q74_to_fahrenheit_all",
        "func": "to_fahrenheit_all",
        "cases": [
            (([0, 100],), [32.0, 212.0]),
            (([20, 35],), [68.0, 95.0]),
            (([-40],), [-40.0]),
            (([],), []),
        ],
        "hints": [
            "map(function, items) runs the function on every single item.",
            "The lambda does the maths: lambda c: c * 9 / 5 + 32",
            "Wrap the result in list() so you get a real list back.",
        ],
    },
    75: {
        "world": 8,
        "title": "Team Score With a Head Start",
        "one_liner": "Add up the scores, but begin from a bonus instead of zero.",
        "module": "q75_team_score",
        "func": "team_score",
        "cases": [
            (([1, 2, 3], 10), 16),
            (([10], 0), 10),
            (([], 5), 5),
            (([-2, 2], 100), 100),
        ],
        "hints": [
            "sum(scores) adds a whole list in one go. No loop needed.",
            "sum() takes a second setting: sum(scores, start=bonus).",
        ],
    },
    76: {
        "world": 8,
        "title": "Shortest First",
        "one_liner": "Sort words by how long they are, not alphabetically.",
        "module": "q76_sort_by_length",
        "func": "sort_by_length",
        "cases": [
            ((["banana", "kiwi", "fig"],), ["fig", "kiwi", "banana"]),
            ((["aa", "b", "ccc"],), ["b", "aa", "ccc"]),
            ((["dog", "cat"],), ["dog", "cat"]),
            (([],), []),
        ],
        "hints": [
            "sorted() takes a key setting that says WHAT to sort by.",
            "key=len tells it to compare the lengths instead of the words.",
            "Words of equal length keep the order they came in -- "
            "that is why dog still comes before cat.",
        ],
    },
    77: {
        "world": 8,
        "title": "Who Is Top of the Class?",
        "one_liner": "Match names to scores and name the highest scorer. Ties go to the first.",
        "module": "q77_top_scorer",
        "func": "top_scorer",
        "cases": [
            ((["Ana", "Bo", "Cy"], [3, 9, 5]), "Bo"),
            ((["Ana", "Bo"], [5, 5]), "Ana"),
            ((["Solo"], [0]), "Solo"),
            ((["Ana", "Bo", "Cy"], [-1, -9, -5]), "Ana"),
            (([], []), ""),
        ],
        "playable": True,
        "hints": [
            "zip(names, scores) pairs each name with its score.",
            "Keep a champion name and a best score as you loop. "
            "Start the best score at None so negative scores still work.",
            "Only swap champions when the new score is strictly greater, "
            "so ties go to whoever came first.",
        ],
    },
}
