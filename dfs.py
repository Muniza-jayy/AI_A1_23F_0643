from grid import start, target, get_neighbors
from visualisation import draw_grid

def reconstruct_path(parent):
    cur = target
    path = [cur]
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

def dfs(grid):
    stack = [start]
    parent = {}
    explored = set()
    frontier = set([start])

    while stack:
        current = stack.pop()   # LIFO
        frontier.discard(current)

        if current in explored:
            continue
        explored.add(current)

        draw_grid(grid, frontier, explored, set(), "DFS")

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "DFS")
            return path

        # Strict order: for DFS, push neighbors in reverse
        # so that when popped, they expand in your required order.
        neighbors = get_neighbors(current, grid)
        for nb in reversed(neighbors):
            if nb not in explored and nb not in frontier:
                parent[nb] = current
                stack.append(nb)
                frontier.add(nb)

    return []
