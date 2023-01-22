def solution(array, n):
    answer = 0
    gap = 99
    for num in array:
        if num<n:
            g = n-num
            if g<gap:
                gap=g
                answer = num
            if g==gap:
                if answer<num:
                    continue
                else:
                    answer=num
        else:
            g = num-n
            if g<gap:
                gap=g
                answer = num
            if g==gap:
                if answer<num:
                    continue
                else:
                    answer=num
    return answer