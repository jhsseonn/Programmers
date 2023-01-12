def solution(letter):
    answer = []
    letterList = letter.split()
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for l in letterList:
        for i in range(0, len(morse)):
            if l==morse[i]:
                answer.append(chr(i+97))
    return ''.join(answer)