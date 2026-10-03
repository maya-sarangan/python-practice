"""Quest 77 -- Who Is Top of the Class?   [World 8: Power-Up Palace]

Final quest. Pair the names with the scores, find the champion, and
handle the ties fairly. Everything you have learned, at once.

YOUR MISSION
    Match names to scores and name the highest scorer. Ties go to the
    first.

EXAMPLES
    top_scorer(['Ana', 'Bo', 'Cy'], [3, 9, 5])     ->  'Bo'
    top_scorer(['Ana', 'Bo'], [5, 5])              ->  'Ana'
    top_scorer(['Solo'], [0])                      ->  'Solo'
    top_scorer(['Ana', 'Bo', 'Cy'], [-1, -9, -5])  ->  'Ana'
    top_scorer([], [])                             ->  ''

WHEN YOU ARE READY
    python3 practice.py 77            grade it
    python3 practice.py 77 --hint     ask for a nudge
    python3 practice.py 77 --play     play with it once it works 🎮
"""


def top_scorer(names, scores):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    names = input("Names, separated by commas: ").split(",")
    scores = input("Scores, separated by commas: ").split(",")
    names = [n.strip() for n in names]
    scores = [int(s) for s in scores]
    print("🏆 Top scorer:", top_scorer(names, scores))
