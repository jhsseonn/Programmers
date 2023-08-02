def solution(id_list, report, k):
    answer = []
    report_dict = {}
    reporter = {}

    for rep in report:
        report_content = rep.split(" ")
        if report_content[1] in report_dict:
            report_dict[report_content[1]].add(report_content[0])
        else:
            report_dict[report_content[1]] = set([report_content[0]])

    for id in id_list:
        reporter[id] = 0

    for v in report_dict.values():
        if len(v)>=k:
            for i in v:
                if i not in reporter.keys():
                    reporter[i]=1
                else:
                    reporter[i]+=1

    for id in id_list:
        if id in reporter.keys():
            answer.append(reporter[id])

    return answer


#example 1
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))

#example 2
id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3

print(solution(id_list2, report2, k2))


#다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

#진짜 개깔끔하다... 와 reports를 저렇게 만들 수 있군... 와... answer list 추가를 저렇게 하면 되는군.... 대박,,