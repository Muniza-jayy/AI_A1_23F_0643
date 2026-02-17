import matplotlib.pyplot as plt
import numpy as np
from grid import ROWS, COLS, start, target

# Global axis target (UI will set this once)
UI_AX = None

def set_ui_ax(ax):
    global UI_AX
    UI_AX = ax

def draw_grid(grid, frontier=set(), explored=set(), path=set(),
              algo="", expansion_order=None, ax=None, pause=0.12):

    # Always draw on UI axis if available
    if ax is None:
        ax = UI_AX if UI_AX is not None else plt.gca()

    ax.clear()
    ax.set_title("GOOD PERFORMANCE TIME APP")

    display = np.where(grid == -1, 1, 0)
    ax.imshow(display, interpolation="none")

    ax.set_xticks(np.arange(-0.5, COLS, 1))
    ax.set_yticks(np.arange(-0.5, ROWS, 1))
    ax.grid(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    def fill(cell, color):
        r, c = cell
        rect = plt.Rectangle((c - 0.5, r - 0.5), 1, 1,
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

    # expansion numbers BUT NOT on S/T
    if expansion_order:
        for (r, c), num in expansion_order.items():
            if (r, c) == start or (r, c) == target:
                continue
            ax.text(c, r, str(num), ha="center", va="center", fontsize=8, color="black")

    # draw S/T on top with small box so numbers never override
    ax.text(start[1], start[0], "S",
            ha="center", va="center",
            fontsize=10, color="black",
            bbox=dict(facecolor="white", alpha=0.7, edgecolor="none", pad=1.5))

    ax.text(target[1], target[0], "T",
            ha="center", va="center",
            fontsize=10, color="black",
            bbox=dict(facecolor="white", alpha=0.7, edgecolor="none", pad=1.5))

    plt.pause(pause)
