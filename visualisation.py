import matplotlib.pyplot as plt
import numpy as np
from grid import ROWS, COLS, start, target


def draw_grid(grid, frontier=set(), explored=set(), path=set(),
              algo="", expansion_order=None):

    plt.clf()
    plt.title("GOOD PERFORMANCE TIME APP")

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
        rect = plt.Rectangle((c - 0.5, r - 0.5), 1, 1,
                             facecolor=color,
                             edgecolor="none",
                             alpha=0.85)
        ax.add_patch(rect)

    # Explored
    for cell in explored:
        if cell != start and cell != target:
            fill(cell, "lightgray")

    # Frontier
    for cell in frontier:
        if cell != start and cell != target:
            fill(cell, "khaki")

    # Final Path
    for cell in path:
        if cell != start and cell != target:
            fill(cell, "deepskyblue")

    # Start & Target
    fill(start, "limegreen")
    fill(target, "royalblue")

    ax.text(start[1], start[0], "S", ha="center", va="center")
    ax.text(target[1], target[0], "T", ha="center", va="center")

    # Expansion Numbers
    if expansion_order:
        for (r, c), num in expansion_order.items():
            ax.text(c, r, str(num),
                    ha='center',
                    va='center',
                    color='black',
                    fontsize=8)

    plt.pause(0.4)
