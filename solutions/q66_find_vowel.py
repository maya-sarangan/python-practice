def find_vowel(word):
    for character in word:
        if character.lower() in "aeiou":
            return character
    return "no vowels!"
