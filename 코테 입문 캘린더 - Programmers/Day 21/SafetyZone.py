def solution(board):
    answer = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if i==0 or i==len(board)-1:
                if j!=0 and j!=len(board)-1:
                    answer+=1
            elif j==0 or j==len(board)-1:
                answer+=1
            elif board[i][j]==1:
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if board[x][y]==0:
                            answer+=1
    


    
    return answer