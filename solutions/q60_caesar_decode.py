def caesar_decode(message, shift):
    result = ""
    for character in message:
        if character.isalpha():
            position = ord(character.lower()) - ord("a")
            result += chr((position - shift) % 26 + ord("a"))
        else:
            result += character
    return result
