import sys
input = sys.stdin.readline

N = int(input())
que = []

for _ in range(N):
    command = list(input().split())
    
    # push
    if command[0] == "push":
        # que.insert(0, int(command[1]))
        que.append(command[1])
    
    # pop
    elif command[0] == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(0))
    
    # size
    elif command[0] == "size":
        print(len(que))
    
    # empty
    elif command[0] == "empty":
        print(1 if len(que) == 0 else 0)
    
    # front
    elif command[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    
    # back
    elif command[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
