def character_card(name, role, strength, speed):
    power = strength * 2 + speed * 3
    return (
        f"=== {name.upper()} the {role.title()} ===\n"
        f"STR {'■' * strength}\n"
        f"SPD {'■' * speed}\n"
        f"Power level: {power}"
    )


def demo():
    name = input("Hero name: ")
    role = input("Hero class (knight, wizard, ninja...): ")
    strength = int(input("Strength (1-10): "))
    speed = int(input("Speed (1-10): "))
    print()
    print(character_card(name, role, strength, speed))
