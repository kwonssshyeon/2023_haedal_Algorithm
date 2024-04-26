# 리스트에서 특정 숫자 위치 찾기(이분 탐색)
# 입력: 리스트 arr, 찾는 값 n
# 출력: 찾으면 그 값의 위치, 찾기 못하면 -1

def binary_search(arr, n):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a) -1)

    start = 0
    end = len(arr) -1
    
    while start <= end:             # 탐색할 범위가 남아 있는 동안 반복
        mid = (start + end) // 2    # 탐색 범위의 중간 위치
        if n == arr[mid]:           # 발견 !
            return mid
        elif n > arr[mid]:          # 찾는 값이 더 크면 오른쪽으로 범위를 좁혀 계속 탐색
            start = mid + 1
        else:                       # 찾는 값이 더 작으면 왼쪽으로 범위를 좁혀 계속 탐색
            end = mid - 1

    return -1                       # 찾지 못했을 때

import sys
input = sys.stdin.readline

n = int(input())

n_list = sorted(list(map(int, input().split())))

m = int(input())

m_list = list(map(int, input().split()))

for i in m_list:
    if binary_search(n_list, i) == -1:
        print(0)
    else:
        print(1)