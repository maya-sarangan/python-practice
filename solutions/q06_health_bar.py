def health_bar(hp, max_hp):
    return "❤️" * hp + "🖤" * (max_hp - hp)


def demo():
    hp = 5
    print("Your hero has 5 hearts. Watch the dragon bite!")
    while hp >= 0:
        print("  " + health_bar(hp, 5))
        hp -= 1
