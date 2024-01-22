import sys
input = sys.stdin.readline

val=input().strip()
result = []
sound = ['q','u','a','c','k']

for c in val:
    if c=='q':
        flag_q=0
        for i in range(len(result)):
            if len(result[i])==5:
                result[i]=c
                flag_q=1
                break
        if flag_q==0:
            result.append(c)
    else:
        flag=0
        for i in range(len(result)):
            if len(result[i])==5:continue
            if c==sound[len(result[i])]:
                result[i]+=c
                flag=1
                break
        if flag==0:
            result.append(".")
            break

answer = len(result)
for r in result:
    if len(r)!=5:
        answer=-1
print(answer)

        


# q이면 길이 5인 문자열이 있다면 덮어쓰고 / 없다면 추가로 문자열 생성
# 나머지의 경우는 자신의 인덱스와 같은 길이의 문자열이 있다면 붙이고 / 없다면 실패(-1)
