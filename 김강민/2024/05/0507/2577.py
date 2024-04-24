import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

number = a * b * c
number = list(str(number))

for i in range(10):
    print(number.count(str(i)))
