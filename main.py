import matplotlib.pyplot as plt
from grid import create_grid
from bfs import bfs
from dfs import dfs
from ucs import ucs
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
    
import matplotlib.pyplot as plt
from grid import create_grid
from ucs import ucs

if __name__ == "__main__":
    grid = create_grid()
    plt.figure(figsize=(8,5))
    path = ucs(grid)
    print("Path length:", len(path))
    print("Path:", path)
    plt.show()
