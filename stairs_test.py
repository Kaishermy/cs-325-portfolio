class Solution:

    @staticmethod
    def climb_stairs(n: int) -> int:
        # could be an Error as well checks if n is less than 0 in case
        if n < 0:
            return None
        # base cases
        if n == 0 or n == 1:
            return 1
        # used to store previous 2 calculations
        prev1, prev2 = 1, 1
        # iterative approach for dp
        for i in range(2, n + 1):
            # temp = prev1
            # prev1 = prev1 + prev2
            # prev2 = temp
            prev1, prev2 = prev1 + prev2, prev1
        # return solution
        return prev1


solution = Solution
print(solution.climb_stairs(5))
print(solution.climb_stairs(0))
