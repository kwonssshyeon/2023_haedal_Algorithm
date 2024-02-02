import sys
from collections import defaultdict,deque
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

dic = defaultdict(deque)

left=0
maximum=0
for right,num in enumerate(nums):
    dic[num].append(right)
    
    if len(dic[num])>k:
        left = max(left,dic[num].popleft()+1)

    maximum = max(right-left+1,maximum)

print(maximum)
