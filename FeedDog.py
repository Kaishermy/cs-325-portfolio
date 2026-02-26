def feedDog(hunger_level, biscuit_size):
    hunger_level.sort(reverse=True)
    biscuit_size.sort(reverse=True)
    satisfied = 0

    while hunger_level:
        biscuits_to_remove = []
        removed_dog = False  # Avoids double-removals in and after for loop
        for curr_biscuit in range(len(biscuit_size)):
            if biscuit_size[curr_biscuit] >= hunger_level[0]:
                removed_dog = True
                hunger_level.pop(0)
                biscuits_to_remove.append(biscuit_size[curr_biscuit])
                satisfied += 1
                break

        biscuit_size = [x for x in biscuit_size if x not in biscuits_to_remove]
        print(biscuit_size, biscuits_to_remove)
        if not removed_dog:
            hunger_level.pop(0)

    return satisfied
