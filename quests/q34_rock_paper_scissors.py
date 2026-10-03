"""Quest 34 -- Rock Paper Scissors Referee   [World 4: True or False Island]

Rock, paper, scissors has only nine possible games. Can you judge all
nine without writing nine ifs?

YOUR MISSION
    Two throws come in, one verdict goes out.

EXAMPLES
    rock_paper_scissors('rock', 'scissors')   ->  'Player 1 wins!'
    rock_paper_scissors('paper', 'rock')      ->  'Player 1 wins!'
    rock_paper_scissors('scissors', 'paper')  ->  'Player 1 wins!'
    rock_paper_scissors('rock', 'paper')      ->  'Player 2 wins!'
    rock_paper_scissors('paper', 'scissors')  ->  'Player 2 wins!'

WHEN YOU ARE READY
    python3 practice.py 34            grade it
    python3 practice.py 34 --hint     ask for a nudge
    python3 practice.py 34 --play     play with it once it works 🎮
"""


def rock_paper_scissors(player_1, player_2):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    print("Rock, paper, scissors! Two players, no peeking.")
    one = input("Player 1 throws: ")
    two = input("Player 2 throws: ")
    print(rock_paper_scissors(one, two))
