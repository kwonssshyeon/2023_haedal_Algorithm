# https://www.acmicpc.net/problem/1181 단어 정렬 (문자열)

n = int(input())

words = set() # 중복 방지 조건
for _ in range(n):
  words.add(input())

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
  print(word)
