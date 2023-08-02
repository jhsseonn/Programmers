def solution(numlist, n):
    answer = []
    result_dict = {}

    for num in numlist:
        result_dict.setdefault(num, abs(n-num))
    
    result_dict = dict(sorted(result_dict.items(), key=lambda x:x[0], reverse=True))
    result_dict = dict(sorted(result_dict.items(), key=lambda x:x[1], reverse=False))
    answer = list(result_dict.keys())

    return answer

#bfs로 풀어볼 수 있지 않을까.. 
#했는데 그래프 만들어줘야 하는 것 같아서 포기하고 그냥 딕셔너리로 품,,

#다른 사람 풀이
#진짜 실화냐 멍청하면 몸이 고생한다 어휴어휴어휴
def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

#bfs 코드 참고
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit