n = int(input())
li = list(map(int, input().split()))
x = int(input())
count = 0

while li:
    tmp = li.pop(0)
    if x - tmp in li:
        count += 1

print(count)

'''
a + b = x 인 쌍 구하는 문제
x - a 가 list에 남아있는지 확인
'''
