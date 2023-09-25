T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    box_list = list(map(int, input().split()))
 
    while n>0:
        box_list = sorted(box_list)
        box_list[0]+=1
        box_list[-1]-=1
        n-=1
         
    box_list = sorted(box_list)
    dump = box_list[-1]-box_list[0]
 
    print("#{} {}".format(test_case, dump))