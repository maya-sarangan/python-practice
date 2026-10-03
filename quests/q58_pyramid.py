r"""Quest 58 -- Star Pyramid   [World 7: The Loop Lair]

Loops can draw. Build a pyramid of stars with spaces pushing each row
into place.

YOUR MISSION
    Draw a pyramid of stars, point at the top, using spaces to centre
    it.

EXAMPLES
    pyramid(1)  ->  '*'
    pyramid(3)  ->  '  *\n ***\n*****'
    pyramid(4)  ->  '   *\n  ***\n *****\n*******'
    pyramid(0)  ->  ''

    which looks like this:

          *
         ***
        *****

WHEN YOU ARE READY
    python3 practice.py 58            grade it
    python3 practice.py 58 --hint     ask for a nudge
    python3 practice.py 58 --play     play with it once it works 🎮
"""


def pyramid(height):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    height = int(input("How tall? "))
    print()
    print(pyramid(height))
