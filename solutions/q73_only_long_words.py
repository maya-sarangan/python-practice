def only_long_words(words, min_length):
    return list(filter(lambda word: len(word) >= min_length, words))
