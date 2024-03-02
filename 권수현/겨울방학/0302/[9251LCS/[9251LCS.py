import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
n1 = len(str1)
n2 = len(str2)
dp = [['' for _ in range(n1+1)]for _ in range(n2+1)]

for i in range(n1):
    for j in range(n2):
        if str1[i]==str2[j]:
            dp[i+1][j+1]=dp[i][j]+str1[i]

        else:
            if len(dp[i+1][j])>len(dp[i][j+1]):
                dp[i+1][j+1]=dp[i+1][j]
            else: dp[i+1][j+1]=dp[i][j+1]


print(len(dp[n1][n2]))
