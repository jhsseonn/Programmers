def solution(denum1, num1, denum2, num2):
    answer = []

    m = LCM(num1, num2)
    n = denum1*(m//num1)+denum2*(m//num2)

    m, n = m//GCD(m, n), n//GCD(m, n)

    answer.append(n)
    answer.append(m)

    return answer

def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

def LCM(x, y):
    return (x*y)//GCD(x, y)