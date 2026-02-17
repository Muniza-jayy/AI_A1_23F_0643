from collections import deque
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

def bfs(grid, should_stop=None):
    q = deque([start])
    parent = {}
    explored = set()
    frontier = set([start])

    expansion_order = {}
    step_count = 1

    while q:
        if should_stop and should_stop():
            return []

        current = q.popleft()
        frontier.discard(current)

        if current in explored:
            continue

        explored.add(current)
        expansion_order[current] = step_count
        step_count += 1

        draw_grid(grid, frontier, explored, set(), "BFS", expansion_order)

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "BFS", expansion_order)
            return path

        for nb in get_neighbors(current, grid):
            if nb not in explored and nb not in frontier:
                parent[nb] = current
                q.append(nb)
                frontier.add(nb)

    return []
