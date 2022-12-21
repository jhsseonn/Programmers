from collections import Counter

def solution(participant, completion):
    answer = ''

    participantsDict = Counter(participant)
    completionsDict = Counter(completion)

    for names in participantsDict.keys():
        if names not in completionsDict.keys():
            answer = names
        if names in completionsDict.keys() and participantsDict["names"]!=completionsDict["names"]:
            answer = names

    return answer

#다른 사람 풀이
#미친.... 콜렉션은 빼기가 가능했다...
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#다른 사람 풀이2
#해시 함수 사용
#파이썬 해시 함수에 대해 공부 해야겠다..
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer