import re

def solution(my_string):
    answer = 0
    numbers = list(map(int, list(re.sub(r'[^0-9]', '', my_string))))
    for i in numbers:
        answer+=i
    return answer