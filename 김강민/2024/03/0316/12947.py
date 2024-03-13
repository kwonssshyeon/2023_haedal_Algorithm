def solution(x):
    num = str(x)
    num_sum = 0
    for i in num:
        num_sum += int(i)
    if x % num_sum == 0:
        return True
    else:
        return False
