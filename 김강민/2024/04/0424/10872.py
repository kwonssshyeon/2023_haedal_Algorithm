import sys
input = sys.stdin.readline

n = int(input())

fac = 1
for i in range(1,n+1):
    fac *= i

print(fac)