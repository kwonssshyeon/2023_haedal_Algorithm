import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,money = map(int,input().split())
need = list(map(int,input().split()))
need.insert(0,0)
friends =[i for i in range(n+1)]



def find(friends,x):
    if friends[x]==x:
        return x
    friends[x] = find(friends,friends[x])
    return friends[x]
    '''while문을 이용한다면
    while i!=friends[i]:
        i = friends[i]
    return i
    '''

def union(friends,a,b):
    a_root = find(friends,a)
    b_root = find(friends,b)
    if need[a_root] > need[b_root]:
        friends[a_root]=b_root
    else:
        friends[b_root]=a_root





for i in range(m):
    a,b = map(int,input().split())
    union(friends,a,b)


result = 0
for i in range(1,n+1):
    if friends[i]==i:
        result+=need[i]

if result<=money:
    print(result)
else:
    print("Oh no")
