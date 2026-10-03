def pyramid(height):
    rows = []
    for i in range(1, height + 1):
        rows.append(" " * (height - i) + "*" * (2 * i - 1))
    return "\n".join(rows)


def demo():
    height = int(input("How tall? "))
    print()
    print(pyramid(height))
