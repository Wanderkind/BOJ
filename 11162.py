A,a,B,b,C,c,D,d=map(int,input().split())
p,r=A-C,a-c
q,s=B-D-p,b-d-r
k=q**2+s**2
if k==0:print((p**2+r**2)**.5);exit()
def f(t):return((p+q*t)**2+(r+s*t)**2)**.5
u=-(p*q+r*s)/k
print(f(u if 0<u<1 else int(1<u)))
