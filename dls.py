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


def dls(grid, limit):
    stack = [(start, 0)]
    parent = {}
    explored = set()
    frontier = {start}

    expansion_order = {}
    step_count = 1

    while stack:
        current, depth = stack.pop()
        frontier.discard(current)

        if current in explored:
            continue

        explored.add(current)
        expansion_order[current] = step_count
        step_count += 1

        draw_grid(grid, frontier, explored, set(),
                  f"DLS (L={limit})", expansion_order)

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored,
                      set(path), f"DLS (L={limit})", expansion_order)
            return path

        if depth == limit:
            continue

        neighbors = get_neighbors(current, grid)
        for nb in reversed(neighbors):
            if nb not in explored and nb not in frontier:
                parent[nb] = current
                stack.append((nb, depth + 1))
                frontier.add(nb)

    return []
