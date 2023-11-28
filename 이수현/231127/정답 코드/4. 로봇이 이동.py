def solution(moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = y = 0
    d = 1
    for c in moves:
        if c == 'G':
            x = x + dx[d]
            y = y + dy[d]
        elif c == 'R':
            d = (d + 1) % 4
        elif c == 'L':
            d = (d - 1) % 4

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
