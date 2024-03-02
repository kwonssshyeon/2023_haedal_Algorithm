import sys
import heapq
input = sys.stdin.readline

n = int(input())
meetings=[]
for _ in range(n):
    meetings.append(tuple(map(int,input().split())))
meetings.sort(key=lambda x:(x[0],x[1]))

answer=1
result=[]
prev=meetings[0][1]
heapq.heappush(result,prev)
for start,end in meetings[1:]:
    prev = heapq.heappop(result)
    if prev<=start:
        heapq.heappush(result,end)
    else:
        answer+=1
        heapq.heappush(result,prev)
        heapq.heappush(result,end)

print(answer)