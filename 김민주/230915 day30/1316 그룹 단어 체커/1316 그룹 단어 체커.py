# [1316 그룹 단어 체커](https://www.acmicpc.net/problem/1316)  

n = int(input())
count = 0

for _ in range(n):
    word = input()
    used = []

    for letter in word: 
        # 한 개씩 체크하며 이미 들어온 문자인지 체크...하면 안되잖아?
        # 현재 문자가 이미 사용한 문자 중에 있고, 바로 직전 문자와 다른지도 체크해야 함
        if (letter in used) and (letter != used[-1]):
            break

        used.append(letter)
    else: 
        count += 1

print(count)