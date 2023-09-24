# 1018.py
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

board = []
result = []

for _ in range(n):
    board.append(input())
    print(list)
    
for i in range(n-7):
    for j in range(m-7):
        isB = 0
        isW = 0
        
        for a in range(i, i+8):
            for b in range(j, j+ 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        isB += 1
                    if board[a][b] != 'W':
                        isW += 1
                else:
                    if board[a][b] != 'W':
                        isB += 1
                    if board[a][b] != 'B':
                        isW += 1
 
        result.append(isB)
        result.append(isW)

print(min(result))