def solution(my_string):
    answer = 0
    num1, calc, num2 = map(str, my_string.split(' '))
    if calc=='+':
        answer = int(num1)+int(num2)
    else:
        answer = int(num1)-int(num2)
    return answer


def solution(my_string):
    return eval(my_string)