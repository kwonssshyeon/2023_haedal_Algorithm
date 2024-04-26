import sys
input = sys.stdin.readline

n,m = map(int,input().split())
know = set(map(int,input().split()[1:]))

parent = [i for i in range(n+1)]

def root(x):
    while x!=parent[x]:
        x = parent[x]
    return x


def union(a,b):
    root_a = root(a)
    root_b = root(b)
    if root_a in know:
        parent[root_b] = root_a
    elif root_b in know:
        parent[root_a] = root_b
    else:
        parent[root_b]=root_a
    
parties = []
for _ in range(m):
    temp = list(map(int,input().split()[1:]))
    parties.append(temp)
    if len(temp)>1:
        for party in temp[1:]:
            union(temp[0],party)


answer = 0
for i,party in enumerate(parties):
    flag = 0
    for e in party:
        if root(e) in know:
            flag=1
            break
    if flag==0:
        answer+=1


print(answer)