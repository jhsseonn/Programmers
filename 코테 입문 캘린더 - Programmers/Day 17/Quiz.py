def solution(quiz):
    answer = []
    for string in quiz:
        numlist = list(string.split(" "))
        if numlist[1]=="+":
            if int(numlist[0])+int(numlist[2])==int(numlist[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(numlist[0])-int(numlist[2])==int(numlist[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer