import sys
input=sys.stdin.readline

t = int(input())
result=[]
for _ in range(t):
    n = int(input())
    def func():
        dp=[1]*(n+1)
        for i in range(2,n+1):
            dp[i]+=(dp[i-2])
        for i in range(3,n+1):
            dp[i]+=(dp[i-3])
        return dp[n]
    result.append(func())

for i in range(t):
    print(result[i])