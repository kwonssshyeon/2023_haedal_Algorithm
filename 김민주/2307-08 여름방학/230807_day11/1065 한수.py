# https://www.acmicpc.net/problem/1065 한수 (brute-force)

import sys
input = sys.stdin.readline

if __name__ == "__main__":
  n = int(input())

  numₓ = 0
  for i in range(1, n+1):
    if i < 100: # 두 자리 수까지는 모두 등차수열을 이룸
      numₓ += 1
    elif i < 1000: # 세 자리 수만 검사
      hund = i//100
      ten = i%100//10
      one = i%10
      if ten-hund == one-ten :
        numₓ += 1

  print(numₓ)
  
