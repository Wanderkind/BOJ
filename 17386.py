a,b,c,d=map(int,input().split());p,q,r,s=map(int,input().split())
if a==c or p==r:u=555/797;v=572/797;a=u*a-v*b;b=v*a+u*b;c=u*c-v*d;d=v*c+u*d;p=u*p-v*q;q=v*p+u*q;r=u*r-v*s;s=v*r+u*s
try:x=((c-a)*(q*r-p*s)-(r-p)*(b*c-a*d))/((r-p)*(d-b)-(c-a)*(s-q));print(0 if(a-x)*(c-x)>0 or(p-x)*(r-x)>0 else 1)
except ZeroDivisionError:print(0)
