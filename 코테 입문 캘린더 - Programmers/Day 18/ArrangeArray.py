def solution(my_string):
    answer = ''
    for string in my_string:
        if ord(string)<=90:
            answer+=chr(ord(string)+32)
        else:
            answer+=string
    return ''.join(sorted(answer))