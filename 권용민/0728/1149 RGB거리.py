n = int(input())

arr = [[0 for col in range(3)] for row in range(n+1)]
for house in range(1, n+1):
    r, g, b = map(int, input().split())
    costs = [r,g,b]
    costIndex = 0
    for color in range(3):
        cost = costs[costIndex]
        arr[house][color] = min(arr[house-1][color-1] + cost, arr[house-1][(color+1) % 3] + cost)
        costIndex += 1

print(min(arr[n][0], arr[n][1], arr[n][2]))
'''
마지막에 r을 골랐을 때 그전까지 최소는?
행은 현재 고려중인 집,
열은 r, g, b
각 셀은 현재 선택중인 집에 선택한 색을 칠했을 때 최소비용 
'''
