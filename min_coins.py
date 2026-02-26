# def find_min_coins(denominations, target, subset):
#     denominations.sort(reverse=True)
#
#     if target == 0:
#         return True
#
#     for coin in denominations:
#         if coin <= target:
#             subset.append(coin)
#             result = find_min_coins(denominations, target - coin, subset)
#             if result:
#                 return subset
#             subset.pop()
#
#     return []

def find_min_coins(denominations, target, curr_subset):
    if target == 0:
        return curr_subset

    best_subset = None
    for coin in denominations:
        if coin <= target:
            result = find_min_coins(denominations, target - coin, curr_subset + [coin])
            if result is not None and (best_subset is None or len(result) < len(best_subset)):
                best_subset = result

    return best_subset


print(find_min_coins([1, 5, 2, 8, 10], 20, []))  # [10, 10]
print(find_min_coins([1, 5, 2, 8, 10], 16, []))  # [8, 8]
print(find_min_coins([1, 5, 2, 8, 10], 17, []))  # [10, 5, 2]
