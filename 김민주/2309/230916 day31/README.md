[25206 너의 평점은](https://www.acmicpc.net/problem/25206)  
===========

> 예제 입력 1  
```
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P
```  
> 예제 출력 1  
```
3.284483
```

### 풀이  
  
--------------
1. 입력 한 줄씩 요구하는 타입, 데이터로 저장
2. **grade == "P"이면 학점에도 포함 x 평점에도 포함 x** 주의하기
3. 나머지는 평점 계산, 출력

### note  

--------------
1. if 문으로 케이스마다 일일이 처리하지 말고 딕셔너리 사용하기 
2. sol 2) [list 변수 만들어서 저장하기](<25206 너의 평점은1.py>)