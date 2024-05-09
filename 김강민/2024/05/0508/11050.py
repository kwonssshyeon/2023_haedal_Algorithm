import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

a,b = 1,1

for i in range(num[1]):
    a *= num[0] - i
    b *= num[1] - i

print(a//b)