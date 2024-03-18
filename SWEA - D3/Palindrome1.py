T = 10

for test_case in range(1, T + 1):
    length = int(input())
    board = list(map(int(input().split)))
    count = 0

    def isPalindromeRow(idx):
        for i in range(0, length):
            if board[idx][i]!=board[idx][length-1-i]:
                return False
        return True
    
    def isPalindromeCol(idx):
        for i in range(0, length):
            if board[i][idx]!=board[length-1-i][idx]:
                return False
        return True

    for i in range(0, length):
        if isPalindromeRow(i):
            count+=1
        if isPalindromeCol(i):
            count+=1

    print(count)
    
    print("#{} {}".format(test_case, count))