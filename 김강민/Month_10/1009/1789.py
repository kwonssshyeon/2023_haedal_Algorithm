import sys
input = sys.stdin.readline

S = int(input())

total = 0
arr = []
i = 0

while total <= S:
    if i == 0:
        i += 1
        total += i
    else:
        arr.append(i)
        i += 1
        total += i


print(len(arr))