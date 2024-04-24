import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
temp = [i for i in range(1, 9)]

if num == temp:
    print("ascending")
elif num == temp[::-1]:
    print("descending")
else:
    print("mixed")
