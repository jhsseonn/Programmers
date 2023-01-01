from itertools import combinations

def isPrimeNumber(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, (num//2)+1):
            if (num%i==0):
                return False
        return True


def solution(nums):
    answer = 0

    for element in list(combinations(nums, 3)):
        if isPrimeNumber(sum(element)):
            answer+=1

    return answer

#소수 판별 알고리즘 기억하기