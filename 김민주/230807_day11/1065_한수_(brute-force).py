# https://www.acmicpc.net/problem/1065 한수 (brute-force)
# 구하는 것: 1 <= x <= n인 한수(양의 정수 중 각 자리가 등차수열을 이루는 수)의 개수

import sys
input = sys.stdin.readline

if __name__ == "__main__":
  numₓ = 0
  
  n = int(input())

  for i in range(1, n+1):
    if i < 100: # 두 자리 수까지는 모두 등차수열을 이룸
      numₓ += 1
    elif i < 1000: # 세 자리 수만 검사하면 됨
      hund = i//100
      ten = i%100//10
      one = i%10
      if ten-hund == one-ten :
        numₓ += 1

  print(numₓ)

  # 숏코딩
  # numₓ = sum(1 for i in range(1, n+1) 
  #            if i < 100 
  #            or (i//100 - (i%100)//10 == (i%100)//10 - i%10) )
