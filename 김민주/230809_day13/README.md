19532 수학은 비대면강의입니다  
================  
ax + by = c  
dx + ey = f  
(-999 <= a,b,c,d,e,f <= 999)  
연립방정식 푸는 프로그램 만들기 - 제목이랑 아무 관계 없음...  

-----------------------  

#### brute-force 알고리즘  
걍 중딩 때 배운 대로... 하면 됨.  
  
        lcm//a * (a*x + b*y) = lcm//a * c  
    -)  lcm//d * (d*x + e*y) = lcm//d * f  
                        ↓ (분배)
        lcm * x + lcm//a * b * y = lcm//a * c  
    -)  lcm * x + lcm//d * e * y = lcm//d * f  
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
    (lcm//a * b - lcm//d * e) * y = lcm//a * c - lcm//d * f  
    y = (lcm//a * c - lcm//d * f) // (lcm//a * b - lcm//d * e)  
<br/>

#### 백준 온라인 저지 시스템 몇 가지 정리  

1. 최소공배수(LCM) 구하기
    > [파이썬, Python] 최소공배수(LCM) https://computer-science-student.tistory.com/585
    근데  
```python
lcm = math.lcm(a, d)
```
    이건 안 되고  
```python
lcm = abs(a * d) // math.gcd(a, d)
```
    이렇게 gcd() 이용해서 구해야 함.  
    왜냐하면 백준은 파이썬 3.7로 돌아가는데 **lcm()은 3.9부터 지원해서...**  
<br/>
  
2. 나누는 수인 a와 d가 0인 경우를 고려하지 않았어서 런타임 에러(ZeroDivisionError)가 계속 났음.  
   **a == 0일 때, d == 0일 때, 둘 다 아닐 때로 케이스를 나눠야 함.**  
   > 그럼 b와 e가 0인 건...? -> 고려하지 않아도 됨. a, b 모두 0이거나 d, e가 모두 0이면 방정식 성립이 안됨.  
