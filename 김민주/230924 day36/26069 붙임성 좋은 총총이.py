# [🌈🤸](https://www.acmicpc.net/problem/26069)

n = int(input())

name_dic = {}

for i in range(1, n+1):
    a, b = input().split()

    if a == "ChongChong" or b == "ChongChong":
        name_dic[a] = True
        name_dic[b] = True
    elif a in name_dic.keys() and name_dic[a] == True:
        name_dic[a] = True 
        name_dic[b] = True
    elif b in name_dic.keys() and name_dic[b] == True:
        name_dic[a] = True 
        name_dic[b] = True
    else:
        name_dic[a] = False
        name_dic[b] = False

count = sum(1 for value in name_dic.values() if value == True)
print(count)
