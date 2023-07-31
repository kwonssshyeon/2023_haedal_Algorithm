import sys
input = sys.stdin.readline

input_list = [0] * 301
dp = []

n = int(input())
for i in range(n):
    input_list[i] = int(input())

dp.append(input_list[0])
dp.append(max(input_list[0]+input_list[1],input_list[1]))
dp.append(max(input_list[0]+input_list[2],input_list[1]+input_list[2]))
for i in range(3,n):
    dp.append(max(dp[i-2] + input_list[i] , dp[i-3] + input_list[i] + input_list[i - 1]))

if(n<3):
    print(max(dp))
else:
    print(dp.pop())