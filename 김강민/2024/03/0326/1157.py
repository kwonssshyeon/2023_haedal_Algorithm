import sys
input = sys.stdin.readline

cnt = []

alphabet = input().strip().upper()
alphabet_list = list(set(alphabet))

for s in alphabet_list:
    count = alphabet.count(s)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(alphabet_list[cnt.index(max(cnt))])