import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    tmp = list(map(int, input().strip()))
    arr.append(tmp)

visited = [[[0] * 2 for col in range(m)] for row in range(n)]

# right, down, left, up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append([0, 0, 0])

visited[0][0][0]= 1
x = 0
y = 0
w = 0
while q:
    x, y, w = q.popleft()
    if x == n-1 and y == m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 밖
        if not 0 <= nx < n or not 0 <= ny < m:
            continue

        # 이동가능 and 아직방문x
        if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
            visited[nx][ny][w] = visited[x][y][w] + 1
            q.append([nx, ny, w])
        # 벽인데 아직 안부숨
        elif arr[nx][ny] == 1 and w == 0:
            visited[nx][ny][1] = visited[x][y][w] + 1
            q.append([nx, ny, 1])

if x == n-1 and y == m-1:
    print(visited[x][y][w])
else:
    print(-1)
