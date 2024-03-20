import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    total=cnt=0
    data=[1,2,3]
    def dfs(start):
        global total,cnt
        
        if total==n:
            cnt+=1
            return
        elif total>n:
            return

        prev=0
        for i in range(start,3):
            if prev!=data[i]:
                total+=data[i]
                prev=data[i]
                dfs(i)
                total-=data[i]
                
    dfs(0)                                                                      
    
    print(cnt)