def solution(balls, share):
    answer = pactorial(balls)/(pactorial(balls-share)*pactorial(share))

    return answer

def pactorial(n):
    num = 1
    for i in range(n, 0, -1):
        num*=i
    return num