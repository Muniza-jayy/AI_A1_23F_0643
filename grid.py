import numpy as np

ROWS = 8
COLS = 10

start = (5, 7)
target = (6, 1)

# Strict clockwise order 
MOVES = [
    (-1, 0),   # Up
    (0, 1),    # Right
    (1, 0),    # Bottom
    (1, 1),    # Bottom-Right (Main Diagonal)
    (0, -1),   # Left
    (-1, -1),  # Top-Left (Main Diagonal)
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
# DEFAULT GRID (your original static wall layout)
# ----------------------------
def create_grid():
    grid = np.zeros((ROWS, COLS), dtype=int)
    for r in range(1, 7):
        grid[r, 5] = -1
    grid[start] = 0
    grid[target] = 0
    return grid


# ----------------------------
# BEST CASE: very narrow corridor (low branching)
# ----------------------------
def create_grid_best():
    grid = -1 * np.ones((ROWS, COLS), dtype=int)  

    
    corridor = [
        start,        # (5,7)
        (4,7),        # Up
        (3,7),        # Up
        (3,6),        # Left
        (2,6),        # Up
        (1,6),        # Up
        (1,5),        # Left
        (1,4),        # Left
        (1,3),        # Left
        (2,3),        # Down
        (3,3),        # Down
        (4,3),        # Down
        (5,3),        # Down
        (6,3),        # Down
        (6,2),        # Left
        (6,1),        # Target
    ]

    for r, c in corridor:
        grid[r, c] = 0

    grid[start] = 0
    grid[target] = 0
    return grid


# ----------------------------
# WORST CASE: mostly open (high branching)
# ----------------------------
def create_grid_worst():
    grid = np.zeros((ROWS, COLS), dtype=int)

    # original wall column
    for r in range(1, 7):
        grid[r, 5] = -1

    # extra walls to force detours but keep lots of open space
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
