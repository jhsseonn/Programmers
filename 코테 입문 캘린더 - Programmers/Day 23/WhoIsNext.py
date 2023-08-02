import numpy as np

def solution(score):
    answer = []

    mean = []
    for s in score:
        mean.append(np.mean(s))

    sort_mean = sorted(mean, reverse=True)

    for m in mean:
        answer.append(sort_mean.index(m)+1)

    return answer

#다른 사람 풀이 너무 참고함...
#아니 근데 이렇게 쉬운걸..