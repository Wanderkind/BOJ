I=input;from math import*
for _ in range(int(I())):
 z=0
 for _ in range(int(I())):
  X,Y,x,y=map(int,I().split())
  z+=1-abs(abs(atan2(Y,X)-atan2(y,x))/pi-1)
 print('{:.5f}'.format(round(z/2,5)))
