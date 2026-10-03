def voice(text):
    if text.endswith("!"):
        return text.upper()
    elif text.endswith("?"):
        return text.lower()
    else:
        return text.title()
