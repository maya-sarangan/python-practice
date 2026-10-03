def score_gap(team_a, team_b):
    if team_a == team_b:
        return "Draw"
    gap = abs(team_a - team_b)
    if team_a > team_b:
        return f"Team A by {gap}"
    return f"Team B by {gap}"
