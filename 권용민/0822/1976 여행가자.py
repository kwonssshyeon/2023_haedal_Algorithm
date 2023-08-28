import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [-1 for _ in range(n+1)]
node_level = [1 for _ in range(n+1)]

def find_ancestor(a):
    if parent[a] > -1:
        ancestor_a = find_ancestor(parent[a])
        parent[a] = ancestor_a
        return ancestor_a
    return a

for i in range(n):
    tmp_arr = list(map(int, sys.stdin.readline().split()))
    for j in range(i, n):
        if tmp_arr[j]:
            ancestor_i = find_ancestor(i)
            ancestor_j = find_ancestor(j)
            if ancestor_i == ancestor_j:
                continue
            
            if node_level[ancestor_i] < node_level[ancestor_j]:
                parent[ancestor_i] = ancestor_j
            else:
                parent[ancestor_j] = ancestor_i

            if node_level[ancestor_i] == node_level[ancestor_j]:
                node_level[ancestor_i] += 1

tmp_arr = list(map(int, sys.stdin.readline().split()))
isYes = True
ancestor_base = find_ancestor(tmp_arr[0]-1)
for i in range(1, m):
    if ancestor_base != find_ancestor(tmp_arr[i]-1):
        print("NO")
        isYes = False
        break
if isYes:
    print("YES")
