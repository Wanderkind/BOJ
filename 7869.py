from math import*
X,Y,R,x,y,r=map(float,input().split())
d=hypot(X-x,Y-y)
if R+r<d:k=0
elif abs(R-r)<d:a=(d**2+R**2-r**2)/2/d;k=R**2*acos(a/R)+r**2*acos((d-a)/r)-d*sqrt(R**2-a**2)
else:k=(min(R,r)**2)*pi
print('{:.3f}'.format(round(k,3)))
