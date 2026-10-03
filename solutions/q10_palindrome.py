def is_palindrome(phrase):
    tidy = phrase.lower().replace(" ", "")
    return tidy == tidy[::-1]
