import sys
input = sys.stdin.readline


n,c = map(int,input().split())
m = int(input())
delivers = []
for _ in range(m):
    delivers.append(tuple(map(int,input().split())))
delivers.sort(key=lambda x:x[1])

amounts=[0]*(n+1)
answer=0
for start,end,cost in delivers:
    fin=cost
    for i in range(start,end):
        if amounts[i]+fin>=c:
            fin=c-amounts[i]

    for i in range(start,end):
        amounts[i]+=fin

    answer+=fin

print(amounts)
print(answer)

# 내리는걸 먼저하기 때문에 end에 cost를 더하지 않으면 빼는 과정을 생략할 수 있음