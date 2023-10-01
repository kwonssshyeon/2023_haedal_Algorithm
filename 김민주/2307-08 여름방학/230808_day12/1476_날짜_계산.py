# 1476 날짜 게산

import sys
input = sys.stdin.readline

if __name__ == "__main__":
  e, s, m = map(int, input().split())

  year = 1
  while True: # 범위 없이 계속 돌아야 함
    if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
      print(year)
      break
    year += 1
    
