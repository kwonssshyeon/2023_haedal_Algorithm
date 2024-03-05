import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
parent=[i for i in range(n+1)]
plan = list(map(int,input().split()))

def root(x):
    while parent[x]!=x:
        x = root(parent[x])
    return x

def union(a,b):
    root_a = root(a)
    root_b = root(b)
    if root_a<root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def check(a,b):
    if root(a-1)==root(b-1):
        return True
    else: return False

for i in range(n):
    for j in range(i):
        if graph[i][j]==1:
            union(i,j)

prev=plan[0]
answer = True
for now in plan[1:]:
    if not check(prev,now):
        answer = False
        break
    prev = now


if answer:
    print("YES")
else: print("NO")


