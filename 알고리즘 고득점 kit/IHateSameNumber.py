def solution(arr):
    answer = []

    for n in arr:
        if len(answer)==0:
            answer.append(n)
        elif answer[len(answer)-1]==n:
            continue
        else:
            answer.append(n)

    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))
