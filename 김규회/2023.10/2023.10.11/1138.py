# 1138.py
# https://www.youtube.com/watch?v=0gacBlazGh0

import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int,input().split()))

ans = [0] * n

for i in range(1,n+1):
    t = h[i-1]
    cnt = 0
    for j in range(n):
        if cnt == t and ans[j] == 0:
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1
            
print(*ans)
    