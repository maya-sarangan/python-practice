def guess_feedback(guess, secret):
    if guess == secret:
        return "Got it! 🎯"
    elif guess < secret:
        return "Too low! Aim higher ⬆️"
    else:
        return "Too high! Aim lower ⬇️"


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
