def friendly_type(value):
    if isinstance(value, bool):
        return "yes-or-no"
    if isinstance(value, int):
        return "whole number"
    if isinstance(value, float):
        return "decimal number"
    if isinstance(value, str):
        return "text"
    if isinstance(value, list):
        return "list"
    return "mystery"
