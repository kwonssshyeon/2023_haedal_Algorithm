import sys

k, n = map(int, input().split())
arr = [0 for _ in range(k)]
for i in range(k):
    arr[i] = int(sys.stdin.readline())

low = 1
high = max(arr)
maxLen = 0
while low <= high:
    mid = (low+high)//2
    availCount = 0
    for i in arr:
        availCount += i // mid
    if availCount >= n:
        maxLen = mid
        low = mid + 1
    else:
        high = mid - 1

print(maxLen)