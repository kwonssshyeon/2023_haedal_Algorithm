import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums=list(map(int,input().split()))
    answer=0
    for i in range(n-1):
        for j in range(i,n):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                answer+=1
    print(answer)
