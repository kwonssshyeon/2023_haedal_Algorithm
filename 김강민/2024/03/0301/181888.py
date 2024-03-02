def solution(num_list, n):
    return num_list[::n]

# items[start:stop:step]
# start: 시작 인덱스
# stop: 끝 인덱스
# step: 간격
# slice를 사용할 때 보통 item[start:stop] 만 사용하는 경우가 많은데
# step을 사용하면 step만큼 건너뛰면서 슬라이싱을 할 수 있다.