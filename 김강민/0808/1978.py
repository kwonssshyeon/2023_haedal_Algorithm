import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
cnt = 0

for x in num:
    for i in range(2, x + 1):
        if x % i == 0:
            if x == i:
                cnt += 1
            
            break

print(cnt)