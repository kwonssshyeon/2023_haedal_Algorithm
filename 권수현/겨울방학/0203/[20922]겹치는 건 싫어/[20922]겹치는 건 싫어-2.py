import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

cnt = [0]*100001
left = result = 0
for right in range(n):
    cnt[nums[right]] += 1

    while cnt[nums[right]] > k:
        cnt[nums[left]] -= 1
        left += 1
    
    if right-left+1 > result:
        result = right-left+1
        
print(result)