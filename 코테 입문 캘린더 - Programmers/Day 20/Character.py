def solution(keyinput, board):
    answer = []
    x=0
    y=0
    for key in keyinput:
        if key=="up":
            y+=1
        if key=="down":
            y-=1
        if key=="left":
            x-=1
        if key=="right":
            x+=1
    if abs(x)>=(board[0]//2):
        if x<0:
            x = -(board[0]//2)
        else:
            x = board[0]//2
    if abs(y)>=(board[1]//2):
        if y<0:
            y = -(board[1]//2)
        else:
            y = board[1]//2
    answer.append(x)
    answer.append(y)
    return answer