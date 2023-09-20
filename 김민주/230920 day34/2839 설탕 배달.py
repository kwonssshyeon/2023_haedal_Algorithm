n = int(input())

count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5 # 5kg 짜리에 담기
        print(count)
        break

    n -= 3 # 3kg 짜리에 담기
    count += 1

else: print(-1)
