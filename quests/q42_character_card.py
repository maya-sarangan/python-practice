r"""Quest 42 -- RPG Character Card   [World 5: The Function Factory]

Every great game has a character sheet. Build the one that prints stat
bars out of solid blocks.

YOUR MISSION
    Build a four-line hero card with bar graphs made of blocks.

EXAMPLES
    character_card('zara', 'knight', 3, 2)       ->  '=== ZARA the Knight ===\nSTR ■■■\nSPD ■■\nPower level: 12'
    character_card('bolt', 'SPEED DEMON', 1, 9)  ->  '=== BOLT the Speed Demon ===\nSTR ■\nSPD ■■■■■■■■■\nPower level: 29'
    character_card('rock', 'tank', 10, 1)        ->  '=== ROCK the Tank ===\nSTR ■■■■■■■■■■\nSPD ■\nPower level: 23'

    which looks like this:

        === ZARA the Knight ===
        STR ■■■
        SPD ■■
        Power level: 12

WHEN YOU ARE READY
    python3 practice.py 42            grade it
    python3 practice.py 42 --hint     ask for a nudge
    python3 practice.py 42 --play     play with it once it works 🎮
"""


def character_card(name, role, strength, speed):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    name = input("Hero name: ")
    role = input("Hero class (knight, wizard, ninja...): ")
    strength = int(input("Strength (1-10): "))
    speed = int(input("Speed (1-10): "))
    print()
    print(character_card(name, role, strength, speed))
