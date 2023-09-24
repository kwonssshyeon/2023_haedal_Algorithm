import sys

input = sys.stdin.readline
N = int(input())
result = 0
branch = 64
branch_sum = 0
while N != branch_sum:
    if branch + branch_sum <= N:
        branch_sum += branch
        result += 1
    branch /= 2
print(result)
