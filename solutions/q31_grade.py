def grade(points):
    if points < 0 or points > 100:
        return "Invalid"
    if points >= 90:
        return "A"
    elif points >= 80:
        return "B"
    elif points >= 70:
        return "C"
    elif points >= 60:
        return "D"
    else:
        return "F"
