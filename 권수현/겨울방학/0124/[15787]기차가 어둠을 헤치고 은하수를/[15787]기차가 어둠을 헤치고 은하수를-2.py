import sys
input = sys.stdin.readline

n,m = map(int,input().split())
orders = []
for _ in range(m):
    orders.append(list(map(int,input().split())))

trains = [0 for _ in range(n)]

for op in orders:
    if op[0]==1:
        train,person = op[1]-1, op[2]-1
        trains[train] = trains[train] | 1<<person
    elif op[0]==2:
        train,person = op[1]-1, op[2]-1
        trains[train] = trains[train] & ~(1<<person)
    elif op[0]==3:
        train = op[1]-1
        trains[train] = trains[train]<<1
        trains[train] = trains[train] & ~(1 << 20)
    elif op[0]==4:
        train = op[1]-1
        trains[train] = trains[train]>>1


print(len(set(trains)))