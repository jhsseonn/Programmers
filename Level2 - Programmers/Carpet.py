def solution(brown, yellow):
    answer = []

    if yellow==1:
        if brown == (yellow+2)*(yellow+2)-yellow:
            answer.append(yellow+2)
            answer.append(yellow+2)
    else:
        for i in range(1, yellow//2+1):
            if yellow%i==0:
                j = yellow//i
                if brown == (i+2)*(j+2)-yellow:
                    answer.append(j+2)
                    answer.append(i+2)
                    break

    return answer