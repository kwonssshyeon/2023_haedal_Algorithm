import sys

input = sys.stdin.readline

num = int(input())

result = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(0, len(A)):
    result += A[i] * B[i]

print(result)