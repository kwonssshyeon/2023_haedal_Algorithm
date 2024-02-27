import sys

n = int(sys.stdin.readline())
state = dict()

for _ in range(n):
    name, attendance = map(str, sys.stdin.readline().split())

    if attendance == "enter":
        state[name] = attendance
    else:
        del state[name]

state = sorted(state.keys(), reverse=True)

for i in state:
    print(i)