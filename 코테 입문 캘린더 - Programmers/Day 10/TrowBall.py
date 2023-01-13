def solution(numbers, k):
    idx = 0+2*(k-1)
    if idx>len(numbers):
        idx = idx%len(numbers)
    return numbers[idx]