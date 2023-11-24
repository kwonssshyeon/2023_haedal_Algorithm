from collections import deque
dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)

dq.popleft()
print(dq)

#입력 크기 10만이 넘어간다.
# logN => 17횟수

#