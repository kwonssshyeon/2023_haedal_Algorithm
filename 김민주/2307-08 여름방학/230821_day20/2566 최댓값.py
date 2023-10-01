# https://www.acmicpc.net/problem/2566 최댓값 (2차원 배열)

import sys

input = sys.stdin.readline

# 배열의 각 셀의 값 초기화 # 인덱스 1부터 씀
array = [[0 for _ in range(10)] for _ in range(10)]
max = array[1][1]

for row in range(1, 10):
  data_list = list(map(int, input().split()))
  for col in range(1, 10):
    array[row][col] = data_list[col-1]

    # 최댓값 저장
    if array[row][col] >= max:
      max = array[row][col]
      
# 출력
for row in range(1, 10):
  for col in range(1, 10):
    if array[row][col] == max:
      print(array[row][col])
      print(f"{row} {col}")
      break
