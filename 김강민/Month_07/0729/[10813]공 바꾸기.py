N , M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp
    
for i in range(N):
    print(basket[i], end=" ")
