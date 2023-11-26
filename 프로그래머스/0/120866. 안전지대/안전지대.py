def solution(board):
    
    pos = []
    
    #지뢰가 있는 위치 저장하기 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==1:
                pos.append([i+1,j+1])
                
    answers = []
    for i in range(len(board)):
        board[i].insert(0,1)
        board[i].append(1)
    board.insert(0,[1 for i in range(len(board[0]))])
    board.append([1 for i in range(len(board[0]))])
    
    
    for x,y in pos:
        board[x][y-1] = 2 #왼쪽 
        board[x][y+1] = 2 #오른쪽
        board[x+1][y] = 2#아래쪽
        board[x-1][y] = 2 #위쪽
        board[x-1][y-1] = 2 
        board[x-1][y+1] = 2 
        board[x+1][y-1] = 2 
        board[x+1][y+1] =2 
        
    result = 0
    for i in board:
        result +=i.count(0)
        
        
        
    return result
        
        
            