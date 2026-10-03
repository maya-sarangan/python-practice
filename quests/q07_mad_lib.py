r"""Quest 07 -- Mad Lib Story Machine   [World 1: The Wizard's Backpack]

The Story Machine is out of words. Feed it eight and it will produce
something nobody has ever read before.

YOUR MISSION
    Eight words in, one ridiculous three-line story out.

EXAMPLES
    mad_lib('Zara', 'goat', 'library', 'pizza', 7, 'dance', 'soggy', 'MOO')            ->  "One soggy morning, Zara found 7 goats in the library.\nThey all shouted 'MOO!' and started to dance.\nZara fed them pizza and became their leader forever."
    mad_lib('Mr Bean', 'robot', 'swimming pool', 'jam', 1, 'sing', 'sparkly', 'beep')  ->  "One sparkly morning, Mr Bean found 1 robots in the swimming pool.\nThey all shouted 'beep!' and started to sing.\nMr Bean fed them jam and became their leader forever."

    which looks like this:

        One soggy morning, Zara found 7 goats in the library.
        They all shouted 'MOO!' and started to dance.
        Zara fed them pizza and became their leader forever.

WHEN YOU ARE READY
    python3 practice.py 7            grade it
    python3 practice.py 7 --hint     ask for a nudge
    python3 practice.py 7 --play     play with it once it works 🎮
"""


def mad_lib(name, animal, place, food, number, verb, adjective, sound):
    # 👇 Delete the line below, then write your answer here.
    raise NotImplementedError


# This part is a gift -- it is already written for you.
# Finish the function above, then run it with --play.
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
