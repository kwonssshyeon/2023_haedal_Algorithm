1476 날짜 계산
================
준규네 나라 연도 표기법: E S M (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)  
우리식 표기법으로는 몇 년인가? (가장 빠른 연도를 출력함)  

-----------------------  

16년:  
16 % 15 = 1  
16 % 28 = 16  
16 % 19 = 16  
  
5266년:  
5266 % 15 = 1  
5266 % 28 = 2  
5266 % 19 = 3  
  
x년:  
x % 15 = e  
x % 28 = s  
x % 19 = m  
  
**거꾸로 가서 x를 구하려면 어떻게 해야하지?**  

#### 알고리즘  
> 구하는 값의 범위가 정해져있지 않고 걍 계속 검사해야 하므로 for문 대신 while문으로 묶는다.  
  
sol1. 가능한 e, s, m 리스트를 만들고 겹치는 최솟값을 찾는다. -> 시간 초과
```python
e_list = []; s_list = []; m_list = []
year = 1
while True: # 범위 없이 계속 돌아야 함
  if year % 15 == e:
    e_list.append(year)
  if year % 28 == s:
    s_list.append(year)
  if year % 19 == m:
    m_list.append(year)

  is_in_all_lists = year in e_list and year in s_list and year in m_list
  if is_in_all_lists: 
    print(year)
    break
  year += 1
```
sol2. (year - e) % 15 == 0: year에서 e를 뺀 값이 0으로 나누어떨어지는가  
```python
year = 1
while True:
  if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
    print(year)
    break
  year += 1
```

