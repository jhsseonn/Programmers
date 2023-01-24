def solution(my_string, num1, num2):
    answer = ''
    str_list = list(my_string)
    for i in range(0, len(str_list)):
        str_list[num1] = my_string[num2]
        str_list[num2] = my_string[num1]
    return ''.join(str_list)