# def solution(n):
#     return fibonacci(n)%1234567

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)
    
#시간 초과에 런타임 에러,, 마찬가지로 리스트나 딕셔너리로 해결해야할 듯

def solution(n):
    fibonacci = {}
    for i in range(n+1):
        if i==0:
            fibonacci[0]=0
        elif i==1:
            fibonacci[1]=1
        else:
            fibonacci[i]=fibonacci[i-2]+fibonacci[i-1]

    return fibonacci.get(n)%1234567

#해결