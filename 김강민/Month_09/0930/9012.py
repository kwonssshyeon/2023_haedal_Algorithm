import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    line = input().strip()
    stk = []

    for i in line:
        if i == '(':
            stk.append('(')
        elif i == ')':
            if len(stk) == 0:
                stk.append(')')
                break
            else:
                stk.pop()

    if len(stk) != 0:
        print('NO')
    else:
        print('YES')