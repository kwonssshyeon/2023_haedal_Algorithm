알고2에서 배웠던 union-find 복습!

일반적인 union-find는 root가 작은 쪽으로 union을 하는데
이 문제의 경우 최소비용이라는 조건이 추가됨

-> union시에 비용이 더 적은 쪽으로 합친다. 그러면 마지막에 비교할때 parent의 값과 index가 같은 경우 root(즉, unique한 집합)으로 판단하면 되고, 해당 index가 가르키는 need값이 최소비용 중 하나가 된다.