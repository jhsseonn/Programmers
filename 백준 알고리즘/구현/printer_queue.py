test_case = int(input())
for i in range(test_case):
    n, index = map(int, input().split())
    important = list(map(int, input().split()))

    result = 1
    while important:
        if important[0] < max(important):
            important.append(important.pop(0))
        else:
            if index == 0:
                break
            important.pop(0)
            result+=1

        if index > 0:
            index -= 1
        else:
            index = len(important) - 1

    print(result)
