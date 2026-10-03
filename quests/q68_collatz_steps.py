"""Quest 68 -- The Collatz Mystery   [World 7: The Loop Lair]

Pick any number. Halve it if even, triple it and add one if odd. Repeat.
Everyone believes you always reach 1, but nobody on Earth has ever
proved it. Go and poke at it.

YOUR MISSION
    Halve it if even, triple-plus-one if odd. Count the steps back to 1.

EXAMPLES
    collatz_steps(1)   ->  0
    collatz_steps(2)   ->  1
    collatz_steps(6)   ->  8
    collatz_steps(7)   ->  16
    collatz_steps(27)  ->  111

WHEN YOU ARE READY
    python3 practice.py 68            grade it
    python3 practice.py 68 --hint     ask for a nudge
    python3 practice.py 68 --play     play with it once it works 🎮
"""


def collatz_steps(n):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    n = int(input("Pick a starting number: "))
    print(f"{n} takes {collatz_steps(n)} steps to reach 1.")
