"""World 2 -- Word Wizardry. Slicing, string methods, ord() and chr()."""

QUESTS = {
    8: {
        "world": 2,
        "title": "Mirror Mirror",
        "one_liner": "Flip a word back to front.",
        "module": "q08_backwards",
        "func": "backwards",
        "cases": [
            (("python",), "nohtyp"),
            (("stressed",), "desserts"),
            (("wow",), "wow"),
            (("",), ""),
        ],
        "hints": [
            "Slicing takes three parts: word[start:stop:step].",
            "A step of -1 walks through the word backwards. "
            "Leave start and stop empty: word[::-1].",
        ],
    },
    9: {
        "world": 2,
        "title": "Secret Agent Initials",
        "one_liner": "Turn three names into dotted capital initials.",
        "module": "q09_initials",
        "func": "initials",
        "cases": [
            (("ada", "byron", "lovelace"), "A.B.L."),
            (("Grace", "Brewster", "Hopper"), "G.B.H."),
            (("zara", "the", "brave"), "Z.T.B."),
        ],
        "hints": [
            "first[0] gives you the very first letter of first.",
            ".upper() on a single letter makes it a capital.",
            "Do not forget the final dot at the end.",
        ],
    },
    10: {
        "world": 2,
        "title": "Palindrome Patrol",
        "one_liner": "Is the phrase the same forwards and backwards? Ignore capitals and spaces.",
        "module": "q10_palindrome",
        "func": "is_palindrome",
        "cases": [
            (("racecar",), True),
            (("Never Odd Or Even",), True),
            (("Taco cat",), True),
            (("Was it a car or a cat I saw",), True),
            (("python",), False),
            (("almost a palindrome",), False),
            (("",), True),
        ],
        "hints": [
            "First make a tidy copy: lowercase it, then remove the spaces.",
            "phrase.replace(\" \", \"\") deletes every space.",
            "Then just ask: is the tidy copy equal to the tidy copy reversed?",
        ],
    },
    11: {
        "world": 2,
        "title": "The Secret Index",
        "one_liner": "Grab the character sitting at one exact spot in a sentence.",
        "module": "q11_pick_letter",
        "func": "pick_letter",
        "cases": [
            (("dragons are real", 0), "d"),
            (("dragons are real", -1), "l"),
            (("dragons are real", 8), "a"),
            (("hello", 4), "o"),
            (("hello", -5), "h"),
        ],
        "hints": [
            "Counting starts at 0, so sentence[0] is the first character.",
            "Negative numbers count from the end. -1 is the last character.",
        ],
    },
    12: {
        "world": 2,
        "title": "Letter Counter",
        "one_liner": "Count a letter in some text, whatever case either one is in.",
        "module": "q12_count_letter",
        "func": "count_letter",
        "cases": [
            (("Mississippi", "s"), 4),
            (("Mississippi", "I"), 4),
            (("Banana", "A"), 3),
            (("abc", "z"), 0),
            (("", "a"), 0),
        ],
        "hints": [
            "text.count(\"s\") counts how many times \"s\" shows up.",
            "To ignore capitals, lowercase BOTH the text and the letter first.",
        ],
    },
    13: {
        "world": 2,
        "title": "Top Secret Censor",
        "one_liner": "Replace a secret word with exactly that many stars.",
        "module": "q13_censor",
        "func": "censor",
        "cases": [
            (("the password is swordfish", "swordfish"),
             "the password is *********"),
            (("no no no", "no"), "** ** **"),
            (("nothing to hide here", "xyz"), "nothing to hide here"),
            (("spy", "spy"), "***"),
        ],
        "hints": [
            "len(secret) tells you how many stars you need.",
            "\"*\" * 5 builds \"*****\".",
            "sentence.replace(old, new) swaps every copy of old for new.",
        ],
    },
    14: {
        "world": 2,
        "title": "School Email Builder",
        "one_liner": "Make a lowercase school email from a first name, last name and school.",
        "module": "q14_make_email",
        "func": "make_email",
        "cases": [
            (("Ada", "Lovelace", "HogwartsHigh"), "ada.lovelace@hogwartshigh.edu"),
            (("RAJ", "Kumar", "OakPark"), "raj.kumar@oakpark.edu"),
            (("zara", "Khan", "SKYSCHOOL"), "zara.khan@skyschool.edu"),
        ],
        "hints": [
            ".lower() gives you a quiet lowercase copy of a string.",
            "The shape is first.last@school.edu -- the dot and the @ are "
            "just characters you type.",
        ],
    },
    15: {
        "world": 2,
        "title": "Squeeze It Shorter",
        "one_liner": "Trim a long title down to a limit, ending it with a single … character.",
        "module": "q15_shorten",
        "func": "shorten",
        "cases": [
            (("Harry Potter", 20), "Harry Potter"),
            (("Harry Potter and the Goblet", 10), "Harry Pot…"),
            (("abcdef", 6), "abcdef"),
            (("abcdef", 5), "abcd…"),
            (("hi", 1), "…"),
        ],
        "hints": [
            "If the title already fits inside the limit, hand it straight back.",
            "The … counts as one character, so you only have room for "
            "limit - 1 real letters.",
            "title[:4] means 'the first four characters'.",
        ],
    },
    16: {
        "world": 2,
        "title": "Messy Name Cleaner",
        "one_liner": "Strip the junk off the edges and give every word a capital letter.",
        "module": "q16_clean_up",
        "func": "clean_up",
        "cases": [
            (("   zara the brave  ",), "Zara The Brave"),
            (("\n  COOL kid \t",), "Cool Kid"),
            (("already neat",), "Already Neat"),
            (("  python  ",), "Python"),
        ],
        "hints": [
            ".strip() removes spaces, tabs and newlines from both ends.",
            ".title() Capitalises The First Letter Of Every Word.",
            "You can chain them: messy.strip().title().",
        ],
    },
    17: {
        "world": 2,
        "title": "Shout, Whisper or Announce",
        "one_liner": "Let the last character of the text decide how loud it is.",
        "module": "q17_voice",
        "func": "voice",
        "cases": [
            (("help me!",), "HELP ME!"),
            (("Is It Safe?",), "is it safe?"),
            (("just walking",), "Just Walking"),
            (("WOW!",), "WOW!"),
            (("",), ""),
        ],
        "hints": [
            "text.endswith(\"!\") is True when the text finishes with !",
            "Three jobs: ! means .upper(), ? means .lower(), "
            "anything else means .title().",
            "Use if / elif / else so only one of them runs.",
        ],
    },
    18: {
        "world": 2,
        "title": "Letter Shifter",
        "one_liner": "Slide one letter along the alphabet, wrapping z around to a.",
        "module": "q18_shift_letter",
        "func": "shift_letter",
        "cases": [
            (("a", 1), "b"),
            (("z", 1), "a"),
            (("A", 2), "c"),
            (("m", -1), "l"),
            (("a", 26), "a"),
            (("a", -1), "z"),
            (("y", 3), "b"),
        ],
        "hints": [
            "ord(\"a\") is 97 and chr(97) is \"a\". "
            "Letters are secretly numbers!",
            "Take ord(letter) - 97 to get 0 for a, 1 for b, and so on.",
            "Add the shift, then use % 26 so it wraps around, "
            "then add 97 back and chr() it.",
        ],
    },
    19: {
        "world": 2,
        "title": "Pig Latin Translator",
        "one_liner": "Move the first letter to the end and add 'ay' -- unless it is a vowel.",
        "module": "q19_pig_latin",
        "func": "pig_latin",
        "cases": [
            (("python",), "ythonpay"),
            (("smile",), "milesay"),
            (("zoo",), "oozay"),
            (("apple",), "appleway"),
            (("egg",), "eggway"),
            (("igloo",), "iglooway"),
        ],
        "hints": [
            "word[0] is the first letter and word[1:] is everything after it.",
            "word[0] in \"aeiou\" is True when the word starts with a vowel.",
            "Vowel start: word + \"way\". Otherwise: word[1:] + word[0] + \"ay\".",
        ],
    },
}
