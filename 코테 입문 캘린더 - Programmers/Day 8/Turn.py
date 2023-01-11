def solution(emergency):
    answer = []
    for num in emergency:
        turn = 1
        for i in range(0, len(emergency)):
            if num<emergency[i]:
                turn+=1
            else:
                continue
        answer.append(turn)
    return answer