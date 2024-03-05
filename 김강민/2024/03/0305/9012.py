import sys

input = sys.stdin.readline

number = int(input())

for _ in range(number):
    stk = []
    data = input().strip()

    for i in data:
        if i == '(':
            stk.append(i)
        elif i == ')':
            if len(stk) == 0:
                stk.append(i)
                break
            else:
                stk.pop()
    if len(stk) == 0: 
        print("YES")
    else:
        print("NO")