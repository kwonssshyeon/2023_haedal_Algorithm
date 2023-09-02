import heapq  # 우선순위큐
import sys
input = sys.stdin.readline

n = int(input())
time = []

for i in range(n):
    start, end = map(int,input().split())
    time.append([start,end])

time.sort(key=lambda x : x[0])

# 앞 강의의 종료시각과 뒷 강의의 시작시각 간 비교
heap = []
heapq.heappush(heap, time[0][1])

for i in range(1,n):
    if heap[0] > time[i][0]:
        heapq.heappush(heap,time[i][1])
    else:
        # 같은 회의실을 사용하는 경우 기존수업 pop -> 새로운수업 push
        heapq.heappop(heap)
        heapq.heappush(heap,time[i][1])


print(len(heap))




# 입력받은 모든 수업이 수행되어야한다.
# 큐에서 push할때마다 강의실이 더 필요할 것으로 간주
# 큐는 각 강의실에서 현재 종료시간이 가장 늦은 수업들로 이루어짐


# 자료구조 공부 ...