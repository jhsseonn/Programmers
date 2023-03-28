import math

def solution(a, b):
    gcd = math.gcd(a,b)
    a = a//gcd
    b = b//gcd

    if b == 1 or b == 2 or b == 5:
        return 1
    else:
        b_primes = []
        for i in range(2, b//2+1):
            if (b%i==0):
                b_primes.append(i)

        if not b_primes:
            b_primes.append(b)

        prime_nums=set()
        for prime in b_primes:
            while(prime%2==0):
                prime_nums.add(2)
                prime=prime//2
            while(prime%5==0):
                prime_nums.add(5)
                prime=prime//5
            if prime!=1: prime_nums.add(prime)

        for num in prime_nums:
            if num!=2 and num!=5:
                return 2
        
        return 1


#다른 사람들 풀이...
from math import gcd
def solution(a, b):
    b //= gcd(a, b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2

#진짜 개허무하다..