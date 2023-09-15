import itertools

def solution(numbers):
    answer = 0
    num_list = list(numbers.split())
    
    for i in range(1, len(numbers)):
        nCr=itertools.combination(num_list,i)
        for j in nCr:
            if isPrimeNum(j):
                answer+=1
    
    return answer

def isPrimeNum(num):
    i=0
    while i<num//2+1:
        if num%i==0:
            return False
        i+=1
    return True