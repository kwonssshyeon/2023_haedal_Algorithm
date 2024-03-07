import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
m = int(input())
errors=set()
if m!=0:
    errors=set(map(int,input().split()))
buttons = sorted(list({0,1,2,3,4,5,6,7,8,9} - errors))

if n==100:
    print(0)
    sys.exit(0)

mini = abs(n-100)
for repeat in range(1,7):
    for idx in product(buttons,repeat=repeat):
        num=''
        for i in idx:
            num+=str(i)
        mini = min(mini,abs(int(num)-n)+repeat)

print(mini)
