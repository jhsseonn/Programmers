from collections import deque

def solution(maps):
    answer = bfs(maps, 0, 0)

    if answer == 1:
        answer = -1

    return answer

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, x, y):
    queue = deque()
    queue.append((x, y))
    n = len(maps)
    m = len(maps[0])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx, ny))

    return maps[n-1][m-1]
