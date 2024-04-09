number = input()

result = int(number[0])
for i in range(1, len(number)):
    if result<=1 or int(number[i])<=1:
        result+=int(number[i])
    else:
        result*=int(number[i])

print(result)
