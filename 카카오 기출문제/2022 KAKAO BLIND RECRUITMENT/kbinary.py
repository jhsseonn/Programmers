def solution(n, k):
    answer = []

    kbinary_list = list(convert(n, k).split('0'))
    for kbinary in kbinary_list:
        if not kbinary:
            continue
        num = int(kbinary)
        if isDecimal(num):
            answer.append(num)

    return len(answer)

def convert(n, q):
    rev_base = ''

    while n>0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    
    return rev_base[::-1]

def isDecimal(n):
    if n==1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

print(solution(437674, 3))

#소수 판별할 때 대상 숫자의 제곱근까지만 확인해줘야 시간 초과가 뜨지 않음...
#소수 판별 함수 다시 기억해두기

