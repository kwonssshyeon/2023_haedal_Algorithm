import sys
input = sys.stdin.readline

row,col,r = map(int,input().split())
arr=[]

for _ in range(row):
    arr.append(list(map(int,input().split())))

for _ in range(r):
    for i in range(min(row,col)//2):

        line1 = arr[i][1+i:col-i]
        line2 = [arr[j][col-1-i] for j in range(1+i,row-i)]
        line3 = arr[row-1-i][i:col-i-1]
        line4 = [arr[j][i] for j in range(i,row-1-i)]


        arr[i][i:col-i-1]=line1

        for j in range(i,row-i-1):
            arr[j][col-1-i] = line2[j-i]
        
        for j in range(1+i,row-i):
            arr[j][i]=line4[j-i-1]
        
        arr[row-1-i][1+i:col-i]=line3
       


for i in range(row):
    print(*arr[i])