def solution(my_string):
    answer = ''
    for string in my_string:
        if 65<=ord(string)<=90:
            answer+=chr(ord(string)+32)
        if 97<=ord(string)<=122:
            answer+=chr(ord(string)-32)
    return answer