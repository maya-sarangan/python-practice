def times_table(n):
    lines = []
    for i in range(1, 11):
        lines.append(f"{n} x {i} = {n * i}")
    return "\n".join(lines)
