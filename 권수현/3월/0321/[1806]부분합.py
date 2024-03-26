import sys
input = sys.stdin.readline

n,s=map(int,input().split())
nums=list(map(int,input().split()))

left,right=0,0

sum=0
answer = 100001
while True:
    if sum<s and right<n:
        sum+=nums[right]
        right+=1

    elif sum>=s and left<n:
        answer = min(answer,right-left)
        sum-=nums[left]
        left+=1

    else: 
        break

if answer==100001: print(0)
else: print(answer)
    