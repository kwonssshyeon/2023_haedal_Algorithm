import sys
input = sys.stdin.readline

n,m = map(int,input().split())

times = []
for i in range(n):
    times.append(int(input()))

left = min(times)
right = max(times) * m

result = right

while left <= right:
    mid = (left+right)//2   # 모든 사람이 입국심사에 걸리는 시간
    cnt = 0
    
    for time in times:
        cnt += (mid//time)    # 시간 내 검사받을 수 있는 사람 수

    if cnt >= m:
        right = mid-1
        result = min(result, mid)


    else:
        left = mid+1

    

print(result)





# 알고리즘 분류를 봐버렸다...