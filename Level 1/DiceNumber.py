def solution(box, n):
    answer = 1
    number = []
    for length in box:
        number.append(length//n)

    for nums in number:
        answer *= nums

    return answer


#다른 사람 풀이
#그러게... 굳이 나눈 값을 배열로 다시 저장할 필요 없었는데..
def solution(box, n):
    answer = 1
    for length in box:
        answer*=length//n

    return answer