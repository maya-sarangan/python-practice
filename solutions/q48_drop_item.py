def drop_item(inventory, item):
    copy = list(inventory)
    if item in copy:
        copy.remove(item)
    return copy
