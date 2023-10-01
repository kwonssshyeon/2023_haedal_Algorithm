theend = [] # 종말의 수 리스트
i = 666 # 검사할 수

n = int(input())

while(True):
    if "666" in str(i):
        theend.append(i) 
        if len(theend) == n:
            break
    i += 1

print(i)