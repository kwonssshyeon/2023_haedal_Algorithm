import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split(" "))
x, y, d = map(int, input().rstrip().split(" "))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
for _ in range(n):
    room.append(list(map(int, input().split(" "))))

answer = 0
while True:
    if room[x][y] == 0:  # 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
        room[x][y] = 2
        answer += 1
    flag = False
    for k in range(4):  # 4방향 확인
        d = (d + 3) % 4  # 반시계 회전
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if room[nx][ny] == 0:  # 청소할 방이면 전진 # 1로 돌아감
                flag = True  # 청소할 방 발견
                x = nx
                y = ny
                break
    if flag == False:  # 후진하고 벽이 있으면 끝
        b = (d + 2) % 4
        nx = x + dx[b]
        ny = y + dy[b]
        if room[nx][ny] == 1:
            break  # 여기서 종료해야함
        else:
            x = nx
            y = ny

print(answer)
