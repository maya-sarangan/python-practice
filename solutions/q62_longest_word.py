def longest_word(words):
    best = ""
    for word in words:
        if len(word) > len(best):
            best = word
    return best
