def solution(bin1, bin2):

    return str(bin(toDecimal(bin1)+toDecimal(bin2)))

def toDecimal(num):
    result = 0
    binary = list(str(num).split()).reverse()

    
    
    return result