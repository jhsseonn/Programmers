def solution(polynomial):
    answer = ''

    poly = list(map(str, polynomial.split(" + ")))
    num = 0
    num2 = 0
    for p in poly:
        if p.isnumeric():
            num2+=int(p)
        else:
            if p=="x":
                num+=1
            if "x" in p and p!="x":
                num+=int(p[:-1])
            
    if num!=0 and num2!=0:
        answer = "{}x + {}".format(num, num2)
    if num!=0 and num2==0:
        answer = "{}x".format(num)
    if num==1 and num2!=0:
        answer = "x + {}".format(num2)
    if num==1 and num2==0:
        answer = "x"
    if num==0 and num2!=0:
        answer = "{}".format(num2)
    if num==0 and num2==0:
        answer = "0"

    return answer