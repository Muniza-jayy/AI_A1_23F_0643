import matplotlib.pyplot as plt
from grid import create_grid
from bfs import bfs
from dfs import dfs
from ucs import ucs
from dls import dls
from iddfs import iddfs
from bidirectional import bidirectional_bfs


if __name__ == "__main__":
    grid = create_grid()
    plt.figure(figsize=(8,5))
    path = bfs(grid)
    print("Path:", path)
    plt.show()

# if __name__ == "__main__":
#     grid = create_grid()
#     plt.figure(figsize=(8,5))
#     path = dfs(grid)
#     print("Path:", path)
#     plt.show()
    
# import matplotlib.pyplot as plt
# from grid import create_grid
# from ucs import ucs

# if __name__ == "__main__":
#     grid = create_grid()
#     plt.figure(figsize=(8,5))
#     path = ucs(grid)
#     print("Path length:", len(path))
#     print("Path:", path)
#     plt.show()

# if __name__ == "__main__":
#     grid = create_grid()
#     plt.figure(figsize=(8,5))

#     limit = 10  # you can change this for best/worst case screenshots
#     path = dls(grid, limit)

#     print("Depth Limit:", limit)
#     print("Path length:", len(path))
#     print("Path:", path)
#     plt.show()


# if __name__ == "__main__":
#     grid = create_grid()
#     plt.figure(figsize=(8,5))

#     max_depth = 20
#     path, found_limit = iddfs(grid, max_depth)

#     print("Max Depth:", max_depth)
#     print("Found at Depth Limit:", found_limit)
#     print("Path length:", len(path))
#     print("Path:", path)

#     plt.show()

if __name__ == "__main__":
    grid = create_grid()
    plt.figure(figsize=(8,5))

    path = bidirectional_bfs(grid)

    print("Path length:", len(path))
    print("Path:", path)
    plt.show()