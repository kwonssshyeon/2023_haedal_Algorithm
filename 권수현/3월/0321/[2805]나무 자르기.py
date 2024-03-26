import sys
input = sys.stdin.readline

n,m=map(int,input().split())
trees=list(map(int,input().split()))

start,end = 0, max(trees)+1
answer=0

while start<=end:
    sum=0
    mid = (start+end)//2
    for tree in trees:
        if tree>mid:
            sum+=(tree-mid)

    if sum>=m:
        start=mid+1
        answer = max(answer,mid)
    else:
        end=mid-1

    
print(answer)