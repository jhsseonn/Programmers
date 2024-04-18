import copy

R, C = map(int, input().split())
map_before = []

for _ in range(R):
    map_before.append(list(input()))

map_after = copy.deepcopy(map_before)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
land_count = 0

for i in range(R):
    for j in range(C):
        if map_before[i][j]=='X':
            sea_count = 0
            land_count+=1
            for n in range(4):
                nx = i + dx[n]
                ny = j + dy[n]

                if (0<=nx<R and 0<=ny<C):
                    if map_before[nx][ny]==".":
                        sea_count+=1
                else:
                    sea_count+=1
                    continue

            if sea_count >= 3:
                map_after[i][j]="."
                land_count-=1

if land_count==0:
    print("X")
else:
    startR, endR = 0, 0
    for i in range(R):
        if "X" in map_after[i]:
            startR = i
            break
    for i in range(R-1, -1, -1):
        if "X" in map_after[i]:
            endR = i
            break
    
    idx = []
    for j in range(C):
        for i in range(startR, endR+1):
            if map_after[i][j]=="X":
                idx.append(j)
                break
    
    for i in map_after[startR:endR+1]:
        print(''.join(i[idx[0]:idx[-1]+1]))