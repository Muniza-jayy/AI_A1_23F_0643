from collections import deque
from grid import start, target, get_neighbors
from visualisation import draw_grid

def reconstruct_path_bidirectional(parent_s, parent_t, meeting):
    # Path from start -> meeting
    path_s = []
    cur = meeting
    while cur != start:
        path_s.append(cur)
        cur = parent_s[cur]
    path_s.append(start)
    path_s.reverse()

    # Path from meeting -> target (using parents from target side)
    path_t = []
    cur = meeting
    while cur != target:
        cur = parent_t[cur]
        path_t.append(cur)

    return path_s + path_t

def bidirectional_bfs(grid):
    if start == target:
        return [start]

    # BFS from start
    q_s = deque([start])
    parent_s = {}
    visited_s = {start}
    frontier_s = {start}

    # BFS from target
    q_t = deque([target])
    parent_t = {}
    visited_t = {target}
    frontier_t = {target}

    explored = set()

    while q_s and q_t:
        # ---- Expand one step from Start side ----
        current_s = q_s.popleft()
        frontier_s.discard(current_s)
        explored.add(current_s)

        draw_grid(grid, frontier=frontier_s | frontier_t, explored=explored, path=set(),
                  algo="Bidirectional (from S & T)")

        for nb in get_neighbors(current_s, grid):  # strict order
            if nb not in visited_s:
                visited_s.add(nb)
                parent_s[nb] = current_s
                q_s.append(nb)
                frontier_s.add(nb)

                # meet check
                if nb in visited_t:
                    path = reconstruct_path_bidirectional(parent_s, parent_t, nb)
                    draw_grid(grid, frontier=set(), explored=explored, path=set(path), algo="Bidirectional")
                    return path

        # ---- Expand one step from Target side ----
        current_t = q_t.popleft()
        frontier_t.discard(current_t)
        explored.add(current_t)

        draw_grid(grid, frontier=frontier_s | frontier_t, explored=explored, path=set(),
                  algo="Bidirectional (from S & T)")

        for nb in get_neighbors(current_t, grid):  # strict order
            if nb not in visited_t:
                visited_t.add(nb)
                parent_t[nb] = current_t
                q_t.append(nb)
                frontier_t.add(nb)

                # meet check
                if nb in visited_s:
                    path = reconstruct_path_bidirectional(parent_s, parent_t, nb)
                    draw_grid(grid, frontier=set(), explored=explored, path=set(path), algo="Bidirectional")
                    return path

    return []
