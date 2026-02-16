import heapq
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


def ucs(grid):
    pq = []
    tie = 0

    # (cost, tie_break, node)
    heapq.heappush(pq, (0, tie, start))

    parent = {}
    cost_so_far = {start: 0}

    explored = set()
    frontier = {start}

    expansion_order = {}
    step_count = 1

    while pq:
        current_cost, _, current = heapq.heappop(pq)

        # Skip outdated pq entries
        if current_cost != cost_so_far.get(current, float("inf")):
            continue

        if current in explored:
            continue

        frontier.discard(current)
        explored.add(current)

        expansion_order[current] = step_count
        step_count += 1

        draw_grid(grid, frontier, explored, set(), "UCS", expansion_order)

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "UCS", expansion_order)
            return path

        for nb in get_neighbors(current, grid):
            new_cost = current_cost + 1  # cost per move = 1

            # Relaxation step
            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                parent[nb] = current
                tie += 1
                heapq.heappush(pq, (new_cost, tie, nb))

                if nb not in explored:
                    frontier.add(nb)

    return []
