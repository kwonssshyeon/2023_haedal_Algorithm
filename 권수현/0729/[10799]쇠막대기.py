import sys
input = sys.stdin.readline

bars = list(input().strip())
#print(bars)

cnt = 0
stack = []
previous=''

for bar in bars:
    if bar == "(":
        stack.append(bar)

    elif bar == ")":
        stack.pop()
        
        if previous == "(":
            cnt+=len(stack)
        elif previous == ")":
            cnt+=1

    previous = bar

print(cnt)