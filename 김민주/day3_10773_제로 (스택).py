# 10773 제로 (스택)
# sum(list): 리스트 원소의 합 리턴

import sys

stack = []

if __name__ == "__main__":
  k = int(sys.stdin.readline())

  for i in range(k):
    n = int(sys.stdin.readline())

    if n == 0:
      stack.pop(-1)
    else:
      stack.append(n)

  print(sum(stack))
