import sys
input = sys.stdin.readline

n = int(input())

result = 1
for _ in range(n):
    cal = list(input().split())
    if cal[0] == '+':
        result += int(cal[1])
    elif cal[0] == '-':
        result -= int(cal[1])
    elif cal[0] == '*':
        result *= int(cal[1])

print(result % 1000000007)

