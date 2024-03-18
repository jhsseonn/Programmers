test_case = int(input())
counts = []

def get_new_recruit():
    n = int(input())
    recruit = []
    for i in range(n):
        recruit.append(list(map(int, input().split())))

    recruit.sort(key=lambda x:x[0])
    count = 1
    min = recruit[0][1]
    for i in range(n):
        if (min > recruit[i][1]):
            min = recruit[i][1]
            count+=1

    counts.append(count)

for i in range(test_case):
    get_new_recruit()

for i in counts:
    print(i, end="\n")