def solution(dots):
    answer=0
    
    dots.sort(key=lambda x:x[0])

    for i in range(len(dots)):
        if dots[i][1]>dots[i+1][0]:
            
    return answer