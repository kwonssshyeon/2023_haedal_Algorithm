# 10828 스택
# 1. 런타임 에러 대비 입출력 속도 비교 : sys.stdin.readline > raw_input() > input() 
# 2. split(sep='구분자', maxsplit=분할횟수): 문자열을 쪼개어 다시 리스트로 만드는 함수

import sys

stack = []

def isEmpty() -> bool:
  return len(stack) == 0

def push(item):
  stack.append(item)

def pop():
  if not isEmpty():
    return stack.pop(-1)

def peek():
  if not isEmpty():
    return stack[-1]

def size(): return len(stack)

def clear():
  global stack # 전역변수로 지정
  stack = []

if __name__ == "__main__":
  n = int(sys.stdin.readline())
  
  for i in range(n):
    command = sys.stdin.readline().split()
        
    if (command[0] == "push"): 
      push(int(command[1]))
    elif (command[0] == "pop") :
      if isEmpty(): print(-1)
      else : print(pop())
    elif (command[0] == "size"):
      print(size())
    elif (command[0] == "empty"):
      if isEmpty(): print(1)
      else : print(0)
    elif (command[0] == "top"):
      if isEmpty(): print(-1)
      else : print(peek())