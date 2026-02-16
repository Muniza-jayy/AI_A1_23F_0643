import matplotlib.pyplot as plt
import numpy as np
from grid import ROWS, COLS, start, target

def draw_grid(grid, frontier=set(), explored=set(), path=set(), algo=""):
    plt.clf()
    plt.title("The Visualization of Algorithms")

    display = np.where(grid == -1, 1, 0)
    plt.imshow(display, interpolation="none")

    ax = plt.gca()
    ax.set_xticks(np.arange(-0.5, COLS, 1))
    ax.set_yticks(np.arange(-0.5, ROWS, 1))
    ax.grid(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    def fill(cell, color):
        r, c = cell
        rect = plt.Rectangle((c-0.5, r-0.5), 1, 1,
                             facecolor=color, edgecolor="none", alpha=0.85)
        ax.add_patch(rect)

    for cell in explored:
        if cell != start and cell != target:
            fill(cell, "lightgray")

    for cell in frontier:
        if cell != start and cell != target:
            fill(cell, "khaki")

    for cell in path:
        if cell != start and cell != target:
            fill(cell, "deepskyblue")

    fill(start, "limegreen")
    fill(target, "royalblue")

    ax.text(start[1], start[0], "S", ha="center", va="center")
    ax.text(target[1], target[0], "T", ha="center", va="center")

    plt.pause(0.4)
