import sys
input = sys.stdin.readline
n = int(input())
s = int(n**(1/2))

arr = [0]*(n+1)
for i in range(1,s+1):
    arr[i**2]=1

answer=4
for i in range(s, 0, -1):
    if arr[n]:
        answer=1
        break
    elif arr[n-(i**2)]:
        answer=2
        break
    else:
        for j in range(int((n-i**2)**(1/2)), 0, -1):
            if arr[(n-i**2)-j**2]: 
                answer=3
print(answer)
