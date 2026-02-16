from collections import deque
from grid import start, target, get_neighbors
from visualisation import draw_grid


def reconstruct_path(meet_node, parent_start, parent_goal):
    path = []

    # From start to meeting point
    node = meet_node
    while node:
        path.append(node)
        node = parent_start.get(node)

    path.reverse()

    # From meeting point to target
    node = parent_goal.get(meet_node)
    while node:
        path.append(node)
        node = parent_goal.get(node)

    return path


def bidirectional(grid):

    q_start = deque([start])
    q_goal = deque([target])

    parent_start = {start: None}
    parent_goal = {target: None}

    explored_start = set()
    explored_goal = set()

    frontier_start = {start}
    frontier_goal = {target}

    expansion_order = {}
    step_count = 1

    while q_start and q_goal:

        # Expand from start side
        current_start = q_start.popleft()
        frontier_start.discard(current_start)
        explored_start.add(current_start)

        expansion_order[current_start] = step_count
        step_count += 1

        if current_start in explored_goal:
            path = reconstruct_path(current_start,
                                    parent_start,
                                    parent_goal)
            draw_grid(grid, set(),
                      explored_start | explored_goal,
                      set(path),
                      "Bidirectional",
                      expansion_order)
            return path

        for nb in get_neighbors(current_start, grid):
            if nb not in explored_start and nb not in frontier_start:
                parent_start[nb] = current_start
                q_start.append(nb)
                frontier_start.add(nb)

        # Expand from goal side
        current_goal = q_goal.popleft()
        frontier_goal.discard(current_goal)
        explored_goal.add(current_goal)

        expansion_order[current_goal] = step_count
        step_count += 1

        if current_goal in explored_start:
            path = reconstruct_path(current_goal,
                                    parent_start,
                                    parent_goal)
            draw_grid(grid, set(),
                      explored_start | explored_goal,
                      set(path),
                      "Bidirectional",
                      expansion_order)
            return path

        for nb in get_neighbors(current_goal, grid):
            if nb not in explored_goal and nb not in frontier_goal:
                parent_goal[nb] = current_goal
                q_goal.append(nb)
                frontier_goal.add(nb)

        draw_grid(grid,
                  frontier_start | frontier_goal,
                  explored_start | explored_goal,
                  set(),
                  "Bidirectional",
                  expansion_order)

    return []
