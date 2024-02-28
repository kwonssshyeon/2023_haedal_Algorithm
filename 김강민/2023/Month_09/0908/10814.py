import sys
input = sys.stdin.readline

N = int(input())

member = []
for _ in range(N):
    age, name = input().split()
    member.append([int(age), name])

s_member = sorted(member, key = lambda x:x[0])
for age, name in s_member:
    print(age, name)