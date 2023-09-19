[1018 체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)  
=====

> 예제 입력 1  
```
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
```  
> 예제 출력 1  
```
1
```
<br>

> 예제 입력 2  
```
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
```  
> 예제 출력 2  
```
12
```

### 풀이  
  
-----
1. 색깔 바꿀 칸 찾기  
   1. 색깔 입력 받아서 board에 저장  
   2. 바꿔야하는지 체크 후 카운트 올리기 (자세한 건 코드 내에...)  
   3. 카운트 출력  
<br>
2. 보드 자르는 단계 추가  

### note  

-----
1. ~~첫 번째 셀은 무조건 그대로 두고 다음 셀부터 바꿔야 하나? 첫 번째 셀을 바꾸는 게 더 빠르면?~~  
**최소** 개수를 찾아야 하는데...  
```python
count = min(count, change_count, 8*8 - change_count)
```
change_count, 8*8 - change_count 비교해서 더 작은 쪽을 선택하면 됨!  

2. 둘이 같은 코드임  
        # 직전 색깔이랑 같으면 색깔 바꾸고 카운트 올리기. [0][1]부터  
        # if i > 0 and board[i - 1][j] == color:  
        #     color = not color  # 색깔 바꾸기  
        #     count += 1  
        #  
        # if j > 0 and board[i][j - 1] == color:  
        #     color = not color  # 색깔 바꾸기  
        #     count += 1  
        #  
        # ----------------------------------------------  
        # if i == 0: # 첫 줄  
        #     if j > 0:  
        #         previous = board[i][j - 1]  
        #  
        #         if color == previous:  
        #             color = not color # 색깔 바꾸기  
        #             count += 1  
        # else:  
        #     if j == 0:  
        #         previous = board[i - 1][0]  
        #  
        #         if color == previous:  
        #             color = not color # 색깔 바꾸기  
        #             count += 1  
        #     else:  
        #         previous = board[i][j - 1]  
        #  
        #         if color == previous:  
        #             color = not color # 색깔 바꾸기  
        #             count += 1  
