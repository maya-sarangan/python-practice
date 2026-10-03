def pizzas_needed(people, slices_each, slices_per_pizza):
    total_slices = people * slices_each
    return (total_slices + slices_per_pizza - 1) // slices_per_pizza
