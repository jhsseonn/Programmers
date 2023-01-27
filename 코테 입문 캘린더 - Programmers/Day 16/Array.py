def solution(my_string):
    num1, calc, num2 = map(str, my_string.split(" "))
    if calc=="+":
        return int(num1)+int(num2)
    return int(num1)-int(num2)