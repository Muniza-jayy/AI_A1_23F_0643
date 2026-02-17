from collections import deque
from grid import start, target, get_neighbors
from visualisation import draw_grid


def reconstruct_meeting_path(parent_fwd, parent_bwd, meet):
    """
    Reconstruct path from start -> meet -> target
    parent_fwd: parents from start side
    parent_bwd: parents from target side
    """
    # start -> meet
    path_fwd = []
    cur = meet
    while cur != start:
        path_fwd.append(cur)
        cur = parent_fwd[cur]
    path_fwd.append(start)
    path_fwd.reverse()

    # meet -> target (using backward parents)
    path_bwd = []
    cur = meet
    while cur != target:
        cur = parent_bwd[cur]
        path_bwd.append(cur)

    return path_fwd + path_bwd


def bidirectional(grid, should_stop=None):
    # Frontier queues
    q_fwd = deque([start])
    q_bwd = deque([target])

    # Parents
    parent_fwd = {}
    parent_bwd = {}

    # Visited sets
    visited_fwd = {start}
    visited_bwd = {target}

    # For visualization
    explored = set()
    frontier = {start, target}

    expansion_order = {}
    step = 1

    while q_fwd and q_bwd:
        if should_stop and should_stop():
            return []

        # ---- Expand one step forward ----
        current_fwd = q_fwd.popleft()
        frontier.discard(current_fwd)
        explored.add(current_fwd)

        if current_fwd not in expansion_order:
            expansion_order[current_fwd] = step
            step += 1

        # meeting check
        if current_fwd in visited_bwd:
            path = reconstruct_meeting_path(parent_fwd, parent_bwd, current_fwd)
            draw_grid(grid, set(), explored, set(path), "Bidirectional", expansion_order)
            return path

        draw_grid(grid, frontier, explored, set(), "Bidirectional", expansion_order)

        for nb in get_neighbors(current_fwd, grid):
            if nb not in visited_fwd:
                visited_fwd.add(nb)
                parent_fwd[nb] = current_fwd
                q_fwd.append(nb)
                frontier.add(nb)

        # ---- Expand one step backward ----
        if should_stop and should_stop():
            return []

        current_bwd = q_bwd.popleft()
        frontier.discard(current_bwd)
        explored.add(current_bwd)

        if current_bwd not in expansion_order:
            expansion_order[current_bwd] = step
            step += 1

        if current_bwd in visited_fwd:
            path = reconstruct_meeting_path(parent_fwd, parent_bwd, current_bwd)
            draw_grid(grid, set(), explored, set(path), "Bidirectional", expansion_order)
            return path

        draw_grid(grid, frontier, explored, set(), "Bidirectional", expansion_order)

        for nb in get_neighbors(current_bwd, grid):
            if nb not in visited_bwd:
                visited_bwd.add(nb)
                parent_bwd[nb] = current_bwd
                q_bwd.append(nb)
                frontier.add(nb)

    return []
