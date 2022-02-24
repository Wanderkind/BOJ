import math
Q,l,w,i=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'],[],1,-1
for _ in range(4):h,m=map(int,input().split(':'));l+=[h*60+m]
a,b,c,d=l;g=math.gcd(c,d)
if(b-a)%g>0:print('Never')
else:
 while 1:
  i+=1;Z=b+d*i
  if(Z-a)%c<1:break
 print(Q[(Z//1440)%7]);print(f'{str((Z//60)%24).zfill(2)}:{str(Z%60).zfill(2)}')
