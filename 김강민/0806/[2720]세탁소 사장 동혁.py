import sys

T = int(sys.stdin.readline())

penny = [25, 10, 5, 1]
money = []
for i in range(T):
    money.append(int(sys.stdin.readline()))
    for j in penny:
        print(money[i] // j, end=" ")
        money[i] %= j
    
    print()
