def solution(dots):
    answer=0
    
    same = []
    dots.sort(key=lambda x:(x[0], x[1]))

    for i in range(len(dots)-1):
        if dots[i][1]>dots[i+1][0]:
            if dots[i][1]>dots[i+1][1]:
                same.append(dots[i+1])
            else:
                same.append([dots[i+1][0], dots[i][1]])
        
    if not same:
        return 0
    else:
        answer+=same[0][1]-same[0][0]
        if len(same)>1:
            if same[1][0]<same[0][1]:
                answer+=same[1][1]-same[0][1]
            else:
                answer+=same[1][1]-same[1][0]
    return answer

# print(solution([[-5, -3], [-5, -2], [-3, -1]]))


#히든 테케 2개 해결 못함..
#다른 사람 풀이
def solution(lines):
    table = [set([]) for _ in range(200)] # -100~100까지 각 선분들의 등장 count 초기화
    for index, line in enumerate(lines):
        x1, x2 = line
        for x in range(x1, x2):
            table[x + 100].add(index) # 선분에 음수가 들어있을 수도 있으므로 +100

    answer = 0
    for line in table:
        if len(line) > 1:
            answer += 1

    return answer