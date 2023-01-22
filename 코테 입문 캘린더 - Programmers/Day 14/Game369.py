def solution(order):
    answer = 0
    game = ['3', '6', '9']
    for num in str(order):
        if num in game:
            answer+=1
    return answer