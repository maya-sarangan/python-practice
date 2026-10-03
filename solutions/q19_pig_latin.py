def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    return word[1:] + word[0] + "ay"
