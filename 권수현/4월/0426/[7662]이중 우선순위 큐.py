# 9:00 ~ 9:50
# remove 이용해서 원소제거하고 다시 heapify 하는거랑 비슷하지 않나..?

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    minQ = []
    maxQ = []
    n = int(input())
    visited = [False for _ in range(1000001)]
    for i in range(n):
        op,num = map(str,input().split())
        
        if op=="I":
            visited[i]=True
            heapq.heappush(maxQ,(int(num)*(-1),i))
            heapq.heappush(minQ,(int(num),i))
        
        elif num=="1":
            while maxQ and not visited[maxQ[0][1]]:
                heapq.heappop(maxQ)
            if maxQ:
                visited[heapq.heappop(maxQ)[1]]=False
        
        elif num=="-1":
            while minQ and not visited[minQ[0][1]]:
                heapq.heappop(minQ)
            if minQ:
                visited[heapq.heappop(minQ)[1]]=False
    
    
    while maxQ and not visited[maxQ[0][1]]:
                heapq.heappop(maxQ)
    while minQ and not visited[minQ[0][1]]:
                heapq.heappop(minQ)

    if maxQ and minQ:
        print(maxQ[0][0]*(-1),minQ[0][0])
    else:
        print("EMPTY")
                    
  
