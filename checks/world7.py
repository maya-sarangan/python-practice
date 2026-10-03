"""World 7 -- The Loop Lair. for, while, range, break, continue, for/else."""


def _times_table(n):
    return "\n".join(
        str(n) + " x " + str(i) + " = " + str(n * i) for i in range(1, 11)
    )


def _grid(n):
    rows = []
    for i in range(1, n + 1):
        rows.append("".join("{:4d}".format(i * j) for j in range(1, n + 1)))
    return "\n".join(rows)


QUESTS = {
    55: {
        "world": 7,
        "title": "Rocket Countdown",
        "one_liner": "Count down to liftoff, all on one line.",
        "module": "q55_countdown",
        "func": "countdown",
        "cases": [
            ((3,), "3... 2... 1... LIFTOFF! 🚀"),
            ((5,), "5... 4... 3... 2... 1... LIFTOFF! 🚀"),
            ((1,), "1... LIFTOFF! 🚀"),
            ((0,), "LIFTOFF! 🚀"),
        ],
        "playable": True,
        "hints": [
            "range(start, 0, -1) counts downwards and stops before 0.",
            "Build the answer up in a variable: "
            "text = text + str(n) + \"... \" each time round.",
            "Then stick \"LIFTOFF! 🚀\" on the end -- "
            "notice each number is followed by a space.",
        ],
    },
    56: {
        "world": 7,
        "title": "Add Them All Up",
        "one_liner": "Add every whole number from 1 up to n, using a loop.",
        "module": "q56_sum_to",
        "func": "sum_to",
        "cases": [
            ((5,), 15),
            ((1,), 1),
            ((10,), 55),
            ((100,), 5050),
            ((0,), 0),
        ],
        "hints": [
            "Start a total at 0 BEFORE the loop begins.",
            "range(1, n + 1) gives you 1 up to and including n.",
            "total += number is short for total = total + number.",
        ],
    },
    57: {
        "world": 7,
        "title": "Times Table Printer",
        "one_liner": "Produce the full 1 to 10 times table for any number.",
        "module": "q57_times_table",
        "func": "times_table",
        "cases": [
            ((3,), "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n"
                   "3 x 6 = 18\n3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n"
                   "3 x 10 = 30"),
            ((1,), _times_table(1)),
            ((12,), _times_table(12)),
        ],
        "hints": [
            "Collect each line into a list, then \"\\n\".join(lines) at the end.",
            "Or build one big string and add \"\\n\" between lines -- "
            "just make sure there is no stray newline at the very end.",
            "The line for i is f\"{n} x {i} = {n * i}\".",
        ],
    },
    58: {
        "world": 7,
        "title": "Star Pyramid",
        "one_liner": "Draw a pyramid of stars, point at the top, using spaces to centre it.",
        "module": "q58_pyramid",
        "func": "pyramid",
        "cases": [
            ((1,), "*"),
            ((3,), "  *\n ***\n*****"),
            ((4,), "   *\n  ***\n *****\n*******"),
            ((0,), ""),
        ],
        "playable": True,
        "hints": [
            "Row 1 has 1 star, row 2 has 3, row 3 has 5. "
            "So row i has 2 * i - 1 stars.",
            "Row i needs height - i spaces in front of it.",
            "Build each row as \" \" * spaces + \"*\" * stars, "
            "then join the rows with \"\\n\".",
        ],
    },
    59: {
        "world": 7,
        "title": "Caesar Cipher Encoder",
        "one_liner": "Shift every letter of a whole message. Leave spaces and punctuation alone.",
        "module": "q59_caesar_encode",
        "func": "caesar_encode",
        "cases": [
            (("attack at dawn", 3), "dwwdfn dw gdzq"),
            (("zoo", 1), "app"),
            (("hello world", 13), "uryyb jbeyq"),
            (("dragons!", 1), "esbhpot!"),
            (("abc", 0), "abc"),
        ],
        "playable": True,
        "hints": [
            "You already solved one letter back in quest 18. "
            "Now do it in a loop, one character at a time.",
            "Only shift real letters. "
            "character.isalpha() tells you if it is a letter.",
            "Anything that is not a letter gets added to the answer unchanged.",
        ],
    },
    60: {
        "world": 7,
        "title": "Caesar Cipher Breaker",
        "one_liner": "Undo the shift and read the secret message.",
        "module": "q60_caesar_decode",
        "func": "caesar_decode",
        "cases": [
            (("dwwdfn dw gdzq", 3), "attack at dawn"),
            (("uryyb jbeyq", 13), "hello world"),
            (("app", 1), "zoo"),
            (("esbhpot!", 1), "dragons!"),
        ],
        "hints": [
            "Decoding is just encoding in the other direction.",
            "A shift of -3 undoes a shift of 3.",
            "So copy your quest 59 answer and change the + to a -. "
            "Reusing your own work is what real programmers do.",
        ],
    },
    61: {
        "world": 7,
        "title": "Backwards Sentence",
        "one_liner": "Keep every word spelled correctly, but put them in reverse order.",
        "module": "q61_reverse_words",
        "func": "reverse_words",
        "cases": [
            (("I love python",), "python love I"),
            (("a b c d",), "d c b a"),
            (("solo",), "solo"),
            (("",), ""),
        ],
        "hints": [
            "sentence.split() chops the sentence into a list of words.",
            "You can reverse a list with a slice: words[::-1].",
            "\" \".join(words) glues them back together with spaces.",
        ],
    },
    62: {
        "world": 7,
        "title": "Longest Word Hunter",
        "one_liner": "Find the longest word. If two tie, the earlier one wins.",
        "module": "q62_longest_word",
        "func": "longest_word",
        "cases": [
            ((["hi", "hello", "hey"],), "hello"),
            ((["a", "bb", "ccc", "dd"],), "ccc"),
            ((["aa", "bb"],), "aa"),
            ((["only"],), "only"),
            (([],), ""),
        ],
        "hints": [
            "Start with best = \"\" so an empty list already works.",
            "Loop through the words and keep the current champion in a "
            "variable.",
            "Use > and not >= so a tie does not knock out the earlier word.",
        ],
    },
    63: {
        "world": 7,
        "title": "Guessing Game Brain",
        "one_liner": "Compare a guess to the secret and nudge the player.",
        "module": "q63_guess_feedback",
        "func": "guess_feedback",
        "cases": [
            ((3, 7), "Too low! Aim higher ⬆️"),
            ((9, 7), "Too high! Aim lower ⬇️"),
            ((7, 7), "Got it! 🎯"),
            ((0, 100), "Too low! Aim higher ⬆️"),
            ((-5, -9), "Too high! Aim lower ⬇️"),
        ],
        "playable": True,
        "hints": [
            "Three outcomes, so if / elif / else.",
            "Check the equal case first -- it is the simplest.",
            "Once this works, run it with --play to play the real game. "
            "The while loop is already written for you!",
        ],
    },
    64: {
        "world": 7,
        "title": "First Bad Apple",
        "one_liner": "Stop at the first rotten apple and report its slot. Or -1 if the barrel is fine.",
        "module": "q64_first_bad_apple",
        "func": "first_bad_apple",
        "cases": [
            ((["good", "good", "rotten", "good"],), 2),
            ((["rotten"],), 0),
            ((["good", "good"],), -1),
            (([],), -1),
            ((["good", "rotten", "rotten"],), 1),
        ],
        "hints": [
            "You need the position, not just the apple, so loop over "
            "range(len(apples)).",
            "The moment you find a rotten one, return its index. "
            "return leaves the loop immediately.",
            "If the loop finishes without returning, return -1 at the end.",
        ],
    },
    65: {
        "world": 7,
        "title": "Skip the Odd Ones",
        "one_liner": "Collect only the even numbers, using continue to skip the rest.",
        "module": "q65_skip_the_odds",
        "func": "skip_the_odds",
        "cases": [
            (([1, 2, 3, 4],), [2, 4]),
            (([0, -2, 7],), [0, -2]),
            (([1, 3, 5],), []),
            (([],), []),
        ],
        "hints": [
            "Make an empty list before the loop, then .append() the keepers.",
            "continue jumps straight to the next trip round the loop.",
            "An odd number has number % 2 == 1... but careful with "
            "negatives! number % 2 != 0 is safer.",
        ],
    },
    66: {
        "world": 7,
        "title": "Vowel Hunt (with for/else)",
        "one_liner": "Return the first vowel in a word, or say there are none.",
        "module": "q66_find_vowel",
        "func": "find_vowel",
        "cases": [
            (("apple",), "a"),
            (("python",), "o"),
            (("Igloo",), "I"),
            (("rhythm",), "no vowels!"),
            (("sky",), "no vowels!"),
            (("crypt",), "no vowels!"),
            (("",), "no vowels!"),
        ],
        "hints": [
            "Loop over the characters and check "
            "character.lower() in \"aeiou\".",
            "Return the character exactly as you found it, "
            "capital letter and all.",
            "A for loop can have an else! It runs only if the loop never hit "
            "a break. That is a neat way to say \"I searched everything "
            "and found nothing\".",
        ],
    },
    67: {
        "world": 7,
        "title": "Multiplication Grid",
        "one_liner": "A loop inside a loop builds a neat square grid of products.",
        "module": "q67_multiplication_grid",
        "func": "multiplication_grid",
        "cases": [
            ((1,), "   1"),
            ((3,), "   1   2   3\n   2   4   6\n   3   6   9"),
            ((4,), _grid(4)),
            ((5,), _grid(5)),
        ],
        "playable": True,
        "hints": [
            "The outer loop picks the row, the inner loop picks the column.",
            "Every number is padded to 4 characters wide: f\"{value:4d}\".",
            "Build each row with the inner loop, add it to a list of rows, "
            "then join the rows with \"\\n\".",
        ],
    },
    68: {
        "world": 7,
        "title": "The Collatz Mystery",
        "one_liner": "Halve it if even, triple-plus-one if odd. Count the steps back to 1.",
        "module": "q68_collatz_steps",
        "func": "collatz_steps",
        "cases": [
            ((1,), 0),
            ((2,), 1),
            ((6,), 8),
            ((7,), 16),
            ((27,), 111),
        ],
        "playable": True,
        "hints": [
            "You do not know how many steps it takes, so this is a job for "
            "while, not for.",
            "Keep going while n != 1. Count every change you make.",
            "Even means n % 2 == 0, and then n = n // 2. "
            "Odd means n = 3 * n + 1.",
            "Nobody on Earth has proved this always reaches 1. "
            "You are poking at a real unsolved maths problem!",
        ],
    },
}
