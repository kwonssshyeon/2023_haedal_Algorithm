arr = []
for _ in range(10):
    number = int(input())
    if number % 42 not in arr:
        arr.append(number % 42)

print(len(arr))