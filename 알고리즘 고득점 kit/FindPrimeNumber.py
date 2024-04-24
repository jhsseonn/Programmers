import itertools

def solution(numbers):
    number_list = list(map(str, ''.join(numbers)))
    answer = []

    for i in range(1, len(numbers)+1):
        numbers = itertools.permutations(number_list, i)
        for n in numbers:
            if n[0]=="0":
                continue
            else:
                number = ""
                for num in n:
                    number+=num
                if isPrimeNumber(int(number)) and int(number) not in answer:
                    answer.append(int(number))
    return len(answer)

def isPrimeNumber(number):
    if number==0 or number==1:
        return False
    for i in range(2, number//2+1):
        if number%i == 0:
            return False
    return True
