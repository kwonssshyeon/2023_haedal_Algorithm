# [level 1] K번째수 - 42748

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

### 성능 요약

메모리: 33.5 MB, 시간: 0.11 ms

### 구분

코딩테스트 연습 > 정렬

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2023년 11월 4일 17:34:36

### 문제 설명

<p>배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.</p>

<p>예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면</p>

<ol>
<li>array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.</li>
<li>1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.</li>
<li>2에서 나온 배열의 3번째 숫자는 5입니다.</li>
</ol>

<p>배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>array의 길이는 1 이상 100 이하입니다.</li>
<li>array의 각 원소는 1 이상 100 이하입니다.</li>
<li>commands의 길이는 1 이상 50 이하입니다.</li>
<li>commands의 각 원소는 길이가 3입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>array</th>
<th>commands</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 5, 2, 6, 3, 7, 4]</td>
<td>[[2, 5, 3], [4, 4, 1], [1, 7, 3]]</td>
<td>[5, 6, 3]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.<br>
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.<br>
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.</p>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

# 문제 풀면서 알게된 함수 및 문법 정리

## slice (a, b)

`arr.slice([begin[, end]])`

### begin

-   잘라낼 배열의 시작 index

### end

-   잘라낼 배열의 종료 index
-   end index의 직전까지 잘라낸다.
-   end index가 생략되면, begin index부터 배열의 끝까지를 잘라낸다.

## sort(a, b)

자바스크립트에서 배열을 정렬할 때는 `sort()` 함수나 `toSorted()` 함수를 사용한다.
<br>
`sort()` 함수를 사용할 때 주의해야할 점은 <b>정렬하기 전에 배열의 값을 내부적으로 문자열로 변환</b> 한다는 점이다.
<br>
이러한 특성 때문에 숫자로 이뤄진 배열을 정렬할 때 생각했던 결과와 다른 결과를 얻을 수도 있다.

```javascript
[100, 3, 1, 20].sort();
// [1, 100, 20, 3]
```

### 숫자 배열 정렬

`sort()` 함수는 인자로 정렬 기준을 나타내는 콜백 함수를 함수로 받는데, 이 대소비교를 위한 함수에는 2개의 인자로 넘어오며 다음과 같은 규칙을 따라야 한다.

-   첫 번째 인자가 두 번째 인자보다 작으면 <b>음수</b>를 반환
-   첫 번째 인자가 두 번째 인자보다 크면 <b>양수</b>를 반환
-   첫 번째 인자가 두 번째 인자와 같으면 `0` 을 반환
    <br>
    <br>

따라서 숫자 배열을 제대로 <b>오름차순 정렬</b>하기 위해서는 첫번째 인자에서 두 번째 인자를 빼준다.

```javascript
[-3, 2, 0, 1, 3, -2, -1].sort((a, b) => a - b);
// [-3, -2, -1, 0, 1,  2,  3]
```

<br>
반대로 숫자 배열을 <b>내림차순으로 정렬</b>하고 싶다면 피연산자의 순서를 바꿔줘야 한다.

```javascript
[-3, 2, 0, 1, 3, -2, -1].sort((a, b) => b - a);
// [3, 2, 1, 0, -1, -2, -3]
```

### 객체에서 정렬

국가 코드 기준으로 정렬

```javascript
countries.sort((a, b) => a.code.localeCompare(b.code));
/**
[
  { no: 2, code: 'CA', name: 'Canada' },
  { no: 5, code: 'CN', name: 'China' },
  { no: 4, code: 'GB', name: 'United Kingdom' },
  { no: 1, code: 'KR', name: 'Korea' },
  { no: 3, code: 'US', name: 'United States' }
]
*/
```

-   문자열 정렬 : `localCompare()` 사용

<br>

국가 번호를 기준으로 정렬

```javascript
countries.sort((a, b) => b.no - a.no);
/**
[
  { no: 5, code: "CN", name: "China" },
  { no: 4, code: "GB", name: "United Kingdom" },
  { no: 3, code: "US", name: "United States" },
  { no: 2, code: "CA", name: "Canada" },
  { no: 1, code: "KR", name: "Korea" },
]
*/
```
