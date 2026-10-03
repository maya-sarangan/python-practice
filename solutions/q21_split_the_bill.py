def split_the_bill(total, tip_percent, people):
    with_tip = total * (1 + tip_percent / 100)
    return round(with_tip / people, 2)
