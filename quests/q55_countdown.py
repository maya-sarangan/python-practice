"""Quest 55 -- Rocket Countdown   [World 7: The Loop Lair]

T minus ten. Count all the way down to liftoff on a single line.

YOUR MISSION
    Count down to liftoff, all on one line.

EXAMPLES
    countdown(3)  ->  '3... 2... 1... LIFTOFF! 🚀'
    countdown(5)  ->  '5... 4... 3... 2... 1... LIFTOFF! 🚀'
    countdown(1)  ->  '1... LIFTOFF! 🚀'
    countdown(0)  ->  'LIFTOFF! 🚀'

WHEN YOU ARE READY
    python3 practice.py 55            grade it
    python3 practice.py 55 --hint     ask for a nudge
    python3 practice.py 55 --play     play with it once it works 🎮
"""


def countdown(start):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    import time
    start = int(input("Count down from what? "))
    line = countdown(start)
    for chunk in line.split(" "):
        print(chunk, end=" ", flush=True)
        time.sleep(0.4)
    print()
