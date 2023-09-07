import sys

n = int(sys.stdin.readline())
sum = 0

for i in range(n):
    opt = sys.stdin.readline().split()
    if len(opt) == 2:
        num = int(opt[1])
    opt = opt[0]

    if opt == 'add':
        sum |= 1 << (num-1)
    elif opt == 'remove':
        sum &= ~(1 << (num-1))
    elif opt == 'check':
        if sum & 1 << (num-1):
            print(1)
        else:
            print(0)
    elif opt == 'toggle':
        if sum & 1 << (num-1):
            sum &= ~(1 << (num-1))
        else:
            sum |= 1 << (num-1)
    elif opt == 'all':
        sum = 0b11111111111111111111
    else:
        sum = 0

'''
true false 역할하는 비트 20개짜리 정수 이용(비트마스킹)
'''