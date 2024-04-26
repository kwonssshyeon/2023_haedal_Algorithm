import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cal = (a + b) * (a - b)

print(cal)

