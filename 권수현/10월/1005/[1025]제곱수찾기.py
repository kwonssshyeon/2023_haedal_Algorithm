import sys
input = sys.stdin.readline

N,M = map(int, input().split())
table = []
for i in range(N):
    table.append(list(map(int,input().strip())))


def is_square(num):
    sqr_num = num**(1/2)
    if sqr_num==int(sqr_num):
        return True
    else:
        return False



ans = -1
for x in range(N):
    for y in range(M):
        for dx in range(-N,N):
            for dy in range(-M,M):
                
                if dx==0 and dy==0:
                    continue
                nx = x
                ny = y
                num = ''

                
                while 0<=nx<N and 0<=ny<M:
                    num += str(table[nx][ny])
                    if is_square(int(num)):
                        ans = max(ans,int(num))
                    
                    nx+=dx
                    ny+=dy

print(ans)
