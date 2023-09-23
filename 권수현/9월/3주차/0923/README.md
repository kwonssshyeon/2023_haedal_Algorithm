### 1차 시도
```python
import sys
input = sys.stdin.readline

height, width = map(int,input().split())
blocks = list(map(int,input().split()))

point = 0
end = 0
sum = 0
for i in range(width):
    if blocks[i]!=0:
        point = i
        break

while True:
    start = blocks[point]
    k = point+1
    while end < start and point < width-1:
        point+=1
        end = blocks[point]

    pivot = min(start,end)

    for i in range(k,point):
        sum+=(pivot-blocks[i])

    if point+1 >= width:
        break

    if blocks[point] < blocks[point+1]:
        point = point+1


print(sum)
```

현재위치 기준으로 다음점(현재랑 같거나 높으면 물이 고임) 찾고, 그다음 블록으로 옮겨서 같은 작업 반복

&rarr; 시간초과
<br>
<br>
<br>


### 2차 시도
```python
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
            if isPossible:         # 2. 오른쪽이 막혀있음 -> 증가시킨 point를 더함 
                result[i]+=point
            isPossible = True      # 1. 왼쪽이 막혀있음 -> 다시 여기에 왔다면 3. 새로운 왼쪽이 막혀있음
            point = 0

        else:
            if isPossible:         # 왼쪽이 막혀있고 현재위치에 블록이 없을때(물이 고이는 자리)
                point+=1

                
print(sum(result))
```
위에는 왼쪽에서 오른쪽으로 블록을 찾아가며 sum을 더했던 반면, 아래에서 위로 sum을 구할 수 있겠다고 생각했다.

그 경우에는 양쪽이 막혀있는지, 뚫려있는지를 생각해보면 된다.(정확히는 왼쪽, 오른쪽으로는 옮겨가며 계산할꺼라서)

그걸 check하기 위해 isPossible 변수를 뒀다.

isPossible 순서를 생각하는데 시간이 쫌 걸릿다..



### 추가
```python
import sys
input = sys.stdin.readline
H, W = map(int,input().split())
block = list(map(int,input().split()))
answer = 0
 
for i in range(1, W-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)

    if m > block[i]:
        answer += m - block[i]
 
print(answer)
```

거의 이런식으로 풀었던데 몰러.. 나중에 디버깅해봐야지