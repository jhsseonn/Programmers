def solution(hp):
    j = hp//5
    b = (hp-(5*j))//3
    i = (hp-(5*j))%3
    return j+b+i