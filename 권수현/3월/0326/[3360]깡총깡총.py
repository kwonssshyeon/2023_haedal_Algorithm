import sys
input = sys.stdin.readline
N = int(input())

answer=0
while N>=0:
    answer+=1
    answer+=N//2
    N-=3

print(answer%1000000)