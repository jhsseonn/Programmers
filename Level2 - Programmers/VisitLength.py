def solution(dirs):
    answer = 0

    visited = set()
    x, y = 0, 0
    dir = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0)
    }

    for d in dirs:
        dx, dy = dir[d]
        nx = x + dx
        ny = y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        x, y = nx, ny

    return len(visited) // 2
