"""Quest 63 -- Guessing Game Brain   [World 7: The Loop Lair]

This is the brain of a real guessing game. Get it working, then run it
with --play and the game plays itself around your code.

YOUR MISSION
    Compare a guess to the secret and nudge the player.

EXAMPLES
    guess_feedback(3, 7)    ->  'Too low! Aim higher ⬆️'
    guess_feedback(9, 7)    ->  'Too high! Aim lower ⬇️'
    guess_feedback(7, 7)    ->  'Got it! 🎯'
    guess_feedback(0, 100)  ->  'Too low! Aim higher ⬆️'
    guess_feedback(-5, -9)  ->  'Too high! Aim lower ⬇️'

WHEN YOU ARE READY
    python3 practice.py 63            grade it
    python3 practice.py 63 --hint     ask for a nudge
    python3 practice.py 63 --play     play with it once it works 🎮
"""


def guess_feedback(guess, secret):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    import random
    secret = random.randint(1, 100)
    tries = 0
    print("I am thinking of a number between 1 and 100.")
    while True:
        guess = int(input("Your guess: "))
        tries += 1
        message = guess_feedback(guess, secret)
        print("  " + message)
        if guess == secret:
            print(f"You did it in {tries} guesses!")
            break
