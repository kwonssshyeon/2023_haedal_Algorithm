# 4673.py
# https://www.acmicpc.net/problem/4673



numbers = list(range(1,10001))
remove_list = []

for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        remove_list.append(num)
        
for remove_num in set(remove_list):
    numbers.remove(remove_num)
for self_num in numbers:
    print(self_num)