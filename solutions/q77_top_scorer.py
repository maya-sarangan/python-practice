def top_scorer(names, scores):
    champion = ""
    best = None
    for name, score in zip(names, scores):
        if best is None or score > best:
            champion = name
            best = score
    return champion


def demo():
    names = input("Names, separated by commas: ").split(",")
    scores = input("Scores, separated by commas: ").split(",")
    names = [n.strip() for n in names]
    scores = [int(s) for s in scores]
    print("🏆 Top scorer:", top_scorer(names, scores))
