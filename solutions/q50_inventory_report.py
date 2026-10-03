def inventory_report(inventory, item):
    if item not in inventory:
        return f"No {item} in the chest."
    how_many = inventory.count(item)
    first_slot = inventory.index(item)
    return f"{how_many} x {item}, first one at slot {first_slot}"
