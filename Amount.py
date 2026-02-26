from copy import deepcopy


def amount_helper(nums, counts, start, result, remainder, combination):
    # Base case
    if remainder == 0:
        result.append(deepcopy(combination))
        return

    # The sum exceeded the target
    elif remainder < 0:
        return

    for i in range(start, len(nums)):
        if counts[i] > 0:  # Exclude duplicate values
            counts[i] -= 1
            combination.append(nums[i])
            amount_helper(nums, counts, i, result, remainder - nums[i], combination,)
            # Backtrack
            combination.pop()
            counts[i] += 1


def amount(nums_list, target_sum):
    result = []
    unique_nums = []
    counts = []

    # Populate list of num counters
    for num in nums_list:
        if num in unique_nums:
            index = unique_nums.index(num)
            counts[index] += 1
        else:
            unique_nums.append(num)
            counts.append(1)

    amount_helper(unique_nums, counts, 0, result, target_sum, [])
    return result


print(amount([11, 1, 3, 2, 6, 1, 5], 8))  # [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]
