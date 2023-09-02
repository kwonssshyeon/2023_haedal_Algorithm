import sys
input = sys.stdin.readline

s = list(map(str,input().strip()))
t = list(map(str,input().strip()))

def compare(s,t):
    if s == t:
        return 1
    if len(t) == 0:
        return 0
    
    result = 0
    if t[-1]=="A":
        result = compare(s,t[:-1])
        
    if result == 1:
        return result
    
    if t[0]=="B":
        t = t[1:]
        t.reverse()
        result = compare(s,t)

    return result


print(compare(s,t))



# 재귀 어렵다...