import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


# 이렇게 하니까 시간초과남...
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            sum += arr[i][j]

    print(sum)


# 단순하게 누적합으로 풀면 안됨
# dp를 이용


# 일단 여기까지...이따 코드 수정해야지
