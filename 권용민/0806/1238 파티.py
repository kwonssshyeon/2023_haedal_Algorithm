import  sys

n, m, x = map(int, sys.stdin.readline().split())
arr = [[sys.maxsize for col in range(n+1)] for row in range(n+1)]
for i in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    arr[s][e] = t
totalTime = [0 for _ in range(n+1)]

# 다익스트라 알고리즘
# x에서 각 노드까지 최단거리 구하기
selected = [False for _ in range(n + 1)]
selected[x] = True
for _ in range(n):
    minTime = sys.maxsize
    minIdx = 0
    # 선택할 minIdx 찾기
    for j in range(1, n+1):
        if selected[j]:
            continue
        if minTime > arr[x][j]:
            minTime = arr[x][j]
            minIdx = j

    # 최단거리 노드 선택 후, 아직 선택x 노드들 거리 업데이트
    selected[minIdx] = True
    for j in range(1, n+1):
        if selected[j]:
            continue
        arr[x][j] = min(arr[x][j], arr[x][minIdx] + arr[minIdx][j])

# x에서 각 노드까지 최단거리 합산
for j in range(1, n+1):
    if arr[x][j] != sys.maxsize:
        totalTime[j] += arr[x][j]


# 다익스트라 알고리즘
# 각 노드에서 x까지 최단거리 구하기 (arr 뒤집어서 구하기)
selected = [False for _ in range(n + 1)]
selected[x] = True
for _ in range(n):
    minTime = sys.maxsize
    minIdx = 0
    # 선택할 minIdx 찾기
    for i in range(1, n+1):
        if selected[i]:
            continue
        if minTime > arr[i][x]:
            minTime = arr[i][x]
            minIdx = i

    # 최단거리 노드 선택 후, 아직 선택x 노드들 거리 업데이트
    selected[minIdx] = True
    for i in range(1, n+1):
        if selected[i]:
            continue
        arr[i][x] = min(arr[i][x], arr[i][minIdx] + arr[minIdx][x])
# 각 노드에서 x까지 최단거리 합산
for i in range(1, n+1):
    if arr[i][x] != sys.maxsize:
        totalTime[i] += arr[i][x]


# 최장거리 출력
print(max(totalTime))
