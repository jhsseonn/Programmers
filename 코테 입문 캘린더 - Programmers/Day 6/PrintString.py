def solution(my_string, n):
    answer = ''
    for str in my_string:
        for i in range(0, n):
            answer+=str
    return answer