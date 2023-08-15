import sys
input = sys.stdin.readline


n = int(input())

for i in range(n):  
    floor = int(input())
    num = int(input())
    bottom = [x for x in range(1, num+1)]
    
    for j in range(floor):
        for k in range(1, num):
            bottom[k] += bottom[k-1] 
    print(bottom[-1]) 