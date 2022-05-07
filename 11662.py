A,a,B,b,C,c,D,d=map(int,input().split())
p,r=A-C,a-c
q,s=B-D-p,b-d-r
k=q*q+s*s
if k==0:exit(print((p*p+r*r)**.5))
def f(t):return((p+q*t)**2+(r+s*t)**2)**.5
u=-(p*q+r*s)/k
print(f(u if 0<u<1 else 1<u))
