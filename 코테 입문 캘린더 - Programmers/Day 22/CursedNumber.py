def solution(n):
    threeXlist = []
    for i in range(300):
        if i%3==0 or ("3" in str(i)):
            continue
        else:
            threeXlist.append(i)

    return threeXlist[n-1]