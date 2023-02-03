def solution(array):
    answer = 0
    for num in array:
        for seven in list(str(num)):
            if seven=='7':
                answer+=1
    return answer