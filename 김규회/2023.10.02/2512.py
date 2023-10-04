# 2512
# https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())

start,end = 0, max(array)


while start <= end:
    mid = (start+end)//2
    cnt = 0
    
    for i in array:
        if i > mid:
            cnt += mid
        else:
            cnt += i
    
    if cnt <= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)