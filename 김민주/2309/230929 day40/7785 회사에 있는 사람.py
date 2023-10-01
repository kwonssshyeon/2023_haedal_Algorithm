import sys

input = sys.stdin.readline

if __name__ == "__main__":
    nowworking = set()

    n = int(input())
    for _ in range(n):
        name, inout = input().split()
        if inout == "enter":
            nowworking.add(name)
        elif inout == "leave":
            nowworking.discard(name)

    nowworking_list = sorted(nowworking, reverse=True)
    # 아니면 이렇게 key=lambda x: x[::-1]

    for name in nowworking_list:
        print(name)