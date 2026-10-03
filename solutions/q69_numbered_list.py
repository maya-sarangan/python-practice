def numbered_list(items):
    lines = []
    for number, item in enumerate(items, start=1):
        lines.append(f"{number}. {item}")
    return "\n".join(lines)
