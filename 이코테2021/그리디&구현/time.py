n = int(input())

# result = 0
# for i in range(n):
#     if i == 3 or i == 13 or i == 23:
#         result += 60 * 60
#     result += 15 * 60 + 45 * 15
#
# print(result)
# 이 때 루프를 정확히 n까지 돌던데 왜지,,,

# 답안 예시
result = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                result += 1

print(result)
