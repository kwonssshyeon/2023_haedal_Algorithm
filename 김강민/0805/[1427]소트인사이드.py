num = list(map(int, str(input())))

num.sort(reverse=True)
for i in num:
    print(i, end='')