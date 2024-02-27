import sys
input = sys.stdin.readline

N = int(input())

dance = {'ChongChong'}

for i in range(1, N+1):
    A, B = input().rstrip().split()

    if A in dance:
        dance.add(B)
    
    if B in dance:
        dance.add(A)
    
print(len(dance))