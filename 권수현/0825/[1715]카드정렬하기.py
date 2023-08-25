import heapq
import sys
input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card,int(input()))

sum = 0
for i in range(1,n):
    now = heapq.heappop(card)
    now+=heapq.heappop(card)
    sum += now
    heapq.heappush(card,now)
    
print(sum)
    
