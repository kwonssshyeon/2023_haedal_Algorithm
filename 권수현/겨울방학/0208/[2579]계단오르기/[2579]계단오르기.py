import sys
input = sys.stdin.readline

n = int(input())
steps=[]
for _ in range(n):
    steps.append(int(input()))

if n<=2:
    print(sum(steps))
    sys.exit(0)

dp = [0]*(n)

dp[0]=steps[0]
dp[1]=steps[0]+steps[1]
if steps[0]>steps[1]:
    check=0
    dp[2]=steps[0]+steps[2]
else:
    check=1
    dp[2]=steps[1]+steps[2]


for i in range(3,n):
    if check==1:
        if dp[i-3]+steps[i-1] > dp[i-2]:
            dp[i] = dp[i-3]+steps[i-1]+steps[i]
        else:
            dp[i] = dp[i-2]+steps[i]
            check=0
    else:
        if dp[i-1] > dp[i-2]:
            dp[i] = dp[i-1]+steps[i]
            check=1
        else:
            dp[i] = dp[i-2]+steps[i]

print(dp[n-1])

