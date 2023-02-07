def solution(numbers):
    max = 0
    numbers = sorted(numbers)
    if numbers[0]*numbers[1]>=numbers[-1]*numbers[-2]:
        max = numbers[0]*numbers[1]
    else:
        max = numbers[-1]*numbers[-2]

    return max