import math

def solution(a, b):
    answer = 0
    a = a // math.gcd(a,b)
    b = b // math.gcd(a,b)

    if b == 1:
        return 1
    else:
        b_primes = []
        for i in range(1, b//2+1):
            if (b%i==0):
                b_primes.append(i)

        print(b_primes)

        prime_nums=set()
        if 2 in b_primes or 5 in b_primes:
            for prime in b_primes:
                while(prime%2==0):
                    prime_nums.add(prime//2)
                    prime=prime//2
                while(prime%5==0):
                    prime_nums.add(prime//5)
                    prime=prime//5
        else:
            prime_nums = b_primes

        print(prime_nums)

        for num in prime_nums:
            if num!=1 and num!=2 and num!=5:
                return 2
        
        return 1
    

print(solution(12, 21))