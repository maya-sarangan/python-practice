def ticket_price(age, hour):
    if hour < 17:
        return 5
    if age >= 60:
        return 8
    elif age < 13:
        return 7
    else:
        return 12
