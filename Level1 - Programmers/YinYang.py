def solution(absolutes, signs):
    answer = 0

    for i, n in enumerate(absolutes):
        if signs[i]:
            answer+=int(n)
        else:
            answer-=int(n)
    return answer

#다른 사람 풀이
#천재다,,
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
