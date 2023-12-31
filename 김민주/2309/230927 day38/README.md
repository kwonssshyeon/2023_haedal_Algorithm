[20920 영단어 암기는 괴로워](https://www.acmicpc.net/problem/20920)  
=====

### 문제 요약

-----
화은이가 만들고자 하는 단어장의 단어 순서는  
1. 자주 나오는 단어일수록 앞에  
2. 길이가 길수록 앞에  
3. 알파벳 순   

길이가 M 이상인 단어들만 외운다.  
<br>

### 입력

-----
첫째 줄에는 영어 지문에 나오는 단어의 개수 N과 외울 단어의 길이 기준이 되는 M이 공백으로 구분되어 주어진다.  
(1 <= N <= 100,000, 1 <= M <= 10)  
둘째 줄부터 N+1번째 줄까지 외울 단어를 입력받는다. 알파벳 소문자로만 주어지며 단어의 길이 < 10  
단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.  
<br>

### 출력

-----
화은이의 단어장의 앞에 위치한 단어부터 한 줄에 한 단어씩 순서대로 출력한다.  
<br>

> 예제 입력 1  
```
7 4
apple
ant
sand
apple
append
sand
sand
```
> 예제 출력 1  
```
sand
apple
append
```

> 예제 입력 2  
```
12 5
appearance
append
attendance
swim
swift
swift
swift
mouse
wallet
mouse
ice
age
```  
> 예제 출력 2  
```
swift
mouse
appearance
attendance
append
wallet
```
<br>

### 풀이  
  
-----
1. 인풋 받아서
2. 단어 길이가 m 이상이면 저장
3. 주어진 순서대로 정렬 
4. 각 단어는 한 번씩 출력
<br>

### note  

-----
<리스트 정렬 순서 지정>
1. key와 lambda x를 이용  
    키가 두 개 이상이기 때문에 **lambda x**를 이용  
    ```
    sorted_list = sorted(my_list, key=lambda x: (len(x), x))
    ```
    > 길이 (오름차순), 알파벳 순  

1. 내림차순으로 하고싶다? -> -len(x)  
2. 리스트 요소의 빈도를 세고 싶다면 (딕셔너리 쓰지 않고) collections 모듈의 Counter 쓰자.  
   ([22108 통계학](<../230925 day37/22108 통계학.py>)에도 등장)  

---
<시간초과 해결>
1. word_list.count(x) -> 같은 함수를 여러 번 호출하면 시간 오래 걸리기 때문에 그냥 단어 빈도 세는 Counter 클래스 사용  
2. 리스트보다 집합 연산이 빠르다.  
   > **집합**은 중복된 요소를 허용하지 않으며 **내부적으로 해시 테이블을 사용**하기 때문에 특정 요소가 집합에 있는지 여부를 빠르게 확인할 수 있습니다.  
   어차피 printed(이미 출력한 단어)에는 각 단어가 한번씩만 저장될 거니깐...  

<br>

### 알고리즘 분류

-----
