# [2563 색종이](https://www.acmicpc.net/problem/2563)

import sys

input = sys.stdin.readline

cells = 101
whole_area = [["" for _ in range(cells)] for _ in range(cells)]
black_cells = 0

# 입력
num_of_black_paper = int(input())

for i in range(num_of_black_paper):
    ver, hor = map(int, input().split())
    
    for row in range(hor+1, hor+11):
        for col in range(ver+1, ver+11):
            whole_area[row][col] = 1

for row in range(1, cells):
    for col in range(1, cells):
        if whole_area[row][col] == 1:
            black_cells += 1 
            # 색칠 영역이 중복될 수 있으므로 검은 셀 개수 나중에 셈

# 출력
print(black_cells)
