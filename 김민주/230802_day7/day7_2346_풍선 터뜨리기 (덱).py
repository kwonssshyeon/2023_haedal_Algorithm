# https://www.acmicpc.net/problem/2346 풍선 터뜨리기
# 1. 인덱스를 출력해야 하므로 골치 아픔.
#     rotate를 해도 원래 덱의 인덱스 값은 보존되어야 한다. ->
#     덱을 복제해두어야 하나? 했는데 enumerate()와 map()을 사용하면 됨.
# 2. rotate 값을 어떻게 해야하는지 뇌 안 돌아감 이슈
# 3. deq.popleft()가 튜플을 반환할 수도 있나?? 괜히 함수 만들고 시간낭비 함. 

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