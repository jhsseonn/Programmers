def solution(numbers):
    answer = ""
    number = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    num_string = ""
    for string in numbers:
        num_string+=string
        if num_string in list(number.keys()):
            answer+=number.get(num_string)
            num_string=''
        
    return int(answer)