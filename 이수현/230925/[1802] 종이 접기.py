import sys

input = sys.stdin.readline

def origami(test_case):
    length = len(test_case) // 2
    print(length)
    for i in range(length + 1):  # 접는 회수
        print(test_case[i * 2], i * 2)
        return "YES"
    return "NO"


N = int(input())
test = []
for _ in range(N):
    test.append(input().rstrip())
for test_case in test:
    print(origami(test_case))

