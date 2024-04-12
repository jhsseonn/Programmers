n = int(input())
seats = [[0] * n for _ in range(n)]
like_info = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n ** 2):
    input_like = list(map(int, input().split()))
    now_student = input_like[0]
    like_students = input_like[1:]
    # 만족도 계산을 위해 input값을 저장
    like_info.append(input_like)
    result = []

    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                count_like_students = 0
                count_empty = 0

                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if seats[nx][ny] in like_students:
                        count_like_students += 1
                    if seats[nx][ny] == 0:
                        count_empty += 1

                result.append((count_like_students, count_empty, i, j))

    result = sorted(result, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seats[result[0][2]][result[0][3]] = now_student

like_info.sort()

sum = 0
for i in range(n):
    for j in range(n):

        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if seats[nx][ny] in like_info[seats[i][j]-1]:
                count+=1

        if count!=0:
            sum += 10**(count-1)

print(sum)
