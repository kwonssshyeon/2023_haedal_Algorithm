def solution(board):
    answer = 0
    dx=[-1, -1, 0, 1, 1, 1, 0, -1]
    dy=[0, 1, 1, 1, 0, -1, -1, -1]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] == 0:
                        answer += 1
                        board[nx][ny] = 2
    
    return answer
                       
print(solution([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0]]))
