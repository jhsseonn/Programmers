T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for i in range(2, n-2):
        dif1 = heights[i]-heights[i-2]
        dif2 = heights[i]-heights[i-1]
        dif3 = heights[i]-heights[i+1]
        dif4 = heights[i]-heights[i+2]
        if dif1>0 and dif2>0 and dif3>0 and dif4>0:
            answer+=min(dif1, dif2, dif3, dif4)

    print("#{} {}".format(test_case, answer))