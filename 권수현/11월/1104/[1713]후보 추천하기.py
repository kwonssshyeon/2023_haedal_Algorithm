import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

people = list(map(int,input().split()))

candidate = []
count = []

for i in range(m):
    person = people[i]
    flag=0

    #0.후보에 존재하는 경우
    for j in range(len(candidate)):
        if candidate[j]==person:
            count[j] += 1
            flag=1
            break
    
    if flag==0:
        # 후보에 자리가 없는 경우
        if len(candidate)>=n:
            mini = min(count)
            idx = count.index(mini)
            count.pop(idx)
            candidate.pop(idx)
        candidate.append(person)
        count.append(1)
 

candidate = sorted(candidate)
print(*candidate)
