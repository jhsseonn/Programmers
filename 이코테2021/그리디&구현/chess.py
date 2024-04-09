start = input()
x, y = start[1], start[0]

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(row)):
    if row[i] == y:
        y = str(i + 1)

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count = 0
for i in range(8):
    nx = int(x) + dx[i]
    ny = int(y) + dy[i]

    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)

# 문자 아스키코드로 바꾸기
# ord()
ord(start[0])
