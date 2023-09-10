n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
printed = [False for _ in range(n)]
ans = [0 for _ in range(m)]

def func(printedCount):
    if printedCount == m:
        for j in range(m):
            print(ans[j], end=" ")
        print()
        return
    
    for i in range(n):
        if printed[i] is False:
            ans[printedCount] = arr[i]
            printed[i] = True
            func(printedCount + 1)
            printed[i] = False



func(0)