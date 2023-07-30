```
# 오류코드
import sys
input = sys.stdin.readline

input_list = list(input().strip())
index = []
stack = []
case = []
final = []

for i in range(input_list):
    if input_list[i]=="(":
        stack.append("(")
        index[i] = len(stack)

    elif input_list[i] == ")":
        index[i] = len(stack)
        stack.pop()


def findAllCase(index,n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(index)): 
        kkk = index[i] 
        ddd = index[i + 1:] 
        for C in findAllCase(ddd, n-1): 
            result.append([kkk]+C) 
              
    return result



n = len(index)
for i in range(n):
    case = findAllCase(index,i)
    for i in case:
        copy_input = input_list[:]
        for a,b in i:
            copy_input[a] = "("
            copy_input[b] = ")"
        final.add("".join(copy_input))

print(*sorted(final),sep='\n') 
```

- 괄호가 닫힌 이후에 다시 여는 경우가 반례
- final 리스트로 하면 중복 문자열 생김
