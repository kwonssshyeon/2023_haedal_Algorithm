import sys
input = sys.stdin.readline

height, width = map(int,input().split())
blocks = list(map(int,input().split()))


result = [0 for _ in range(height)]
for i in range(height):
    isPossible = False
    point = -1

    for j in range(width):

        if blocks[j]>i:
            if isPossible:
                result[i]+=point
            isPossible = True
            point = 0

        else:
            if isPossible:
                point+=1

                
print(sum(result))