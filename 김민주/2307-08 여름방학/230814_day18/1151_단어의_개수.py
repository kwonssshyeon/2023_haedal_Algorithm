# https://www.acmicpc.net/problem/1152 단어의 개수 (문자열)

words = list(input().split())
'''
# 똑같은 코드 늘린 거
words = []
for word in input().split():
    words.append(word)
'''

print(len(words))


# 공백을 받을 때마다 += 1 해도 되지 않을까?
