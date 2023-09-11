# 테스트 죄다 실패^^

# def solution(people, limit):
#     answer = 0

#     people = sorted(people)
#     kg = 0

#     for p in people:
#         kg+=p
#         if (kg>limit):
#             answer+=1
#             kg = p
#         if people.index(p)==(len(people)-1):
#             answer+=1

#     return answer

# 그리디 알고리즘 공부 후 2번째 시도~

def solution(people, limit):
    answer = 0

    people.sort()

    start = 0
    end = len(people)-1

    while start < end:
        if people[start]+people[end]<=limit:
            answer+=1
            start+=1
            end-=1
        else:
            start+=1

    return answer

# 다른 사람 풀이...
# 내가 생각한 방식대로라면 sort를 reverse로 해야했음.. 
# 근데 오름차순으로 sort 해놓고 이게 왜 0이 나오지 하는 멍청한 생각을 하고 있었음 바본가
def solution(people, limit):
    answer = 0

    people.sort()

    a = 0
    b = len(people)-1
    while a<b:
        if people[a]+people[b]<=limit:
            a+=1
            answer+=1
        b-=1

    return len(people)-answer