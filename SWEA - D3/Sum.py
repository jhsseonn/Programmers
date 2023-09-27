T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    # array_list = [[0]*100 for _ in range(100)]

    # x=0
    # while x<len(array):
    #     for i in range(0, 100):
    #         for j in range(100):
    #             array_list[i][j]=array[x]
    #             x+=1

    sum1=sum2=0

    for i in range(0, 100):
        sum_col=sum_row=0
        for j in range(0, 100):
            sum_col+=array[i][j]
            sum_row+=array[j][i]
        sum1+=array[i][i]
        sum2+=array[i][len(array)-i-1]
        sum_list.append(sum_col)
        sum_list.append(sum_row)
        sum_list.append(sum1)
        sum_list.append(sum2)

    print("#{} {}".format(n, max(sum_list)))