"""The flavour text. One short story hook per quest, written for a 10-14 year old.

Keep every story to one or two sentences. A story earns its place if it makes
the student want to type the code. If you cannot say it in two sentences,
the quest is probably doing too much.
"""

STORIES = {
    # ---- World 1: The Wizard's Backpack ----------------------------------
    1: "You are the official badge printer at Wizard School, and the sorting "
       "hat insists every name is SHOUTED. Make the badges.",
    2: "A box of unlabelled magic items washes up on the beach. Build the "
       "scanner that tells you what each one actually is.",
    3: "The potion shop's label printer broke and the new one needs code. "
       "Every potion's power must show exactly one digit after the dot.",
    4: "Someone tried to add text to a number and Python exploded. "
       "You are the repair crew. Cast the text into a real number and save the day.",
    5: "Your friend claims they are 'about a million seconds old'. "
       "Build the calculator that proves them spectacularly wrong.",
    6: "Every good game shows your health as hearts, not as a boring number. "
       "Draw the bar.",
    7: "The Story Machine is out of words. Feed it eight and it will produce "
       "something nobody has ever read before.",

    # ---- World 2: Word Wizardry ------------------------------------------
    8: "The Mirror of Backwards reflects every word the wrong way round. "
       "Try it on the word 'stressed' and see what comes out.",
    9: "Spy HQ only issues dotted initials. Three names in, one codename out.",
    10: "A palindrome reads the same in both directions. The Palindrome Patrol "
        "needs a detector that ignores capitals and spaces, so 'Taco cat' counts.",
    11: "An ancient scroll says the treasure is hidden at one exact character. "
        "Count carefully -- and remember that -1 means the last one.",
    12: "How many s's are really in Mississippi? Build the counter and settle "
        "the argument, whatever case anyone types.",
    13: "You are about to post a screenshot that still has the password in it. "
        "Replace it with stars first -- exactly as many stars as letters.",
    14: "First day at a new school, and 400 email addresses need generating. "
        "Nobody is doing that by hand.",
    15: "The game's menu is only so wide. Chop long titles down and finish them "
        "with a single … so players know there is more.",
    16: "Sign-up forms are full of stray spaces and SHOUTING. "
        "Build the cleaner that makes every name look neat.",
    17: "The text-to-speech robot takes its volume from your punctuation. "
        "A ! means shout, a ? means whisper, anything else is a calm announcement.",
    18: "Time to learn the secret that every code in history is built on: "
        "letters are really numbers in disguise.",
    19: "Pig Latin is the world's easiest secret language. "
        "Ythonpay isway unfay otay aysay!",

    # ---- World 3: Number Ninjas -----------------------------------------
    20: "Thirty hungry people, eight slices a pizza. Order four and a quarter "
        "pizzas? The shop will laugh at you. Round UP.",
    21: "The bill arrives, everyone goes quiet, and somebody has to do the "
        "maths. Be the hero with the tip already included.",
    22: "The vending machine must give change using the fewest coins possible. "
        "// and % are about to become your two favourite operators.",
    23: "The game shows times as '125 minutes', which nobody can read. "
        "Turn it into proper clock time -- with the leading zero.",
    24: "Your weather app only speaks Celsius and your cousin only speaks "
        "Fahrenheit. Translate, then judge the weather.",
    25: "Your dog turns 5 today. In dog years, how old is that really? "
        "The first two years count for much more than the rest.",
    26: "Drop a ball and it comes back to 60% of its height, every single time. "
        "Predict exactly how high the fifth bounce goes.",
    27: "Your inventory stacks 64 to a slot. Work out how many full stacks you "
        "have and how many items are rattling around loose.",
    28: "Full time. Report the winner and the margin -- and remember that a "
        "goal difference is never negative.",

    # ---- World 4: True or False Island -----------------------------------
    29: "February 29th only exists in leap years, and the rule has a rule "
        "inside a rule. 1900 was NOT a leap year. 2000 was. Work out why.",
    30: "You are on the door at the biggest gig of the year. "
        "Three answers, no arguments.",
    31: "The grading robot broke on the last day of term. "
        "Rebuild it -- and make sure it refuses impossible scores.",
    32: "The cinema till needs a new brain. Daytime is cheap for everybody. "
        "Evenings depend on who you are.",
    33: "Build the little meter that tells people their password is rubbish. "
        "Long, a digit and a capital -- all three or nothing.",
    34: "Rock, paper, scissors has only nine possible games. "
        "Can you judge all nine without writing nine ifs?",
    35: "This is the question companies really use to interview programmers. "
        "You are going to solve it today.",
    36: "Python secretly thinks some values already mean False. "
        "Learn which ones, and you will understand code nobody else can read.",
    37: "Dividing by zero crashes Python instantly. "
        "A real program must see it coming and refuse politely.",

    # ---- World 5: The Function Factory -----------------------------------
    38: "A greeting that normally says Hello, but lets a caller override it. "
        "Default values make functions feel polite.",
    39: "A 12 inch pizza is not 'a bit bigger' than a 10 inch one. "
        "Prove how much more pizza you actually get.",
    40: "The sale starts in five minutes and every price needs recalculating. "
        "One function, used everywhere.",
    41: "max() is banned. You will have to actually think about this one -- "
        "and negative numbers are waiting to catch you out.",
    42: "Every great game has a character sheet. "
        "Build the one that prints stat bars out of solid blocks.",
    43: "Here is the weirdest rule in Python: a function can READ a variable "
        "from outside, but it cannot CHANGE it -- not without a magic word. "
        "Try it without the word first and read the error.",

    # ---- World 6: Treasure Chests ---------------------------------------
    44: "The chest is full of loot. You only want the first thing and the last "
        "thing, handed back together.",
    45: "Split the loot fairly: you take the back half. "
        "With an odd number of items, the bigger half is yours.",
    46: "Every second step on the bridge is rotten. "
        "Only tread on the safe ones.",
    47: "Two potions, wrong hands. Swap them -- "
        "and Python can do it without a spare bottle.",
    48: "Drop one apple from your bag. Careful: if you are not careful you will "
        "change the original list, and in real programs that causes real bugs.",
    49: "The tournament is over. Put the scores in order, best first, "
        "WITHOUT wrecking the original list.",
    50: "The chest inspector reports how many of a thing you have and which "
        "slot the first one sits in. If it is not there at all, say so -- "
        "because asking for a missing item crashes.",
    51: "The treasure map is a grid: a list of rows, each row a list of squares. "
        "Dig at the given row and column.",
    52: "Assemble the squad: leader at the front, extras on the end. "
        "And leave everybody else's lists exactly as you found them.",
    53: "A profile arrives as a nested list. Unpack it into proper named "
        "variables -- including the list hiding inside it.",
    54: "One captain, and everybody else. The star operator scoops up "
        "the rest for you, however many there are.",

    # ---- World 7: The Loop Lair -----------------------------------------
    55: "T minus ten. Count all the way down to liftoff on a single line.",
    56: "Add up every number from 1 to 100. "
        "A mathematician called Gauss did this in his head aged nine. "
        "You get to use a loop.",
    57: "Print a whole times table on demand. "
        "Ten lines of output from four lines of code.",
    58: "Loops can draw. Build a pyramid of stars with spaces pushing each row "
        "into place.",
    59: "Julius Caesar really used this code to send orders to his generals. "
        "Now you can send secret messages too.",
    60: "You intercepted an enemy message and you know the shift. "
        "Crack it open.",
    61: "Reverse the ORDER of the words without reversing the words themselves. "
        "Yoda would approve.",
    62: "Somewhere in that list of words is the longest one. "
        "Find it -- and if two tie, the earlier one wins.",
    63: "This is the brain of a real guessing game. Get it working, then run it "
        "with --play and the game plays itself around your code.",
    64: "One rotten apple spoils the barrel, so stop looking the instant you "
        "find it. That is what break is for.",
    65: "Walk past every number but only pick up the even ones. "
        "continue means 'nothing to see here, next!'",
    66: "Some words have no vowels at all -- rhythm, crypt, sky. "
        "You need a way to say 'I searched everything and found nothing', "
        "and Python has a strange and lovely tool for exactly that.",
    67: "A loop inside a loop. The outer one picks the row, "
        "the inner one fills it in. This is how every grid in every game works.",
    68: "Pick any number. Halve it if even, triple it and add one if odd. "
        "Repeat. Everyone believes you always reach 1, "
        "but nobody on Earth has ever proved it. Go and poke at it.",

    # ---- World 8: Power-Up Palace ---------------------------------------
    69: "You could track the line numbers yourself with a counter... "
        "or you could use the tool built for exactly this job.",
    70: "Two lists, names and medals, that belong together. "
        "Walk down both at once.",
    71: "Everything you know about loops, squeezed into one line. "
        "This is the move that makes Python code look like Python.",
    72: "TAKE EVERY WORD AND SHOUT IT! One line again.",
    73: "A lambda is a function so small it does not even get a name. "
        "Use one to sieve out the short words.",
    74: "A whole week of temperatures to convert. "
        "map() applies your function to every single one.",
    75: "Add up the team's scores -- but they start with a bonus already "
        "on the board.",
    76: "Sort by length instead of alphabet. "
        "The key setting lets you sort by anything you can imagine.",
    77: "Final quest. Pair the names with the scores, find the champion, "
        "and handle the ties fairly. Everything you have learned, at once.",
}
