def search_list(a, x):
    n = len(a)              # 입력 크기 n
    for i in range(0, n):   # 리스트 a의 모든 값을 차례로
        if x == a[i]:       # x 값과 비교하여
            return i        # 같으면 위치를 돌려준다.
    return -1               # 끝까지 비교해도 없으면 -1을 돌려준다.

v = [17, 92, 18, 33, 58, 5, 33, 42]
print(search_list(v, 18))  # 2(순서상 세 번째지만, 위치 번호는 2)
print(search_list(v, 33))  # 3(33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
print(search_list(v, 900))  # -1(900은 리스트에 없음)
