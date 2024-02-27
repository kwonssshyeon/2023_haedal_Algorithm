def solution(s):
    s_list = list(s)
    
    cnt_p = 0
    cnt_y = 0

    for i in s_list:
        if i == 'p' or i == 'P':
            cnt_p += 1
        if i == 'y' or i == 'Y':
            cnt_y += 1
    if cnt_p == cnt_y or (cnt_p == 0 and cnt_y == 0):
        answer = True
    elif cnt_p != cnt_y:
        answer = False
    return answer

s = "pPoooY"
print(solution(s))