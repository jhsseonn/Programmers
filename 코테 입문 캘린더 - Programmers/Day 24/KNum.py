def solution(i, j, k):
    answer = 0

    for num in range(i, j+1):
        num_list = list(str(num))
        # print(num_list)
        if str(k) in num_list:
            answer+=num_list.count(str(k))
            # print(answer)

    return answer

print(solution(10, 50, 5))

#나는 프린트하고 별 짓 다 했는데.. 다른 사람들은 이렇게 한 줄로 끝냈네...

def solution(i, j, k):
    return sum([str(num).count(str(k)) for num in range(i, j+1) ])