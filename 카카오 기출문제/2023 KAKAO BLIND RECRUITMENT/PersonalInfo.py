# def solution(today, terms, privacies):
#     answer = []
#     term = {}

#     for t in terms:
#         s = t.split(" ")
#         term[s[0]] = s[1]

#     for p in privacies:
#         privacy_list = p.split(" ")
#         expiration = list(map(int, privacy_list[0].split(".")))

#         expiration[0] += int(term.get(privacy_list[1]))//12
#         if int(term.get(privacy_list[1]))%12==0:
#             expiration[1]-=1
#         else:
#             expiration[1] += int(term.get(privacy_list[1]))%12
#         expiration[2] -= 1
#         if expiration[1]>12:
#             expiration[0] += expiration[1]//12
#             expiration[1] %= 12
#         if expiration[2]==0:
#             expiration[2]=28
#         expiration = [str(x) for x in expiration]

#         if len(expiration[1])==1:
#             expiration[1] = expiration[1].zfill(2)
#         if len(expiration[2])==1:
#             expiration[2] = expiration[2].zfill(2)

#         expiration_date = ''.join([str(x) for x in expiration])
#         today = today.replace(".", "")
#         print(expiration_date)
#         if int(expiration_date)<int(today):
#             answer.append(privacies.index(p)+1)

#     return answer

#풀린 코드...
#아직도 날수로 계산하는 방법이랑 개월수로 계산해서 더하고 크기 비교하는 방법이랑 뭐가 다른지 모르겠음..
def solution(today, terms, privacies):
    answer = []
    term = {}
    today_date_list = list(map(int, today.split(".")))
    

    for t in terms:
        s = t.split(" ")
        term[s[0]] = s[1]

    for i, p in enumerate(privacies):
        privacy_list = p.split(" ")
        expiration = list(map(int, privacy_list[0].split(".")))

        last_date = yearToDate(expiration) + int(term.get(privacy_list[1]))*28
        today_date = yearToDate(today_date_list)

        print(last_date)
        print(today_date)

        if last_date<=today_date:
            answer.append(i+1)

    return answer

def yearToDate(date):
    return date[0]*12*28+date[1]*28+date[2]


today1 = "2022.05.19"
terms1 = ["A 6", "B 12", "C 3"]
privacies1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

print(solution(today1, terms1, privacies1))