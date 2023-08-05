import sys
input = sys.stdin.readline

target, num = map(int, input().split())

hotels=[]
for i in range(num):
    cost, benefit = map(int, input().split())
    hotels.append([cost, benefit])


INF = 100000
# result배열 범위 주의
# 증가한 고객의 최대값은 1000이지만 한번의 비용으로 얻을 수 있는 고객수가 최대 100이기 때문에 dp배열의 최대값은 1000+100이 되어야함.
result = [INF]*(target+100)
result[0]=0
for cost, benefit in hotels:
    for i in range(benefit,target+100):
        result[i]=min(result[i-benefit]+cost, result[i])


print(min(result[target:]))
