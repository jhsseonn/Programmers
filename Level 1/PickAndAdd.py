def solution(numbers):
    answer = []

    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            answer.append(numbers[i-1]+numbers[j])

    return sorted(set(answer))