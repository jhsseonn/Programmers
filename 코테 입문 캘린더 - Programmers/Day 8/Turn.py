def solution(emergency):
    answer = [1*len(emergency)]
    for i in range(0, len(emergency)):
        if emergency[i]<emergency[i+1]:
            answer[i]+=1
        else:
            answer[i+1]+=1
    return answer