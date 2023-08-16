import sys
input = sys.stdin.readline

N = int(input())

bag = 0

while N >= 0:
    if N % 5 == 0:
        bag += int(N // 5)
        print(bag)
        break
    N -= 3
    bag += 1

else:
    print(-1)