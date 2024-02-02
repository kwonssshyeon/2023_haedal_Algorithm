import sys
from itertools import combinations
input = sys.stdin.readline

target = input().strip()
n = int(input())
books = {}

for _ in range(n):
    a,b = map(str,input().split())
    books[b]=int(a)


result=float('inf')
for i in range(1,n+1):
    for items in combinations(books.keys(),i):
        answer = list(target)
        sum=0
        for item in items:
            book = list(item)
            temp=answer.copy()

            for c in temp:
                if c in book:
                    book.remove(c)
                    answer.remove(c)


            sum+=books[item]
            if len(answer)==0:
                result = min(sum,result)

if result==float('inf'):
    print(-1)
else:
    print(result)
