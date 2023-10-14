import sys
input = sys.stdin.readline


n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]
arr = []
result = 100000000


def dfs(depth, start):
    global result
    # 기저
    if depth == length:
        sour = 1 
        bitter = 0
        for i in arr:
            sour *= i[0] 
            bitter += i[1] 
        if abs(bitter - sour) < result:
            result = abs(bitter - sour) 
        return  

    for i in range(start, n):
        arr.append(taste[i])
        dfs(depth + 1, i + 1)
        arr.pop()




for i in range(1, n + 1): 
    length=i
    dfs(0, 0)

print(result)


# 쉬운거 풀었움..바빴어유2...