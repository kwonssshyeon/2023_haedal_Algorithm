import sys
input = sys.stdin.readline

h, w = map(int,input().split())
blocks = list(map(int,input().split()))


stack = [0]
height = blocks[0]
sum=0
for i in range(1,len(blocks)):
    height=blocks[i]

    while stack and height>=blocks[stack[-1]]:
        point = stack.pop()
        
        if len(stack)==0:
            break

        distance = i-stack[-1]-1
        depth = min(height, blocks[stack[-1]]) - blocks[point]

        sum += distance * depth

    stack.append(i)


print(sum)
