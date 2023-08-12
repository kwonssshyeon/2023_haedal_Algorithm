n, m = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
while low <= high:
    # mid: 자를 높이
    mid = (low+high) // 2
    acquiredTree = 0
    for tree in trees:
        acquiredTree += max(tree - mid, 0)

    # 원하는 것 보다 많이 잘랐으면 -> 절단높이 높이기
    if acquiredTree > m:
        low = mid + 1
        result = mid
    # 원하는 것 보다 적게 잘랐으면 -> 절단높이 낮추기
    elif acquiredTree < m:
        high = mid - 1
    # 정확히 원하는 만큼 잘랐으면 -> break
    else:
        result = mid
        break

print(result)