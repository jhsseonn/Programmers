from itertools import permutations

def solution(numbers):

    perms = list(permutations(numbers, len(numbers)))
    stringPerm = ["".join(list(map(str, i))) for i in perms]

    return max(stringPerm)

#permutation 사용 시간 초과

#lambda 함수 사용
def solution(numbers):

    perms = list(map(str, numbers))
    perms.sort(key = lambda x:x*3, reverse=True)

    return str(int(''.join(perms)))