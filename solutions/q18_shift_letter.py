def shift_letter(letter, shift):
    position = ord(letter.lower()) - ord("a")
    return chr((position + shift) % 26 + ord("a"))
