# 9012 괄호 (스택) https://www.acmicpc.net/problem/9012

def isVPS(ps) -> bool:
  stk = []
  
  for p in ps: 
    if p == "(":
      stk.append(p)
    
    elif p == ")":
      if not stk: 
        return False
        
      else: stk.pop()

  return len(stk) == 0


if __name__ == "__main__":
  # 테스트 데이터 수
  t = int(input())
  
  # 각 테스트 데이터에 대해
  for _ in range(t):    
    ps = input() # ((()))))( 
    
    if isVPS(ps):
      print("YES")
    else: 
      print("NO")

# Logic:
# 원소를 다 읽을 동안
  # (이면 스택에 넣고 
  # )이면 )는 버리고 (를 출력
  # )을 읽었는데 꺼낼 (이 없으면 -> NO 출력
# 끝까지 읽었다면
  # (이 남아있으면 -> NO 출력
  # 스택에 아무 것도 남아있지 않으면 -> YES 출력

# 이것 땜에 계속 틀림 ㅅㅍ
# len(stk) == 0인 상황이 두 가지로 나뉨!
  # 스트링에서 )을 읽었는데 꺼낼 (이 없으면 -> NO 출력
  # 스트링을 끝까지 다 읽었고 스택에 아무 것도 남아있지 않으면 -> YES 출력
