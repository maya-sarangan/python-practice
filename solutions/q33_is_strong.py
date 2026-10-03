def is_strong(password):
    long_enough = len(password) >= 8
    has_digit = any(character.isdigit() for character in password)
    has_capital = any(character.isupper() for character in password)
    return long_enough and has_digit and has_capital
