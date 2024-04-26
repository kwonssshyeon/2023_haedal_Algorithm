import sys
input = sys.stdin.readline

num = list(input().split())

sum = 0
for i in num:
    sum += (int(i)**2)
print(sum % 10)