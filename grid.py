import numpy as np

ROWS = 8
COLS = 10

def create_grid():
    grid = np.zeros((ROWS, COLS), dtype=int)
    for r in range(1, 7):
        grid[r, 5] = -1
    return grid

start = (5, 7)
target = (6, 1)

MOVES = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
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
