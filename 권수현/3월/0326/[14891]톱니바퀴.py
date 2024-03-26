import sys
input = sys.stdin.readline

wheels = [0]

def rotate(wheel,op):
    if op==-1:
        temp = wheel[0]
        wheel = wheel[1:]+[temp]
    else:
        temp = wheel[-1]
        wheel = [temp]+wheel[:-1]
    return wheel

for _ in range(4):
    wheels.append(list(map(int,input().strip())))

t = int(input())

for _ in range(t):
    idx,op = map(int,input().split())
    init_op = op
    
    prev = wheels[idx][2]
    for i in range(idx+1,5):
        if prev!=wheels[i][6]:
            prev = wheels[i][2]
            wheels[i] = rotate(wheels[i],op*(-1))
            op = op*(-1)
        else:
            break
    
    op = init_op
    prev = wheels[idx][6]
    for i in range(idx-1,0,-1):
        if prev!=wheels[i][2]:
            prev = wheels[i][6]
            wheels[i] = rotate(wheels[i],op*(-1))
            op = op*(-1)
        else:
            break
        
    wheels[idx] = rotate(wheels[idx],init_op)


answer=0
for i in range(1,5):
    if wheels[i][0]==1:
        answer+=2**(i-1)

print(answer)
    
        