# 10866 덱
# https://www.acmicpc.net/problem/10866
# deque 모듈로 구현
# isEmpty() 만들지 않고 not deq 사용하니까 통과됨

from collections import deque
import sys

deq = deque()

if __name__ == "__main__":
  n = int(sys.stdin.readline())
  
  for i in range(n):
    cmd =  sys.stdin.readline().rstrip().split()

    if cmd[0] == "push_front":
      deq.appendleft(cmd[1])
      
    elif cmd[0] == "push_back":
      deq.append(cmd[1])
      
    elif cmd[0] == "pop_front":
      if not deq: print(-1)
      else: print(deq.popleft())
        
    elif cmd[0] == "pop_back":
      if not deq: print(-1)
      else: print(deq.pop())
        
    elif cmd[0] == "size":
      print(len(deq))
      
    elif cmd[0] == "empty":
      print(int(not deq))
      
    elif cmd[0] == "front":
      if not deq: print(-1)
      else: print(deq[0])
      
    elif cmd[0] == "back":
      if not deq: print(-1)
      else: print(deq[-1])
    
    
    # push_front X: 정수 X를 덱의 앞에 넣는다.
    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    # size: 덱에 들어있는 정수의 개수를 출력한다.
    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.