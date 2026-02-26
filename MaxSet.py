def max_independent_set(nums):
    n = len(nums)
    if n == 0:  # Empty list
        return []

    cache = [0] * (n + 1)       # Create cache list and initialize all values to 0
    cache[1] = max(0, nums[0])  # Set pos 1 to max val

    # Loop through nums and cache, starting at 2 since cache[0] and cache[1] are solved
    for i in range(2, n + 1):
        include = nums[i - 1] + cache[i - 2]    # If nums[i - 1] is included, skip the prior element
        exclude = cache[i - 1]                  # If nums[i - 1] is excluded, use the previous sum
        cache[i] = max(include, exclude)        # Determine whether to include/exclude based on max

    # Create subsequence
    subsequence = []
    while n >= 1:
        if nums[n - 1] + cache[n - 2] >= cache[n - 1]:  # nums[i - 1] was included
            if nums[n - 1] > 0:  # If it's positive, add it to subsequence
                subsequence.append(nums[n - 1])
            n -= 2  # Skip over next element
        else:  # nums[i - 1] was excluded
            n -= 1  # Go back 1 element instead of skipping it

    # Reverse the list since we worked backwards
    subsequence.reverse()

    return subsequence
