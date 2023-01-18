def solution(n):
    answer = 0
    pactorial = 1
    for i in range(1, 11):
        pactorial*=i
        if pactorial>n:
            answer = i-1
            break
        elif pactorial==n:
            answer = i
            break
        else:
            continue
    return answer