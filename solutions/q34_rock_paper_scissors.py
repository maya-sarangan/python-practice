def rock_paper_scissors(player_1, player_2):
    one = player_1.lower()
    two = player_2.lower()
    if one == two:
        return "Tie!"
    player_1_wins = (
        (one == "rock" and two == "scissors")
        or (one == "paper" and two == "rock")
        or (one == "scissors" and two == "paper")
    )
    if player_1_wins:
        return "Player 1 wins!"
    return "Player 2 wins!"


def demo():
    print("Rock, paper, scissors! Two players, no peeking.")
    one = input("Player 1 throws: ")
    two = input("Player 2 throws: ")
    print(rock_paper_scissors(one, two))
