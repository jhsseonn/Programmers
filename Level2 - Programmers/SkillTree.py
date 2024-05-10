from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        queue = deque(skill)
        tf = True

        for c in s:
            if c not in skill:
                continue
            else:
                if c == queue[0]:
                    queue.popleft()
                else:
                    tf = False
                    break
        if tf:
            answer += 1

    return answer
