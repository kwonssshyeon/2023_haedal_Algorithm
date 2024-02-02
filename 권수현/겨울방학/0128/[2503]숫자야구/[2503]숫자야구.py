# 18:17 ~
import sys
input = sys.stdin.readline

n = int(input())
items = []
for _ in range(n):
    items.append(list(map(int,input().split())))
answer=[]

for num in range(100,1000):
    for i in range(n):
        strike,ball=0,0
        is_answer=True
        for idx in range(3):
            if str(num)[idx]==str(items[i][0])[idx]:
                strike+=1
            elif str(num)[idx] in str(items[i][0]):
                ball+=1
        if items[i][1]!=strike or items[i][2]!=ball:
            is_answer=False
            break
    
    if is_answer and len(set(str(num)))==3 and '0' not in set(str(num)):
        answer.append(num)

print(len(answer))
    


# 스트라이크 크고 -> 볼 작은 순으로 정렬
