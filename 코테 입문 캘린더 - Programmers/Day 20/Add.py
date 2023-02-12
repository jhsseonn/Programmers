def solution(polynomial):
    answer = ''

    poly = list(map(str, polynomial.split(" + ")))
    num = 0
    num2 = 0
    for p in poly:
        if ("x" in p) and p!="x":
            num+=int(p[0])
        if p=="x":
            num+=1
        if "x" not in p:
            num2+=int(p)

    if num2!=0:
        answer = "{}x + {}".format(num, num2)
    else:
        answer = "{}x".format(num)

    return answer