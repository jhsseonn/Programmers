def solution(my_string):
    answer = 0

    num = ''
    for i in range(0, len(my_string)):
        if my_string[i].isdigit():
            num+=my_string[i]
            if i==(len(my_string)-1):
                answer+=int(num)
        else:
            if num!='':
                answer+=int(num)
            num = ''

    return answer