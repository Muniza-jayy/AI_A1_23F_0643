import matplotlib.pyplot as plt
from grid import create_grid
from bfs import bfs
from dfs import dfs

# if __name__ == "__main__":
#     grid = create_grid()
#     plt.figure(figsize=(8,5))
#     path = bfs(grid)
#     print("Path:", path)
#     plt.show()

if __name__ == "__main__":
    grid = create_grid()
    plt.figure(figsize=(8,5))
    path = dfs(grid)
    print("Path:", path)
    plt.show()