import sys
input = sys.stdin.readline

N = int(input())

stk = []
for i in range(N):
    command = list(input().split())

    # push
    if command[0] == "push":
        # stk.insert(0, int(command[1]))
        stk.append(command[1])
    
    # pop
    elif command[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    
    # size
    elif command[0] == "size":
        print(len(stk))
    
    # empty
    elif command[0] == "empty":
        print(1 if len(stk) == 0 else 0)
    
    # top
    elif command[0] == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])