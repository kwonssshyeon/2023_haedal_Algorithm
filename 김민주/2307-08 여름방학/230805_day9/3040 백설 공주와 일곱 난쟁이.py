# https://www.acmicpc.net/problem/3040 백설 공주와 일곱 난쟁이 (brute-force)
# 아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오
## 9개 중에 7개를 찾으면 되니까 빼야할 2개를 빼면 됨! 역발상
## enumerate() 함수는 주로 반복 가능한(iterable) 객체를 순회할 때, 각 원소의 인덱스와 값을 함께 가져올 때 사용됩니다. 각 순회 단계에서 (인덱스, 값)의 형태로 튜플을 반환합니다.

import sys
input = sys.stdin.readline
from typing import List


def findSevenDwarfs(dwarf: List[int]) -> List[int]:
  total = sum(dwarf)
  
  for i in range(8):
    for j in range(i+1, 9):
      if total - dwarf[i] - dwarf[j] == 100:
        return [d for idx, d in enumerate(dwarf) if idx != i and idx != j]
        # i번째와 j번째가 아닌 원소들을 리스트로 리턴하기


if __name__ == "__main__":
  dwarf = [0] * 9
  
  # 입력
  for i in range(9):
    dwarf[i] = int(input())

  # 합이 100이 되는 7개의 수 찾기
  answer = findSevenDwarfs(dwarf)
  
  # 답 출력
  for num in answer:
    print(num)