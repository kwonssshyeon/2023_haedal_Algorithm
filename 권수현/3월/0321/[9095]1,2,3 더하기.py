import sys
input = sys.stdin.readline

n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

result = []
for num in nums:
    def solution():
        if num<=2:
            return num
        dp = [1]*(num+1)
        dp[2]=2
        for i in range(3,num+1):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])
        return dp[num]

    print(solution())
        