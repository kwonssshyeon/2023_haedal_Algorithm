import sys
input = sys.stdin.readline

n = input().rstrip()

n_list = list(input().split())

m = input().rstrip()

m_list = list(input().split())

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)

