def solution(array):
    answer = []
    num = array[0]
    index = 0
    for i in range(1, len(array)):
        if array[i]>num:
            num=array[i]
            index=i
    answer.append(num)
    answer.append(index)
    return answer