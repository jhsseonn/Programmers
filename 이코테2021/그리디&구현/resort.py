input = input()
string = []
number = 0

for i in input:
    if i.isalpha():
        string.append(i)
    else:
        number += int(i)

string.sort()

if number!=0:
    string.append(str(number))

print(''.join(string))

# 파이썬 문자열에서 문자가 알파벳인지 구별하는 함수 -> isalpha()
