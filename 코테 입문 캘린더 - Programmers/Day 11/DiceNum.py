def solution(box, n):
    answer = 1
    number = []
    for length in box:
        number.append(length//n)

    for nums in number:
        answer *= nums

    return answer

#다른 사람 풀이
def solution(box, n):
    answer = 1
    for b in box:
        answer *= b // n
    return answer