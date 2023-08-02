def solution(dots):
    
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]): 
        return 1
    elif slope(dots[0], dots[2]) == slope(dots[1], dots[3]): 
        return 1
    elif slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    else:
        return 0

def slope(a, b):
    return (b[1]-a[1])/(b[0]-a[0])

#너무 쉬웠는데... 몰라서 구글링해봄