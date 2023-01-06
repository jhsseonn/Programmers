from collections import Counter

def solution(array):
    result = 0
    count = Counter(array)
    countset = count.most_common()
    maxCount = countset[0][1]

    mode = []
    for set in countset:
        if set[1]==maxCount:
            mode.append(set[0])

    if len(mode)>1:
        result = -1
    else:
        result = mode[0]

    return result

# 다른 사람 풀이
# 이해가 안감.... 뭐지.. 어떻게 푼거지..
def solution(array):
    while len(array)!=0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i==0: return a
    return -1