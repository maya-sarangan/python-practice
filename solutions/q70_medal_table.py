def medal_table(names, medals):
    lines = []
    for name, medal in zip(names, medals):
        lines.append(f"{name}: {medal}")
    return "\n".join(lines)
