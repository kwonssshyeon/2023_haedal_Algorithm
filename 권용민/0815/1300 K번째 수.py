n = int(input())
k = int(input())

s = 1
e = n*n
mid = (s+e)//2
while s < e:
    below_count = 0
    for i in range(1, n+1):
        below_count += min(mid//i, n)

    if below_count >= k:
            e = mid
    else:
        s = mid + 1
    mid = (s+e)//2


print(mid)

'''
x보다 작거나 같은 값이 k-1개인 x 찾기  

각 행에서 x보다 작은거나 같은 수의 개수: x//i 
'''