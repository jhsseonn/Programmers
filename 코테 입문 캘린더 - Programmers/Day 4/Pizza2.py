def solution(n):
    piece = lcm(n, 6)
    return piece//6

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b)//gcd(a, b)