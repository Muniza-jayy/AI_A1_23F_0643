import numpy as np

ROWS = 8
COLS = 10

start = (5, 7)
target = (6, 1)

MOVES = [
    (-1, 0),   # Up
    (-1, 1),   # Top-Right
    (0, 1),    # Right
    (1, 1),    # Bottom-Right
    (1, 0),    # Bottom
    (1, -1),   # Bottom-Left
    (0, -1),   # Left
    (-1, -1),  # Top-Left
]

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def get_neighbors(node, grid):
    r, c = node
    neighbors = []
    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and grid[nr, nc] != -1:
            neighbors.append((nr, nc))
    return neighbors


# ----------------------------
# BEST CASE: very narrow corridor (low branching)
# ----------------------------
def create_grid_best():
    grid = -1 * np.ones((ROWS, COLS), dtype=int)  # everything wall first

    corridor = [
        (5, 7),  # start
        (6, 6),
        (7, 5),
        (7, 4),
        (6, 3),
        (5, 2),
        (6, 1)   # target
    ]

    for cell in corridor:
        grid[cell] = 0

    # ensure start/target are open
    grid[start] = 0
    grid[target] = 0

    return grid


# ----------------------------
# WORST CASE: mostly open (high branching)
# ----------------------------
def create_grid_worst():
    grid = np.zeros((ROWS, COLS), dtype=int)

    # original wall column (like your earlier setup)
    for r in range(1, 7):
        grid[r, 5] = -1

    # add a few extra walls to make detours but keep lots of open space
    extra_walls = [
        (0, 3), (1, 3), (2, 3),
        (4, 7), (4, 8),
        (6, 2), (7, 2)
    ]
    for cell in extra_walls:
        grid[cell] = -1

    grid[start] = 0
    grid[target] = 0
    return grid
