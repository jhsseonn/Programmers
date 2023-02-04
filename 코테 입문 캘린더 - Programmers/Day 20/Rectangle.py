def solution(dots):
    x = 0
    y = 0
    for i in range(1, len(dots)):
        if dots[i-1][0]!=dots[i][0]:
            x = abs(dots[i-1][0]-dots[i][0])
        if dots[i-1][1]!=dots[i][1]:
            y = abs(dots[i-1][1]-dots[i][1])
    return x*y