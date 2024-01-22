# 15:32 ~ 4:22(시도 2회 / 중간에 result에 포함될 수 없는 경우가 생기면 바로 -1 끝내야함)

import sys
from collections import defaultdict
input = sys.stdin.readline

val=input().strip()
result = []
sound = ['q','u','a','c','k']


for c in val:
    fail=True
    flag=0
    
    if c=='q' and len(result)==0:
        result.append(c)
        fail=False
    else:
        for i in range(len(result)):
            if len(result[i])==5:
                if c == 'q':
                    result[i]=c
                    flag=1
                    fail=False
                    break
            elif c == sound[len(result[i])]:
                result[i] = result[i]+c
                fail=False
                break
        if c=='q' and flag==0:
            result.append(c)
            fail=False
        
        if fail==True:
            result.append(".")

answer = len(result)
for r in result:
    if len(r)!=5:
        answer = -1
print(answer)


                
    


# temp문자열의 길이에 따라 알파벳 매핑
