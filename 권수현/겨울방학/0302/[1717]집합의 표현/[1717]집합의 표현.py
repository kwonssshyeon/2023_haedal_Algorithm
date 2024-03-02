import sys
input = sys.stdin.readline

n,m=map(int,input().split())
parents = [i for i in range(n+1)]

def find_root(x):
    while parents[x]!=x:
        x = find_root(parents[x])
    return x

def union(a,b):
    root_a = find_root(a)
    root_b = find_root(b)
    if root_a<root_b:
        parents[root_b]=root_a
    else: parents[root_a]=root_b

def check(a,b):
    if find_root(a)==find_root(b):
        print("YES")
    else: print("NO")

for _ in range(m):
    op,a,b = map(int,input().split())
    if op==0:
        union(a,b)
    elif op==1:
        check(a,b)