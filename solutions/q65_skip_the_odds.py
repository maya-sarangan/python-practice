def skip_the_odds(numbers):
    evens = []
    for number in numbers:
        if number % 2 != 0:
            continue
        evens.append(number)
    return evens
