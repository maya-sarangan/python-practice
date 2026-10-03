def multiplication_grid(n):
    rows = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row += f"{i * j:4d}"
        rows.append(row)
    return "\n".join(rows)


def demo():
    n = int(input("Grid size? "))
    print()
    print(multiplication_grid(n))
