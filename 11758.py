from math import*
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
o=atan2(y1-y2,x1-x2)-atan2(y3-y2,x3-x2)
if min(abs(o+2*pi),abs(o+pi),abs(o),abs(o-pi),abs(o-2*pi))<0.0000001:print(0)
elif -2*pi<o<-pi or 0<o<pi:print(1)
else:print(-1)
