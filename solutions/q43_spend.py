coins = 100


def spend(amount):
    global coins
    coins -= amount
    return coins
