# 에라토스테네스의 체
import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
prime_number = [True for i in range(M + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화
prime_number[1] = False

for i in range(2, int(math.sqrt(M)) + 1):
    if prime_number[i] == True:
        j = 2
        while i * j <= M:
            prime_number[i * j] = False
            j += 1


for i in range(N, M + 1):
    if prime_number[i]:
        print(i)
