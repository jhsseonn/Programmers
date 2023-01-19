import re

def solution(my_string):
    answer = []
    numbers = re.sub(r'[^0-9]', '', my_string)
    answer = list(map(int, list(sorted(numbers))))
    return answer