import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
items = []
counts = []
for _ in range(n):
    item,strike,ball = map(int,input().split())
    items.append(item)
    counts.append((strike,ball))

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

answer=0
for num in list(permutations(data, 3)):
    is_answer=True
    for item,count in zip(items,counts):
        item = tuple(str(item))
        strike=ball=0
        for idx in range(3):
            if num[idx]==item[idx]:
                strike+=1
            elif num[idx] in item:
                ball+=1
        if count[0]!=strike or count[1]!=ball:
            is_answer=False
            break
    
    if is_answer:
        answer+=1

print(answer)
