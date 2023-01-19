def solution(n):
    answer = []
    primeNumbers = []
    
    for i in range(2, n+1):
        if isPrimeNumber(i):
            primeNumbers.append(i)
    
    for i in primeNumbers:
        while n%i==0:
            if i not in answer:
                answer.append(i)
            n = n//i

    return answer

def isPrimeNumber(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True


#더 간결한 풀이
def solution(n):
    answer = []
    d = 2

    while d<=n:
        if n%d==0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d+=1

    return answer