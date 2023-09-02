from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

indegree=[0]*(v+1)
graph=[[] for _ in range(v+1)]
count = [[]for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int,input().split())
    #a를 만들기 위해 b가 c개 필요
    #5를 만들기 위해 1이 2개 필요
    #graph[1]=[[5,2], ]
    graph[b].append([a,c])
    indegree[a]+=1
    count[a].append([b,c])


# 위상정렬 --> 부품 조립순서 구함
result=[]
basic=[]
queue = deque()
for i in range(1,v+1):
    if indegree[i]==0:
        queue.append(i)
        basic.append(i)

while queue:
    now = queue.popleft()
    result.append(now)

    for i,cnt in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            queue.append(i)



# 동적계획법 --> 필요한 부품개수 구함
count_result=[0]*(v+1)
count_result[result[v-1]]=1
for i in range(v-1,-1,-1):
    point = result[i]
    for j, cnt in count[point]:
        count_result[j]+=cnt*count_result[point]


# 재귀적인 방법(DP아님) X
def count_basic(n):
    for i,cnt in count[n]:
        if i in basic:
            count_result[i]+=cnt
        else:
            for _ in range(cnt):
                count_basic(i)


for i in range(1,v+1):
    # count가 없으면 기본부품임
    if len(count[i])==0:
        print(i,count_result[i])

# 기본부품인지 체크없이 출력 -> 왜 이게 더 오래 걸리지?
# for i in range(1, len(basic)+1):
#     print(basic[i-1],count_result[basic[i-1]])



# 기본 부품이 1부터 시작하는게 아님
#count_basic(v) --> 왜 오류나는지 다시 확인(IndexError)