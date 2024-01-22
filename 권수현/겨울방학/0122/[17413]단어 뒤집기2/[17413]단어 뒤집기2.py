# 1:11 ~ 1:36

# 뛰어쓰기를 만나면  result에 추가 / 태그안 내용은 무조건 그대로 들어감

import sys
from collections import deque
input = sys.stdin.readline

words = input()
back = True
string = deque()
result = ''
for i in range(len(words)):

    if words[i]==" " or i==len(words)-1:
        if back==True:
            while string:
                result+=string.pop()
        elif back==False:
            while string:
                result+=string.popleft()
        result+=' '

    else:
        
        if words[i]=="<":
            while string:
                result+=string.pop()
            back=False
            string.append(words[i])
        
        elif words[i]==">":
            string.append(words[i])
            while string:
                    result+=string.popleft()
            back=True

        else:
            string.append(words[i])

print(result)