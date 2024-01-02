import sys
input = sys.stdin.readline

height, width = map(int,input().split())
blocks = list(map(int,input().split()))


left, right = 0, width-1
left_max, right_max = blocks[left], blocks[right]
sum=0

while left<right:
    if blocks[left]<=blocks[right]:
        left+=1
        left_max = max(left_max,blocks[left])
        if left_max>blocks[left]:
            sum+=(left_max-blocks[left])
    else:
        right-=1
        right_max = max(right_max,blocks[right])
        if right_max>blocks[right]:
            sum+=(right_max-blocks[right])


print(sum)