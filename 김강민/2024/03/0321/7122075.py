from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque([])

# 1 x : Queue에 x를 추가한다.
# 2 : Queue에 가장 먼저 들어온 원소를 삭제한다.
# 3 : Queue에 가장 먼저 들어온 원소를 출력한다.
# 4 : Queue에 존재하는 원소의 개수를 출력한다.

for _ in range(n):
    num = list(input().split())

    if num[0] == '1':
        queue.append(num[1])
    elif num[0] == '2' and queue:
        queue.popleft()
    elif num[0] == '3':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif num[0] == '4':
        print(len(queue))

# 진짜 어렵다..........