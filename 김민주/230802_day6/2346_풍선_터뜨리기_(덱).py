# https://www.acmicpc.net/problem/2346 풍선 터뜨리기

from collections import deque
import sys
input = sys.stdin.readline

# 점검용
# n = 5
# deq = deque(enumerate(map(int, [3, 2, 1, -3, -1]))) 
n = int(input())
deq = deque(enumerate(map(int, input().split())))


if __name__ == "__main__":
  for _ in range(n):
    popped_index, paper = deq.popleft()
    print(popped_index + 1, end=" ")
    
    if paper > 0: 
      deq.rotate(-(paper-1))
    elif paper < 0:
      deq.rotate(-paper) 

    # 원소의 인덱스 찾고
    # pop 하고
    # 인덱스 출력하고
    # 다음 원소로 이동 (rotate() 사용. 덱 길이는 자동으로 줄어듦)