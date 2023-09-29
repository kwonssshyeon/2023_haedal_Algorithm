[7785 회사에 있는 사람](https://www.acmicpc.net/problem/7785)  
=====

### 문제 요약

-----
<집합 - 삽입/제거>  
어떤 사람이 회사에 들어왔는지, 나갔는지 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.  
<br>

### 입력

-----
첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106)  
다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다.  
<br>

### 출력

-----
현재 회사에 있는 사람의 이름을 **사전 순의 역순**으로 **한 줄에 한 명씩** 출력한다.  
<br>

예제 입력 1  
```
4
Baha enter
Askar enter
Baha leave
Artem enter
```  
예제 출력 1  
```
Askar
Artem
```
<br>

### 풀이  
  
-----

<br>

### note  

-----
1. #### 집합의 요소 제거  
   **remove()**: 제거하는 아이템이 없으면 오류  
   **discard()**: 오류 안 남  
   > 요소가 반드시 집합에 있어야 한다면 remove(), 오류를 발생시키지 않으려면 discard()를 쓰면 된다.  

2. #### 맨날 해도 헷갈리는 공백으로 구분된 입력 받기...  
   1. 튜플로 입력받기. 문자열 그대로
      ```python
      name, inout = input().split()
      ```

   2. 정수형으로 타입 변환하여 받기
      ```python
      name, inout = map(int, input().split())
      ```

   3. 정수형 리스트로 받기
      ```python
      list = list(map(int, input().split()))
      ```
   <br>

   map()이란... not suscriptable  
   **map 객체를 인덱싱할 수 없다.** 하려면 리스트형으로 만들어야...  

3. #### 집합을 리스트로 
   만들 수 있다. sorted() 사용  
   
4. #### lambda에 대하여  
   익명의 함수를 생성할 때 사용  
   문법  
   ```
   lambda arguments: expression
   ```
   arguments: 입력 매개변수(인자)를 나타내는 부분입니다.  
   expression: 입력 매개변수를 이용하여 계산하고 반환할 결과  
   <br>
   e.g. key를 사용하여 리스트의 요소들을 재정렬하고 싶을 때  
   ```
   lambda x: x[::-1]  
   ```
   리스트가 매개변수 x로 들어가고 x의 요소들을 역순으로 반환  

   1. #### 슬라이스 표기법  
      [start:end]  
      e.g. [:] 처음부터 끝까지 반환  
      [start:stop:step]
      e.g. [::-1] 처음부터 끝까지 역순으로 반환  

<br>

### 알고리즘 분류

-----
- 자료 구조
- 해시를 사용한 집합과 맵