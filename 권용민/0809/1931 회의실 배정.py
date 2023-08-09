import sys

n = int(sys.stdin.readline())
meetings = []
curTime = 0
meetingCount = 0
for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))

# 끝나는 시간으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 가능한거 나올때 까지 pop
while meetings :
    fastestEnd = meetings.pop(0)
    if fastestEnd[0] < curTime:
        continue
    curTime = fastestEnd[1]
    meetingCount += 1

print(meetingCount)
