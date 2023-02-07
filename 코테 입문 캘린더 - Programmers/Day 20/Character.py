def solution(keyinput, board):
    limit_x = (board[0]-1)//2
    limit_y = (board[1]-1)//2

    state = {
        "up": [0, 1],
        "down": [0, -1],
        "right": [1, 0],
        "left": [-1, 0]
    }

    x = y = 0
    for key in keyinput:
        dx, dy = state[key]
        nx, ny = x+dx, y+dy
        if abs(nx)<=limit_x and abs(ny)<=limit_y:
            x, y = nx, ny
    
    return [x, y]