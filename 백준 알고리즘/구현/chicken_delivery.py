import itertools

N, M = map(int, input().split())
town = []
for i in range(N):
    town.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if town[i][j]==2:
            chicken.append((i, j))
        if town[i][j]==1:
            house.append((i, j))

chicken_delivery = 9999
for comb in itertools.combinations(chicken, M):
    chicken_distance = 0
    for h in house:
        distance = 9999
        for c in comb:
            distance = min(distance, abs(c[0]-h[0])+abs(c[1]-h[1]))
        chicken_distance+=distance
    chicken_delivery = min(chicken_delivery, chicken_distance)

print(chicken_delivery)
