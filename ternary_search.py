import math


def ternary_search(input_list, target):
    """Search input_list for target by dividing into three subsets"""
    low = 0
    high = len(input_list) - 1

    while low <= high:
        # Use truncated percentages to find midpoints
        mid_1 = math.floor((low + high) * 0.3)
        mid_2 = math.floor((low + high) * 0.6)

        # If either midpoint is on the target, return its position
        if input_list[mid_1] == target:
            return mid_1 + 1  # Add 1 since indexing starts at position 1
        elif input_list[mid_2] == target:
            return mid_2 + 1  # Add 1 since indexing starts at position 1

        # Estimate target location and adjust search zone
        elif input_list[mid_1] >= target:
            high = mid_1 - 1
        elif input_list[mid_2] >= target > input_list[mid_1]:
            high = mid_2 - 1
        elif input_list[mid_1] < target <= input_list[mid_2]:
            low = mid_1 + 1
        elif input_list[mid_2] < target:
            low = mid_2 + 1

    return None
