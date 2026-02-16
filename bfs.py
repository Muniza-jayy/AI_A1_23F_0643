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

def bfs(grid):
    q = deque([start])
    parent = {}
    explored = set()
    frontier = set([start])

    while q:
        current = q.popleft()
        frontier.discard(current)
        explored.add(current)

        draw_grid(grid, frontier, explored, set(), "BFS")

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "BFS")
            return path

        for nb in get_neighbors(current, grid):
            if nb not in explored and nb not in frontier:
                parent[nb] = current
                q.append(nb)
                frontier.add(nb)

    return []
