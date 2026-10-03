def freezing_or_frying(celsius):
    fahrenheit = round(celsius * 9 / 5 + 32, 1)
    if celsius <= 0:
        verdict = "FREEZING 🥶"
    elif celsius >= 35:
        verdict = "FRYING 🥵"
    else:
        verdict = "just fine 😎"
    return f"{fahrenheit} deg F -> {verdict}"
