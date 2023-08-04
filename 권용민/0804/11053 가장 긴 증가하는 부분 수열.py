n = int(input())
sequence = list(map(int, input().split()))
# 이차원 배열: col원소에서 이어질 때 증가부분수열의 최대 길이
arr = [[0 for col in range(n)] for row in range(n)]

# 지금 고려중인 i번째 원소
for i in range(n):
    # i번째 원소의 직전에 왔을 원소 (처음부터 i번째 원소 까지)
    for j in range(i+1):
        # 자기 자신으로부터 증가부분수열 시작
        if i == j:
            arr[i][j] = 1
        # 선택된 직전원소보다 감소함 (증가부분수열 아님)
        elif sequence[j] > sequence[i]:
            continue
        # 선택된 직전원소와 값이 같음 (증가부분수열임, but 길이증가x)
        elif sequence[j] == sequence[i]:
            arr[i][j] = max(arr[j])
        # 선택된 직전원소보다 값이 큼 (증가부분수열, 길이 증가)
        else:
            arr[i][j] = max(arr[j]) + 1

print(max(map(max, arr)))