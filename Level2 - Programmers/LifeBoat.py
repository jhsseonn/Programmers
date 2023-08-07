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