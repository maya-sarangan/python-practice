def mad_lib(name, animal, place, food, number, verb, adjective, sound):
    return (
        f"One {adjective} morning, {name} found {number} {animal}s in the {place}.\n"
        f"They all shouted '{sound}!' and started to {verb}.\n"
        f"{name} fed them {food} and became their leader forever."
    )


def demo():
    print("Fill in the blanks and I will write you a story.\n")
    name = input("A name: ")
    animal = input("An animal: ")
    place = input("A place: ")
    food = input("A food: ")
    number = input("A number: ")
    verb = input("Something you can do (a verb): ")
    adjective = input("A describing word: ")
    sound = input("A silly sound: ")
    print()
    print(mad_lib(name, animal, place, food, number, verb, adjective, sound))
