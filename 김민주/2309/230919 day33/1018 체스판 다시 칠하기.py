count = float('inf') # 다시 칠해야 하는 최소 칸 수 - 무한대

n, m = map(int, input().split())

board = [[None for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == "B": color = True
        else: color = False

        board[i][j] = color # 입력된 색깔 일단 저장

# 8x8 사이즈의 부분 보드로 나누어서 체크
# 현재 위치의 색깔을 정답과 비교 - 틀리면 바꿔야 함
for i in range(n - 7): 
    for j in range(m - 7): 
        change_count = 0 # 현재 부분 보드에서 다시 칠해야 하는 칸의 수
        
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y - i - j) % 2 == 0: # 현재 위치 (x, y)가 짝수 행과 짝수 열에 속하는 경우
                    if board[x][y] == True:
                        change_count += 1
                else: # 현재 위치 (x, y)가 홀수 행 또는 홀수 열에 속하는 경우
                    if board[x][y] == False:
                        change_count += 1

        # 현재 부분 보드에서 변경한 횟수와 최소 칸 수 비교
        count = min(count, change_count, 8*8 - change_count)

'''
for i in range(n):
    for j in range(m):
        print(f"{str(board[i][j]):<6s}", end="")
    print()
'''
print(count)
