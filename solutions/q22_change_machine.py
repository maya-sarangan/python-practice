def change_machine(cents):
    quarters = cents // 25
    left = cents % 25
    dimes = left // 10
    left = left % 10
    nickels = left // 5
    pennies = left % 5
    return (quarters, dimes, nickels, pennies)


def demo():
    cents = int(input("How many cents? "))
    quarters, dimes, nickels, pennies = change_machine(cents)
    print(f"  {quarters} quarter(s)")
    print(f"  {dimes} dime(s)")
    print(f"  {nickels} nickel(s)")
    print(f"  {pennies} penny/pennies")
