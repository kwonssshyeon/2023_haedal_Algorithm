import sys
input = sys.stdin.readline

N = int(input())
words = []

for _ in range(N):
    words.append(input().strip())

set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key = len)

for i in words:
    print(i)