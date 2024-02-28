# dfs 백트래킹 -> 전체를 새로 구할 필요없이 이전에 계산한데서 추가로 연산되기 때문
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
opps = list(map(int,input().split()))

mini,maxi = float('inf'),-float('inf')

def dfs(cnt,num,plus,minus,multi,divide):
    global mini, maxi
    
    if cnt==n:
        mini = min(num,mini)
        maxi = max(num,maxi)
        return
    
    if plus:
        dfs(cnt+1, num+nums[cnt],plus-1,minus,multi,divide)
    if minus:
        dfs(cnt+1, num-nums[cnt],plus,minus-1,multi,divide)
    if multi:
        dfs(cnt+1, num*nums[cnt],plus,minus,multi-1,divide)
    if divide:
        if num>=0:
            dfs(cnt+1, num//nums[cnt],plus,minus,multi,divide-1)
        else:
            num*=(-1)
            num//=nums[cnt]
            num*=(-1)
            dfs(cnt+1, num,plus,minus,multi,divide-1)
        

dfs(1,nums[0],opps[0],opps[1],opps[2],opps[3])

print(maxi)
print(mini)

# (cnt, 현재까지 계산된 수, 4개 연산자 각각 남은 개수)

