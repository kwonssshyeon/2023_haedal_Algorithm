# 7/30
## 피보나치 수 6 - 11444 

[문제 링크](https://www.acmicpc.net/problem/11444) 

### 분류

분할 정복을 이용한 거듭제곱, 수학

### 문제 설명

<p>피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.</p>

<p>이를 식으로 써보면 F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> (n ≥ 2)가 된다.</p>

<p>n=17일때 까지 피보나치 수를 써보면 다음과 같다.</p>

<p>0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597</p>

<p>n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.</p>


<details>
<summary>풀이과정</summary>
<div markdown="1">
피보나치 수는 행렬화가 가능하다.<br>
[ F_{n+1}, F_{n} ]    [ 1, 1 ] ^n<br>
[ F_{n}, F_{n-1} ]  = [ 1, 0 ]
 <br>(유도과정은 https://restudycafe.tistory.com/497 참조)
 
1, 2, 4, 8, 16, ...등의 2의 제곱수는 ${{{2^1}^2}^2}^2...$식으로 빠르게 계산이 가능하다.<br> 그리고 모든 자연수는 2진법으로 표현이 가능하므로 2의 제곱수들의 합으로 나타낼 수 있다. 예를들어 100은 64+32+4이다.<br>따라서 어떤 수의 거듭제곱수는 곧 2의 제곱수 승을 가진 수들의 곱으로 나타낼 수 있다.<br><br> 이를 이용하면 거듭제곱수는 분할정복을 통해 빠르게 계산이 가능하다.<br>예를 들어, 위 행렬을 M이라고 한다면 $M^{100}=M^{1100100_2}=M^{64+32+4}=M^{64}*M^{32}*M^4$ 이다.<br>마지막 식의 각 항들은 빠르게 계산이 가능하다.
  
</div>
</details>
