"""Quest 06 -- Emoji Health Bar   [World 1: The Wizard's Backpack]

Every good game shows your health as hearts, not as a boring number.
Draw the bar.

YOUR MISSION
    Draw a health bar with red hearts for health and black for damage.

EXAMPLES
    health_bar(3, 5)   ->  '❤️❤️❤️🖤🖤'
    health_bar(0, 3)   ->  '🖤🖤🖤'
    health_bar(4, 4)   ->  '❤️❤️❤️❤️'
    health_bar(1, 10)  ->  '❤️🖤🖤🖤🖤🖤🖤🖤🖤🖤'

WHEN YOU ARE READY
    python3 practice.py 6            grade it
    python3 practice.py 6 --hint     ask for a nudge
    python3 practice.py 6 --play     play with it once it works 🎮
"""


def health_bar(hp, max_hp):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    hp = 5
    print("Your hero has 5 hearts. Watch the dragon bite!")
    while hp >= 0:
        print("  " + health_bar(hp, 5))
        hp -= 1
