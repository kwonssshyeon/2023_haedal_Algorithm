import sys
input=sys.stdin.readline

t = int(input())
result=[]
for _ in range(t):
    string = input().strip()
    answer=0
    left,right=0,len(string)-1
    while left<right:
        if string[left]==string[right]:
            left+=1
            right-=1
        else:
            if right-left==1:
                answer=1
            dist=(right-left)//2
            if string[left:left+dist]==string[right-dist:right][::-1]:
                answer=1
            elif string[left+1:left+1+dist]==string[right-dist+1:right+1][::-1]:
                answer=1
            else:
                answer=2
            break

        

    result.append(answer)

for i in range(t):
    print(result[i])