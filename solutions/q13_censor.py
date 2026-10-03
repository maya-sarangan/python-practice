def censor(sentence, secret):
    return sentence.replace(secret, "*" * len(secret))
