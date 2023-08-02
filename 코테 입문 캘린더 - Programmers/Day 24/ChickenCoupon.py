def solution(chicken):
    answer = 0
    rest_coupon = 0

    if chicken<10:
        answer+=chicken

    while(chicken>=10):
        rest_coupon += chicken%10
        chicken = chicken//10
        answer += chicken
    
    rest_coupon += chicken
    
    while(rest_coupon>=10):
        answer += rest_coupon//10
        rest_coupon = rest_coupon%10 + rest_coupon//10

    return answer

# 다른 사람 풀이..
def solution(chicken):
    answer = 0
    
    while(chicken>=10):
        div = chicken//10
        mod = chicken%10
        answer += div
        chicken = div+mod

    return answer