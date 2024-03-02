import sys
input = sys.stdin.readline

n = int(input())
meetings=[]
for _ in range(n):
    meetings.append(tuple(map(int,input().split())))
meetings.sort(key=lambda x:(x[1],x[0]))

answer=1
prev=meetings[0][1]
for start,end in meetings[1:]:
    if start>=prev:
        answer+=1
        prev=end

print(answer)