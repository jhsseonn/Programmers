n = int(input())
direction = list(map(str, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ["U", "D", "L", "R"]

x, y = 1, 1
for d in direction:
    for i in range(4):
        if d == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx >= n or ny < 1 or ny >= n:
        continue
    x, y = nx, ny

print(x, y)
