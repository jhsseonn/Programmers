def solution(spell, dic):
    answer = 2

    for word in dic:
        same = 0
        for s in spell:
            if s in word:
                same+=1
        if same==len(spell):
            answer=1

    return answer