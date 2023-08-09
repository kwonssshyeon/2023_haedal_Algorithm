import sys
import math
input = sys.stdin.readline


if __name__ == "__main__":
  a, b, c, d, e, f = map(int, input().split())
   
  lcm = abs(a * d) // math.gcd(a, d)
    
  if a == 0:
    y = c//b
    x = (f - e*y) // d
  elif d == 0:
    y = f//e
    x = (c - b*y) // a
  else: 
    y = (lcm//a*c - lcm//d*f) // (lcm//a*b - lcm//d*e)
    x = (c - b*y) // a
    
  print(x, y)
