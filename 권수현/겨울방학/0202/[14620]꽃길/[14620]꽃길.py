# 21:23~
import sys
from itertools import combinations, product
input = sys.stdin.readline

n = int(input())

costs=[]
for _ in range(n):
    costs.append(list(map(int,input().split())))

# 씨앗의 범위 1~n-2
# 두 씨앗간 거리 3이상

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def calc(y,x):
    result=costs[y][x]
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        result+=costs[ny][nx]
    return result
    
def isPossible(a,b,c):

    if abs(a[0]-b[0])+abs(a[1]-b[1]) <3:
        return False
    if abs(a[0]-c[0])+abs(a[1]-c[1]) <3:
        return False
    if abs(b[0]-c[0])+abs(b[1]-c[1]) <3:
        return False
    
    return True
    

answer = float('inf')
for seeds in combinations(product(tuple(range(1,n-1)),tuple(range(1,n-1))),3):
    if isPossible(seeds[0],seeds[1],seeds[2]):
        cost = 0
        for i in range(3):
            cost+=calc(seeds[i][0],seeds[i][1])
        answer = min(cost,answer)

print(answer)