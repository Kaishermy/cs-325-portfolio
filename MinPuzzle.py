import heapq


def minEffort(puzzle):
    # Initialize the distances and the priority queue
    rows, cols = len(puzzle), len(puzzle[0])
    dist = {(r, c): float('inf') for r in range(rows) for c in range(cols)}  # Set all node distances to infinity
    dist[(0, 0)] = 0  # Distance to the source is 0
    priority_queue = [(0, 0, 0)]  # Min-priority queue of (height, row, column)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Each of the four directions allowed to move

    while priority_queue:
        # Extract variables from priority_queue
        effort, curr_row, curr_col = heapq.heappop(priority_queue)

        # Stop algorithm if the bottom-right corner has been reached
        if (curr_row, curr_col) == (rows - 1, cols - 1):
            return effort

        # Loop through each direction for the current node to find the best path
        for row_direction, col_direction in directions:
            next_row, next_col = curr_row + row_direction, curr_col + col_direction
            if 0 <= next_row < rows and 0 <= next_col < cols:  # If puzzle[next_row][next_col] is valid
                current_diff = abs(puzzle[curr_row][curr_col] - puzzle[next_row][next_col])
                max_effort = max(effort, current_diff)
                if max_effort < dist[(next_row, next_col)]:
                    dist[(next_row, next_col)] = max_effort
                    heapq.heappush(priority_queue, (max_effort, next_row, next_col))

    return -1
