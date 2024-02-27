import sys
input = sys.stdin.readline

N, M = map(int, input().split())

chess_board = []
result = []

for _ in range(N):
    chess_board.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        draw1 = 0
        draw2 = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if chess_board[x][y] != 'B':
                        draw1 += 1
                    if chess_board[x][y] != 'W':
                        draw2 += 1
                else:
                    if chess_board[x][y] != 'W':
                        draw1 += 1
                    if chess_board[x][y] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))

