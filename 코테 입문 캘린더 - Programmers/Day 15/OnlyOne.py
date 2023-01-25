def solution(s):
    answer = ''
    str_count = {}
    for string in s:
        if string not in list(str_count.keys()):
            str_count[string] = 1
        else:
            str_count[string] += 1
    
    for key in list(str_count.keys()):
        if str_count[key]==1:
            answer+=key
    return ''.join(sorted(answer))