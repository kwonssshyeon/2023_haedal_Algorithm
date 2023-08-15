# https://www.acmicpc.net/problem/2738 행렬 덧셈

import sys

input = sys.stdin.readline

# 입력
row, col = map(int, input().split())
A = [[0 for _ in range(col)] for _ in range(row)]
B = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
  data_list = list(map(int, input().split()))
  # 한 줄에 여러 개가 들어와서 줄별로 리스트 만들어 저장
  for j in range(col):
    A[i][j] = data_list[j]

for i in range(row):
  data_list = list(map(int, input().split()))
  for j in range(col):
    B[i][j] = data_list[j]

# 출력
for i in range(row):
  for j in range(col):
    print(A[i][j] + B[i][j], end=" ")
  print()
