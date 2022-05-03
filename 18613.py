from decimal import*
getcontext().prec=40
import math,sys
input=sys.stdin.readline
input()
l=[*map(int,input().split())]
for i in l:
  n=(Decimal(24*i+1).sqrt()-5)//12
  k=i-6*n*n-5*n-1
  if k<1:z=8
  elif k<2*n+2:z=9
  elif k<6*n+4:z=0
  elif k<6*n+5:z=1
  elif k<8*n+7:z=0
  else:z=9
  print(z,end=' ')
