import sys
input = sys.stdin.readline

zero = [1,0,1]
one = [0,1,1]
result = []

def func(num):
    length = len(zero)
    if num>=length:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    result.append([zero[num],one[num]])



n = int(input())
for i in range(n):
    num = int(input())
    func(num)

for i in range(n):
    print(result[i][0], result[i][1])


# 쉬운거 풀었움..바빴어유...