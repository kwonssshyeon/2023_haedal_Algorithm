import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


dp = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # dp 배열을 미리 만들어두고
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]
        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    # ~1의 연산만 시행
    result = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)