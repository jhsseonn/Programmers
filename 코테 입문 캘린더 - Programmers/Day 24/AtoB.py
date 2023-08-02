def solution(before, after):
    before = before[::-1]
    for i, s in enumerate(after):
        if s!=before[i]:
            return 0
    return 1

#문제 의도 완전히 잘못 파악함,,
#순서를 바꾸는 것이지 뒤집는 게 아니었음..


def solution(before, after):
    
    bnum=getDictionary(before)
    anum=getDictionary(after)

    if sorted(bnum.keys())==sorted(anum.keys()):
        for a in sorted(anum.keys()):
            if bnum[a]!=anum[a]:
                return 0
        return 1
    return 0
    
    
def getDictionary(string):
    snum={}
    for s in string:
        if s not in snum.keys():
            snum[s]=1
        else:
            snum[s]+=1

    return snum

#다른 사람 풀이
#미쳤나... 문제 너무 어렵게 생각함 짜증난다
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0