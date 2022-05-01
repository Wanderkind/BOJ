from math import*
X,Y,R,x,y,r=map(float,input().split())
d=hypot(X-x,Y-y)
if R+r<d:k=0
elif abs(R-r)<d:a=(d*d+R*R-r*r)/2/d;k=R*R*acos(a/R)+r*r*acos((d-a)/r)-d*sqrt(R*R-a*a)
else:k=(min(R,r)**2)*pi
print('{:.3f}'.format(round(k,3)))
