import sys

n, c = map(int, input().split())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
result = 0

s = 1
e = arr[-1]
while s <= e:
    mid = (s + e) // 2
    preIndex = 0
    routerCount = 1 #시작점에 1개
    # 공유기 개수 체크
    for curIndex in range(1, n):
        if arr[curIndex] - arr[preIndex] >= mid:
            preIndex = curIndex
            routerCount += 1
    if routerCount >= c:
        result = mid
        s = mid + 1
    else:
        e = mid - 1

print(result)

'''
routerCount == c인 shortestLen을 이분탐색으로 찾기

shortestLen이 mid일 때 충족하면 (routerCount >= c) => res 저장 후 거리 늘리기 (shortestLen 늘리기)
routerCount > c이어도 shortestLen이 아닌데서 공유기 설치를 안하면 해당됨  
routerCount < c이면 => 거리 줄이기

'''
