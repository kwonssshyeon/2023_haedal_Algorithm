import sys
from collections import deque

queue = deque()

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    command = list(input().split())

    if command[0] == '1':
        deque.appendleft(command[1])
    elif command[0] == '2':
        deque.append(command[1])
    elif command[0] == '3' and queue:
        deque.popleft()
    elif command[0] == '4' and queue:
        deque.pop()
    elif command[0] == '5':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == '6':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == '7':
        print(len(deque))


