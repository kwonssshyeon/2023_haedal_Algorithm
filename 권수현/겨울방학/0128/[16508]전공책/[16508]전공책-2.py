import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

target = input().strip()
n = int(input())
books = {}

for _ in range(n):
    a,b = map(str,input().split())
    books[b]=int(a)

def solution(items):
    dic = defaultdict(int)
    sum=0
    for item in items:
        sum+=books[item]
        for c in item:
            dic[c]+=1

    for c in target:
        if dic[c]==0:
            return float('inf')
        dic[c]-=1

    return sum


min_cost=float('inf')
for i in range(1,n+1):
    for items in combinations(books.keys(),i):
        min_cost = min(min_cost,solution(items))
        
        
        
           
if min_cost==float('inf'):
    print(-1)
else:
    print(min_cost)