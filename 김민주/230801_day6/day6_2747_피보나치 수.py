# https://www.acmicpc.net/problem/2747 피보나치 수
# 재귀함수를 썼다 반복문이 기억이 안 난다
# 시간 초과돼서 반복문으로 구현 (DP)


def fib(n) -> int:
  fib_list = [0, 1]

  for i in range(2, n + 1):
    fib_list.append(fib_list[i - 1] + fib_list[i - 2])

  return fib_list[n]


if __name__ == "__main__":
  n = int(input())

  print(fib(n))

# def fib(n) -> int:
#   if n == 0 or n == 1:
#     return n
#     # f[0] = 0; f[1] = 1

#   else:
#     return fib(n-1) + fib(n-2)
