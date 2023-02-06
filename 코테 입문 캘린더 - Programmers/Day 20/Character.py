def solution(keyinput, board):
    answer = []
    answer.append(0)
    answer.append(0)
    for key in keyinput:
        if key=="right" and answer[0]<=(board[0]//2):
            answer[0]+=1
        elif key=="left" and abs(answer[0])<=(board[0]//2):
            answer[0]-=1
        elif key=="up" and answer[1]<=(board[1]//2):
            answer[1]+=1
        elif key=="down" and abs(answer[1])<=(board[1]//2):
            answer[1]-=1
    
    return answer