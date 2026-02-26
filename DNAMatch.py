def dna_match_bottomup(DNA1, DNA2):
    n = len(DNA1)
    m = len(DNA2)
    cache = [[0 for x in range(n + 1)] for x in range(m + 1)]  # m + 1 rows, n + 1 columns
    cache[0][0] = 0  # empty strings have 0 LCS

    # +1 to be sure all rows/columns are hit
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNA2[i - 1] == DNA1[j - 1]:  # Characters match
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:  # Characters don't match
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    return cache[m][n]


def LCS(DNA1, DNA2, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if memo[m][n] != -1:
        return memo[m][n]
    if DNA1[m - 1] == DNA2[n - 1]:
        memo[m][n] = 1 + LCS(DNA1, DNA2, m - 1, n - 1, memo)
    else:
        memo[m][n] = max(LCS(DNA1, DNA2, m - 1, n, memo), LCS(DNA1, DNA2, m, n - 1, memo))

    return memo[m][n]


def dna_match_topdown(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)
    memo = [[-1 for x in range(n + 1)] for x in range(m + 1)]
    return LCS(DNA1, DNA2, m, n, memo)
