N, M, B = map(int, input().split())
land_heights = []

for i in range(N):
    land_heights.append(list(map(int, input().split())))

max_height = 0
min_height = 256
for i in land_heights:
    if (max_height<max(i)):
        max_height=max(i)
    if (min_height>min(i)):
        min_height=min(i)

result_time = [0] * 257
result_height = 0
for i in range(257):
    plus = 0
    minus = 0
    for j in land_heights:
        for b in j:
            if b >= i:
                minus += b-i
            elif b < i:
                plus += i-b
    if B-plus+minus>=0:
        result_time[i] = minus*2+plus
        if result_time[i] <= result_time[result_height]:
            result_height=i
        

print(result_time[result_height], result_height)