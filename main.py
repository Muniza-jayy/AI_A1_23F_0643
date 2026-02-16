import numpy as np
import matplotlib.pyplot as plt

# Grid size
ROWS = 8
COLS = 10

# Create empty grid
grid = np.zeros((ROWS, COLS), dtype=int)

# Create static walls (example)
for r in range(1, 7):
    grid[r, 5] = -1

# Start and Target

start = (5, 7)
target = (6, 1)

# Make sure start/target not blocked
grid[start] = 0
grid[target] = 0

def draw_grid(grid, start, target):
    plt.figure(figsize=(8, 5))
    plt.title("GOOD PERFORMANCE TIME APP")

    # Base display (walls = 1, free = 0)
    display = np.where(grid == -1, 1, 0)
    plt.imshow(display, interpolation='none')

    ax = plt.gca()

    # Draw grid lines
    ax.set_xticks(np.arange(-0.5, COLS, 1))
    ax.set_yticks(np.arange(-0.5, ROWS, 1))
    ax.grid(True)

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Mark Start (Green)
    ax.add_patch(plt.Rectangle((start[1]-0.5, start[0]-0.5), 1, 1,
                               color='limegreen'))

    # Mark Target (Blue)
    ax.add_patch(plt.Rectangle((target[1]-0.5, target[0]-0.5), 1, 1,
                               color='royalblue'))

    # Add labels
    ax.text(start[1], start[0], "S", ha='center', va='center', color='black')
    ax.text(target[1], target[0], "T", ha='center', va='center', color='black')

    plt.show()

if __name__ == "__main__":
    draw_grid(grid, start, target)
