from dls import dls

def iddfs(grid, max_depth):
    # Try depth limits from 0 up to max_depth
    for limit in range(max_depth + 1):
        path = dls(grid, limit)
        if path:  # found a solution
            return path, limit
    return [], None
