from collections import deque
import sys
input = sys.stdin.readline

class_num,n = map(int,input().split())

classes = [[] for _ in range(class_num+1)]
check = [0]*(class_num+1)
dp = [0]*(class_num+1)

for i in range(n):
    pre,after = map(int, input().split())
    classes[pre].append(after)
    check[after]+=1

#print(classes)
queue = deque()
for i in range(1, class_num+1):
    if check[i]==0:
        queue.append(i) #진입차수가 0이면 삽입
        dp[i]=1
        


while queue:
    point = queue.popleft()
    for i in classes[point]:
        check[i]-=1
        dp[i]=dp[point]+1
        if check[i]==0:
            queue.append(i)

print(*dp[1:])







"""
모든 과목에 대해 같은 방식으로 수행하면 시간초과 발생
블로그 보니까 위상정렬이라는 것을 이용함
선수과목이 몇개인지 먼저 카운트를 하고(check) 위상정렬을 이용
위상정렬??
"""
