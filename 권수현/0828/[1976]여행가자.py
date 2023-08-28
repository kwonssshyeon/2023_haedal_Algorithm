import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = []
for i in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)

visit = list(map(int,input().split()))

parent=[]
for i in range(n+1):
    parent.append(i)


def find_parent(parent,x):
    if parent[x]==x:
        return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]
    

def join_set(parent,a,b):
    a_root = find_parent(parent,a)
    b_root = find_parent(parent,b)
    if a_root > b_root:
        parent[a_root]=b_root
    else:
        parent[b_root]=a_root

def check_set(parent,visit):
    for i in range(m-1):
        a_root = find_parent(parent,visit[i])
        b_root = find_parent(parent,visit[i+1])
        if a_root != b_root:
            return False
    return True



for i in range(n-1):
    for j in range(i+1,n):
        if matrix[i][j]==1:
            join_set(parent,i+1,j+1)
            

if check_set(parent,visit):
    print("YES")
else:
    print("NO")



