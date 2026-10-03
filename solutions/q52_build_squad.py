def build_squad(core, extras, leader):
    squad = list(core)
    squad.insert(0, leader)
    squad.extend(extras)
    return squad
