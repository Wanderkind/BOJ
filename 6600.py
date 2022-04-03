from math import*
try:
 while 1:
  A,a,B,b,C,c=map(float,input().split())
  print(round(abs(pi*hypot(A-C,a-c)/sin(atan2(a-b,A-B)-atan2(c-b,C-B))),2))
except EOFError:exit()
