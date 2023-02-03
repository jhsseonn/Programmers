def solution(my_str, n):
    answer = []
    string = ""
    for i in range(0, len(my_str)):
        string+=my_str[i]
        if len(string)==n:
            answer.append(string)
            string=""
        elif i==(len(my_str)-1):
            answer.append(string)
    return answer