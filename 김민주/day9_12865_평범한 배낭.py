# https://www.acmicpc.net/problem/12865 평범한 배낭
# 짐을 쪼갤 수 없음... 넣든가 빼든가 둘 중 하나
# 
# n: 짐의 개수
# w, v: 각 짐의 무게와 가치
# k: 담을 수 있는 최대 무게
# 구하는 것: 가치의 최댓값 W

import sys
input = sys.stdin.readline


if __name__ == "__main__":
  n, k = map(int, input().split())
  
  stuff = [[0, 0]] 
  pack = [[0]*(k+1) for _ in range(n+1)] # 물건 개수 * 무게
  #    n \ k   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  
  #   w  |  v  |     |     |     |     |     |     |     |     
  #   6  | 13  |     |  0  |  0  |  0  |  0  |  0  | 13  | 13  
  #   4  |  8  |     |  0  |  0  |  0  |  8  |  8  | 13  | 13  
  #   3  |  6  |     |  0  |  0  |  6  |  8  |  8  | 13  | 14  
  #   5  | 12  |     |  0  |  0  |  6  |  8  | 12  | 13  | 14  
  
  for i in range(n):
    w, v = map(int, input().split())
    stuff.append([w, v])

  # 물건을 담을지 말지... 결정
  for i in range(1, n+1):
    for j in range(1, k+1):
      w = stuff[i][0]; v = stuff[i][1] # 해당 물건의 무게와 가치

      if j < w: # 물건 무게가 최대 무게보다 작으면?
        pack[i][j] = pack[i-1][j] # 윗칸 그대로 가져옴
      else:
        pack[i][j] = max( (pack[i-1][j-w] + v), pack[i-1][j] ) # 둘 중에 뭘 담을지 정해라
  
  print(pack[n][k])
