def solution(num, k):
    answer = -1
    num_str = str(num)
    for i in range(0, len(num_str)):
        if num_str[i]==str(k):
            answer = i+1
            break
    return answer