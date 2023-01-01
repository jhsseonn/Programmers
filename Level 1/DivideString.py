def solution(s):
    stringList = list(s)
    splited = []
    same = 0
    diff = 0
    
    while(len(stringList)!=0):
        compare(stringList, same, diff, splited)

    return len(splited)


def compare(stringList, same, diff, splited):
    for i in range(len(stringList)-1):
        x = stringList[0]
        if stringList[i]==x:
            same+=1
        else:
            diff+=1
        if same == diff:
            divide(same+diff, stringList, splited)
            break


def divide(idx, stringList, splited):
    word = []
    for j in range(idx-1):
        word.append(stringList[j])
        del stringList[j]
    splited.append(''.join(word))
    word.clear()


#시간 초과
#다른 사람 풀이
def solution(s):
    answer=0
    t = ["", 0, 0]
    for i in s:
        if t[0]=="":
            t[0] = i
            t[1] += 1
        else:
            if t[0]==i:
                t[1]+=1
            else:
                t[2]+=1
            if t[1]==t[2]:
                answer+=1
                t = ["", 0, 0]
    
    if t!=["", 0, 0]:
        answer+=1

    return answer

#문자열을 배열화 하지 않고 그냥 풀 수도 있고, 큐를 사용할 수도 있음
#큐 공부 제발 하자...