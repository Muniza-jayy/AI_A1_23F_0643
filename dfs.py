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

def dfs(grid, should_stop=None):
    stack = [start]
    parent = {}
    explored = set()
    frontier = set([start])

    expansion_order = {}
    step_count = 1

    while stack:
        if should_stop and should_stop():
            return []

        current = stack.pop()
        frontier.discard(current)

        if current in explored:
            continue

        explored.add(current)
        expansion_order[current] = step_count
        step_count += 1

        draw_grid(grid, frontier, explored, set(), "DFS", expansion_order)

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "DFS", expansion_order)
            return path

        neighbors = get_neighbors(current, grid)
        for nb in reversed(neighbors):
            if nb not in explored and nb not in frontier:
                parent[nb] = current
                stack.append(nb)
                frontier.add(nb)

    return []
