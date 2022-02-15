a,b,c,d=map(int,input().split());p,q,r,s=map(int,input().split())
u=555/797;v=572/797;A=u*a-v*b;B=v*a+u*b;C=u*c-v*d;D=v*c+u*d;P=u*p-v*q;Q=v*p+u*q;R=u*r-v*s;S=v*r+u*s
try:x=((C-A)*(Q*R-P*S)-(R-P)*(B*C-A*D))/((R-P)*(D-B)-(C-A)*(S-Q));print(0 if(A-x)*(C-x)>0 or(P-x)*(R-x)>0 else 1)
except ZeroDivisionError:print(0)
