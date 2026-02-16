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
    # priority queue items: (cost, tie_break, node)
    pq = []
    tie = 0

    heapq.heappush(pq, (0, tie, start))

    parent = {}
    cost_so_far = {start: 0}

    explored = set()
    frontier = {start}

    while pq:
        current_cost, _, current = heapq.heappop(pq)

        # If this is an outdated entry, skip
        if current_cost != cost_so_far.get(current, float("inf")):
            continue

        frontier.discard(current)
        explored.add(current)

        draw_grid(grid, frontier, explored, set(), "UCS")

        if current == target:
            path = reconstruct_path(parent)
            draw_grid(grid, set(), explored, set(path), "UCS")
            return path

        for nb in get_neighbors(current, grid):  # strict order
            new_cost = current_cost + 1  # cost per action = 1 (as per assignment)

            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                parent[nb] = current
                tie += 1
                heapq.heappush(pq, (new_cost, tie, nb))
                if nb not in explored:
                    frontier.add(nb)

    return []
