def solution(s):
    stringList = list(s)
    splited = []
    same = 0
    diff = 0
    
    for i in range(len(stringList)-1):
        x = stringList[0]
        if stringList[i]==x:
            same+=1
        else:
            diff+=1
        if same==diff:
            word = []
            for j in range(i-(same+diff)+1, i, 1):
                word.append(stringList[j])
                del stringList[j]
            splited.append(''.join(word))
            word.clear()
                
            


    return answer