import sys

input = sys.stdin.readline

arr_first = [list(map(int, input().split())) for _ in range(9)]

max = 0
max_row, max_column = 0, 0

for i in range(9):
    for j in range(9):
        if max <= arr_first[i][j]:
            max_row = i + 1
            max_column = j + 1
            max = arr_first[i][j]

print(max)
print(max_row, max_column)