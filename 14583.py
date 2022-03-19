from math import*
h,v=map(float,input().split())
t=atan(v/h)/2
print(round(h/cos(t)/2,2),round(v*cos(t)-h*sin(t),2))
