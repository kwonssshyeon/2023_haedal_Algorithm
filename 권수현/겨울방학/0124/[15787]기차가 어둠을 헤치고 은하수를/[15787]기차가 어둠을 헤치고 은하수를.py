# 15:11 ~ 14:07(시도 겁나 여러번../튜플은 순서가 있다 !!, 같은 원소 중복을 피하기 위해 set)

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
orders = []
dic = {i+1:set() for i in range(n)}
for _ in range(m):
    orders.append(list(map(int,input().split())))

for order in orders:
    if order[0]==1:
        dic[order[1]].add(order[2])
    elif order[0]==2:
        if order[2] in dic[order[1]]:
            dic[order[1]].discard(order[2])
    elif order[0]==3:
        dic[order[1]] = {i+1 for i in dic[order[1]] if i<20}
    elif order[0]==4:
        dic[order[1]]= {i-1 for i in dic[order[1]] if i>1}



answer = set()
for train in dic.values():
    answer.add(tuple(sorted(train)))


print(len(answer))