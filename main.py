import matplotlib.pyplot as plt
from grid import create_grid_worst as create_grid


from bfs import bfs
from dfs import dfs
from dls import dls
from iddfs import iddfs
from bidirectional import bidirectional
from ucs import ucs 


def run_algorithm(name, function, *args):
    print("\n==============================")
    print(f"Running Algorithm: {name}")
    print("==============================")

    grid = create_grid()
    plt.figure(figsize=(8, 5))

    result = function(grid, *args)

    if isinstance(result, tuple):
        path = result[0]
    else:
        path = result

    print("Path Length:", len(path))
    print("Path:", path)

    plt.show()




if __name__ == "__main__":

    # BFS
    run_algorithm("Breadth First Search (BFS)", bfs)

    # DFS
    run_algorithm("Depth First Search (DFS)", dfs)

    # DLS
    run_algorithm("Depth Limited Search (DLS)", dls, 10)

    # IDDFS
    run_algorithm("Iterative Deepening DFS (IDDFS)", iddfs, 20)
    
    #UCS
    run_algorithm("Uniform Cost Search (UCS)", ucs)

    # Bidirectional
    run_algorithm("Bidirectional Search", bidirectional)


