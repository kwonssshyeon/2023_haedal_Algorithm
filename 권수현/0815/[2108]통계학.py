import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

print(round(sum(arr)/n))
print(arr[n//2])


dic=dict()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
        
maximum=max(dic.values())
max_dic=[]

# 최빈값 여러개
for i in dic:
    if maximum==dic[i]:
        max_dic.append(i)

if len(max_dic)>1:
    print(max_dic[1])
else:
    print(max_dic[0])




print(max(arr)-min(arr))
