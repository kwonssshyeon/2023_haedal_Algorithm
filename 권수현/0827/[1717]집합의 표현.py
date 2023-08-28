import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = []
for i in range(n+1):
    parent.append(i)


def find_parent(parent,x):
    if parent[x]==x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def join_set(parent, a,b):
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    if a_root<b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


def check_set(parent,a,b):
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)
    if a_root == b_root:
        print("YES")
    else:
        print("NO")





for i in range(m):
    cmd, a,b = map(int,input().split())
    if cmd == 0:
        join_set(parent, a,b)
    elif cmd == 1:
    
        check_set(parent,a,b)

