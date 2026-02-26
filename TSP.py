def solve_tsp(G):
    solution = [0]
    node = 0
    next_node = 0

    for _ in range(len(G) - 1):
        min_edge = float('inf')  # Use instead of max() to handle floats
        for col, col_val in enumerate(G[node]):
            if 0 < col_val < min_edge and col not in solution:
                min_edge = col_val
                next_node = col
        solution.append(next_node)
        node = next_node

    solution.append(0)
    return solution


graph = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]
print(solve_tsp(graph))  # [0, 4, 3, 1, 2, 0]
