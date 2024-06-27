from collections import deque

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Find the start (S) and end (E) positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    # If start or end not found, return an empty path
    if not start or not end:
        return []

    # BFS initialization
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        (current_pos, path) = queue.popleft()
        if current_pos == end:
            return path

        for direction in directions:
            new_r, new_c = current_pos[0] + direction[0], current_pos[1] + direction[1]
            new_pos = (new_r, new_c)

            if 0 <= new_r < rows and 0 <= new_c < cols and new_pos not in visited:
                if maze[new_r][new_c] == '.' or maze[new_r][new_c] == 'E':
                    queue.append((new_pos, path + [new_pos]))
                    visited.add(new_pos)

    # No path found
    return []

# Example usage
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '#', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '.', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '#', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

path = solve_maze(maze)
print(path)
