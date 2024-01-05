def solution(n, lost, reserve):
    answer = 0
    add = 0

    lost.sort()
    reserve.sort()

    new_lost = []
    new_reserve = []

    for i in lost:
        print(i)
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)

    print(lost)
    print(reserve)

    for i in new_lost:
        if i - 1 in reserve:
            add += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            add += 1
            reserve.remove(i + 1)

    answer = n - len(new_lost) + add
    return answer
