def solution(age):
    answer = ''
    for num in list(str(age)):
        if num=='0':
            answer+="a"
        elif num=='1':
            answer+="b"
        elif num=='2':
            answer+="c"
        elif num=='3':
            answer+="d"
        elif num=='4':
            answer+="e"
        elif num=='5':
            answer+="f"
        elif num=='6':
            answer+="g"
        elif num=='7':
            answer+="h"
        elif num=='8':
            answer+="i"
        elif num=='9':
            answer+="j"
    return answer