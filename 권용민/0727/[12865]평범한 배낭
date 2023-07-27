n, totalWeight = input().split()
n = int(n)
totalWeight = int(totalWeight)
weights = []
values = []
for i in range(n):
    w, v = input().split()
    w = int(w)
    v = int(v)
    weights.append(w)
    values.append(v)

arr = [[0 for col in range(totalWeight+1)] for row in range(n+1)]
for i in range(1, n+1):
    for j in range(1, totalWeight+1):
        if j - weights[i-1] >= 0:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j - weights[i-1]] + values[i-1], arr[i-1][j])
        else:
            arr[i][j] = arr[i-1][j]

print(arr[-1][-1])
