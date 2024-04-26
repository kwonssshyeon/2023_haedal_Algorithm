import sys
input = sys.stdin.readline

n, m = map(int, input().split())

print(abs(n - m))
# if n < 0:
#     print(-n + m)
# elif m < 0:
#     print(n - m)
# else:
#     print(n + m)