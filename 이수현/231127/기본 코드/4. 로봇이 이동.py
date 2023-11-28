def solution(moves):
    x = y = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ["G","R","L"]

    #R default
    m = 1
    for move in moves:
        if move == "G":
            x += dx[m]
            y += dy[m]
        elif move == "R":
            m = (m+1)%4
        elif move == "L":
            m = (m - 1) % 4 # 여기 주의하기
    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
