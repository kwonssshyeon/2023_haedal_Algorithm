# [👋🐻](https://www.acmicpc.net/problem/25192)

n = int(input())

stored_id = {}
count = 0

for _ in range(n):
    str = input()

    if str == "ENTER":
        for key, value in stored_id.items():
            if value == 1:
                count += 1

        stored_id = {}
    else: 
        # if str not in stored_id:
        #     stored_id[str]=1
        #     count += 1
        if str in stored_id:
            continue
        else:
            stored_id[str] = 1 # value는 딱히 필요 없어서 아무 값으로

for key, value in stored_id.items():
    if value == 1:
        count += 1
print(count)