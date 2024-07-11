case = int(input())

for i in range(1, case + 1):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    candies.sort()
    answer = 99999999999999
    for j in range(0, N-K+1):
        diff = candies[j+K-1]-candies[j]
        answer = min(diff, answer)
    print(f"#{i}", answer)
