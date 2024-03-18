test_case = int(input())
counts = []

def get_new_recruit():
    n = int(input())
    paper = []
    interview = []

    for i in range(n):
        p, i = map(int, input().split())
        paper.append(p)
        interview.append(i)
    
    count = 0
    for i in range(n):
        for j in range(0, n):
            if(paper[i]>paper[j] & interview[i]>interview[j]):
                break
            if(j==n-1):
                count+=1
    
    counts.append(count)

for i in range(test_case):
    get_new_recruit()

for i in counts:
    print(i, end="\n")