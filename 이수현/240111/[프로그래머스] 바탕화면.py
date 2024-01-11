def solution(wallpaper):
    answer = []
    wallpapers = []
    lux, luy, rdx, rdy = 51, 51, 0, 0
    for str in wallpaper:
        wallpapers.append(list(str))

    # 맨 위, 맨 아래
    # 맨 왼쪽, 맨 오른쪽

    for i in range(len(wallpapers)):
        for j in range(len(wallpapers[0])):
            print(wallpapers[i][j], end="")
            if wallpapers[i][j] == "#":
                if luy > j:  # y가 더 작아 높이있다.
                    luy = j
                if lux > i:  # 가장 왼쪽
                    lux = i
                if rdy < j + 1:  # 가장 아래쪽
                    rdy = j + 1
                if rdx < i + 1:  # 가장 오른쪽
                    rdx = i + 1
    answer = [lux, luy, rdx, rdy]
    return answer
