def solution(n, k):
    if n>=10:
        num = n//10
        k = k-num
    return n*12000+k*2000