import copy

r, c = map(int, input().split())
map_before = []

for _ in range(r):
    map_before.append(list(map(str, input().split())))

map_after = copy.deepcopy(map_before)
land_count = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(r):
    for j in range(c):
        if map_before[i][j]=="X":
            count = 0
            land_count+=1
            for n in range(4):
                nx = i + dx[j]
                ny = i + dy[j]

                # 바다 카운트
                if (nx < 0 | nx >= c | ny < 0 | ny >= r):
                    count+=1
                elif map_before[nx][ny]==".":
                    count+=1
                
            if count>=3:
                map_after[i][j]=="."
                land_count-=1
            else:
                map_after[i][j]=="X"

if land_count==0:
    print("X")
else:
    startR = 0
    endR = 0
    for i in range(r):
        if "X" in map_after[i]:
            startR = i
            break
    for i in range(r-1, -1, -1):
        if "X" in map_after[i]:
            endR = i
            break

    idx = []
    for j in range(c):
        for i in range(startR, endR+1):
            if 'X'==map_after[i][j]:
                idx.append(j)

    for i in map_after[startR:endR+1]:
        print(''.join(i[idx[0]:idx[-1]+1]))