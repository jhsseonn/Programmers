def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []
    
    for num in arr1:
        a.append(format(num, 'b').zfill(n))
    
    for num2 in arr2:
        b.append(format(num2, 'b').zfill(n))

    for i, bin in enumerate(a):
        barrier = ""
        for k, v in enumerate(bin):
            if v=="1" or b[i][k]=="1":
                barrier+="#"
            else:
                barrier+=" "
        answer.append(barrier)
    
    return answer

array1 = [9, 20, 28, 18, 11]
array2 = [30, 1, 21, 17, 28]
n = 5


print(solution(n, array1, array2))

#다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

#zip이란 걸 쓸 수 있었군... rjust는 또 뭐지... 모르는 거 투성이다,, 공부하자..