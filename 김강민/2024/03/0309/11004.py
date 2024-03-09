import sys

input = sys.stdin.readline

N, K = map(int, input().split())

num = list(map(int, input().split()))

num.sort()

print(num[K-1])

# 기본적인 입출력 다 까먹었네..