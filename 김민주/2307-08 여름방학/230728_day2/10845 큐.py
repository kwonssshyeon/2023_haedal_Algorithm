# 10845 큐 - 선형큐로 구현
# 스택과 동일하게 리스트로 구현

import sys

queue = []

def isEmpty() -> bool:
  return len(queue) == 0

def enqueue(item):
  queue.append(item)

def dequeue():
  if not isEmpty():
    return queue.pop(0)

def front():
  if not isEmpty():
    return queue[0]

def rear():
  if not isEmpty():
    return queue[-1]

def size(): return len(queue)

def clear():
  global queue # 전역변수로 지정
  queue = []


if __name__ == "__main__":
  n = int(sys.stdin.readline())
  
  for i in range(n):
    command = sys.stdin.readline().split()
        
    if (command[0] == "push"): 
      enqueue(int(command[1]))
    elif (command[0] == "pop") :
      if isEmpty(): print(-1)
      else : print(dequeue())
    elif (command[0] == "size"):
      print(size())
    elif (command[0] == "empty"):
      if isEmpty(): print(1)
      else : print(0)
    elif (command[0] == "front"):
      if isEmpty(): print(-1)
      else : print(front())
    elif (command[0] == "back"):
      if isEmpty(): print(-1)
      else : print(rear())
