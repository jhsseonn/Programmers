def solution(slice, n):
    answer = 0
    if slice>=n:
        answer = 1
    else:
        if n%slice==0:
            answer=(n//slice)
        else:
            answer = (n//slice)+1
    return answer