import matplotlib.pyplot as plt
from grid import create_grid
from bfs import bfs

if __name__ == "__main__":
    grid = create_grid()
    plt.figure(figsize=(8,5))
    path = bfs(grid)
    print("Path:", path)
    plt.show()
