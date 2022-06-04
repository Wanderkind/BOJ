from math import*
import sys
input=sys.stdin.readline
th=sqrt(3)
while 1:
    I=input().strip()
    if I=='0 0 0 0 0':
        break
    r,X,Y,x,y=map(float,I.split())
    X*=2/r;Y*=2/r;x*=2/r;y*=2/r
    P=3*floor(X/3)
    U=th*(2*round((Y-th*P%2)/2/th)+P%2)
    l1=[[P,U],[P+3,U-(2*(Y<U)-1)*th]]
    d1=[hypot(X-c[0],Y-c[1])for c in l1]
    M=min(d1)
    S=l1[d1.index(M)]
    p=3*floor(x/3)
    u=th*(2*round((y-th*p%2)/2/th)+p%2)
    l2=[[p,u],[p+3,u-(2*(y<u)-1)*th]]
    d2=[hypot(x-c[0],y-c[1])for c in l2]
    m=min(d2)
    s=l2[d2.index(m)]
    if S==s:
        z=hypot(X-x,Y-y)
    else:
        A,B=abs(S[0]-s[0]),abs(S[1]-s[1])
        if B/A<10**-8+1/th:
            t=2*A/th
        else:
            t=B+A/th
        z=M+m+t
    print('{:.3f}'.format(z*r/2))
