import sys
from collections import defaultdict
input = sys.stdin.readline
word = input().strip()
word_dict = defaultdict(int)
word_set = set(word)

for char in word:
    word_dict[char] += 1

n = int(input())
book = []
for _ in range(n):
    a, b = map(str,input().split())
    book.append((int(a), b))
used = defaultdict(int)
ans = float('inf')

def dfs(pos, res):
    global ans
    if res > ans:
        return
    if pos == n:
        valid = True
        for char in word_set:
            if word_dict[char] > used[char]:
                valid = False
                break
        if valid:
            ans = min(ans, res)
            return
    else:
        for char in book[pos][1]:
            if char in word_set:
                used[char] += 1
        dfs(pos+1, res+book[pos][0])
        for char in book[pos][1]:
            if char in word_set:
                used[char] -= 1
        dfs(pos+1, res)

dfs(0,0)
if ans == float('inf'):
    print(-1)
else:
    print(ans)