"""Quest 22 -- The Change Machine   [World 3: Number Ninjas]

The vending machine must give change using the fewest coins possible. //
and % are about to become your two favourite operators.

YOUR MISSION
    Break a pile of cents into quarters, dimes, nickels and pennies.

EXAMPLES
    change_machine(87)  ->  (3, 1, 0, 2)
    change_machine(41)  ->  (1, 1, 1, 1)
    change_machine(99)  ->  (3, 2, 0, 4)
    change_machine(25)  ->  (1, 0, 0, 0)
    change_machine(4)   ->  (0, 0, 0, 4)

WHEN YOU ARE READY
    python3 practice.py 22            grade it
    python3 practice.py 22 --hint     ask for a nudge
    python3 practice.py 22 --play     play with it once it works 🎮
"""


def change_machine(cents):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
def demo():
    cents = int(input("How many cents? "))
    quarters, dimes, nickels, pennies = change_machine(cents)
    print(f"  {quarters} quarter(s)")
    print(f"  {dimes} dime(s)")
    print(f"  {nickels} nickel(s)")
    print(f"  {pennies} penny/pennies")
