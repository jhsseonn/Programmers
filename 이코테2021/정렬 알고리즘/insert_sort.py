array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 1부터 시작하는 이유는 맨 앞에 있는 원소는 고정이라고 가정 하에 뒤의 원소들과 비교 정렬하기 때문
    for j in range(i, 0, -1): # 현재 원소 자리부터 인덱스를 하나씩 줄여가면서 왼쪽 원소들과 비교 정렬함 
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)