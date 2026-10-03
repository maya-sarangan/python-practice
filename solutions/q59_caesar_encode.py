def caesar_encode(message, shift):
    result = ""
    for character in message:
        if character.isalpha():
            position = ord(character.lower()) - ord("a")
            result += chr((position + shift) % 26 + ord("a"))
        else:
            result += character
    return result


def demo():
    message = input("Message to encode: ")
    shift = int(input("Shift by how much? "))
    print("Secret message:", caesar_encode(message, shift))
