# 11000py
# https://www.acmicpc.net/problem/11000

import sys
import heapq
input = sys.stdin.readline

n = int(input())

time = [[0]*2 for _ in range(n)]

for i in range(n):
    start,end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

time.sort()

room = []
heapq.heappush(room, time[0][1])

for i in range(1, n):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])
        
print(len(room))