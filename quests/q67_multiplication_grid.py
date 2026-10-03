r"""Quest 67 -- Multiplication Grid   [World 7: The Loop Lair]

A loop inside a loop. The outer one picks the row, the inner one fills
it in. This is how every grid in every game works.

YOUR MISSION
    A loop inside a loop builds a neat square grid of products.

EXAMPLES
    multiplication_grid(1)  ->  '   1'
    multiplication_grid(3)  ->  '   1   2   3\n   2   4   6\n   3   6   9'
    multiplication_grid(4)  ->  '   1   2   3   4\n   2   4   6   8\n   3   6   9  12\n   4   8  12  16'
    multiplication_grid(5)  ->  '   1   2   3   4   5\n   2   4   6   8  10\n   3   6   9  12  15\n   4   8  12  16  20\n   5  10  15  20  25'

    which looks like this:

           1   2   3
           2   4   6
           3   6   9

WHEN YOU ARE READY
    python3 practice.py 67            grade it
    python3 practice.py 67 --hint     ask for a nudge
    python3 practice.py 67 --play     play with it once it works 🎮
"""


def multiplication_grid(n):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    n = int(input("Grid size? "))
    print()
    print(multiplication_grid(n))
