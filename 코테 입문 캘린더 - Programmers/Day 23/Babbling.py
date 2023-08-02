def solution(babbling):
    answer = 0

    babbles = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for babble in babbles:
            while(babble in word):
                word = (' ').join(word.split(babble))
                print(word)
        if word.isspace():
            answer+=1
            
    return answer