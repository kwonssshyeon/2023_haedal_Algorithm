# [20920 영단어 암기는 괴로워](https://www.acmicpc.net/problem/20920)  

import sys
from collections import Counter

input = sys.stdin.readline

word_list = []
word_count = Counter()
printed = set()

n, m = map(int, input().split())
for _ in range(n):
    str = input().strip()
    if (len(str) >= m):
        word_list.append(str) # 길이가 m 이상인 단어만 저장
        word_count[str] += 1

# print(word_list)

sorted_word_list = sorted(word_list, key = lambda x: (-word_count[x], -len(x), x))

for w in sorted_word_list:
    if w not in printed:
        print(w)
        printed.add(w) # 한 단어는 한 번만 출력
