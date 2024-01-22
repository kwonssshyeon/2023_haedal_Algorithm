# 1:42 ~ 1:56

# i = 2, d[i]=3 p[d[i]]->s[i]
# s[i] = p[d[i]]


import sys
input = sys.stdin.readline
n,k = map(int,input().split())

s = list(map(int,input().split()))
d = list(map(int,input().split()))
p = [0 for _ in range(n)]

for _ in range(k):
    for i in range(n):
        p[d[i]-1]=s[i]
    s = p[:]

print(*p)