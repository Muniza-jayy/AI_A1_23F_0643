from dls import dls

def iddfs(grid, max_depth, should_stop=None):
    for limit in range(max_depth + 1):
        if should_stop and should_stop():
            return [], None
        path = dls(grid, limit, should_stop=should_stop)
        if path:
            return path, limit
    return [], None
