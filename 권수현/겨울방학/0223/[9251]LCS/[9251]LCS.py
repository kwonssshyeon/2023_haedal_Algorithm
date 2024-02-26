import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
n1=len(str1)
n2=len(str2)
dp = [['']*(n2+1) for _ in range(n1+1)]


for i in range(n1):
    for j in range(n2):
        if str1[i]==str2[j]:
            dp[i+1][j+1]=dp[i][j]+str1[i]

        else:
            if len(dp[i][j+1])>len(dp[i+1][j]):
                dp[i+1][j+1]=dp[i][j+1]
            else: dp[i+1][j+1]=dp[i+1][j]

print(len(dp[n1][n2]))
if len(dp[n1][n2])!=0:
    print(dp[n1][n2])