import sys
input = sys.stdin.readline

N = int(input())
std = list(map(int, input().split()))

stk = []
target = 1

while std:
    if std[0] == target:
        std.pop(0)
        target += 1
    else:
        stk.append(std.pop(0))
    
    while stk:
        if stk[-1] == target:
            stk.pop()
            target += 1
        else:
            break

if len(stk) == 0:
    print('Nice')
else:
    print('Sad')