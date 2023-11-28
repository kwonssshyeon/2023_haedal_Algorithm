def solution(moves):
    x = y = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dir = ["U","R","D","L"]
    for move in moves:
        for k in range(4):
            if move == dir[k]:
                x += dx[k]
                y += dy[k]

    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
