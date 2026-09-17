def solution(board):
    
    
    # 정사각형의 기준  가로길이 = 세로길이
    # 각점을 오른쪽 아래로 생각하고
    # 왼쪽, 위, 왼쪽 위 확인해서 더하기 
    # 가장 작은값 찾기
    
    
    # 1인 위치 찾기
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] >= 1:
               board[i][j] = min(board[i][j-1]+1, board[i-1][j]+1, board[i-1][j-1]+1)
    
    sum = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > sum:
                sum = board[i][j]
    
    return sum*sum
                
                