import sys
import heapq
input = sys.stdin.readline

answer=0
n,c = map(int,input().split())
m = int(input())
delivers = [[]for _ in range(n+1)]
for _ in range(m):
    start,end,count = map(int,input().split())
    heapq.heappush(delivers[start],(end,count))

bus = []
total=0
for start in range(1,n+1):
    while bus:
        fin = heapq.heappop(bus)
        if fin[0]==start:
            total-=fin[1]
            answer+=fin[1]
        else:
            heapq.heappush(bus,fin)
            break
        
    for next,boxes in delivers[start]:
        if total+boxes<=c:
            total+=boxes
            heapq.heappush(bus,(next,boxes))
        elif total<c:
            heapq.heappush(bus,(next,c-total))
            total=c


print(answer)


# 빨리 내리는 걸 먼저 담아야함 -> 빨리 싣는걸 먼저해서 틀림