def solution(my_string):
    answer = ''
    list_str = list(my_string)
    vowel = ['a', 'e', 'i', 'o', 'u']
    print(list_str)
    for i in list_str:
        if i in vowel:
            continue
        else:
            answer+=i
    return answer

string = input()
print(solution(str(string)))