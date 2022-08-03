from functools import reduce as R
import sys
input=sys.stdin.readline
Q=lambda a:(a>0)-(a<0)
T=lambda p,q,r:Q((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
def L(H,r):
    while len(H)>1 and T(H[-2],H[-1],r)<1:H.pop()
    if not len(H) or H[-1]!=r:H.append(r)
    return H
def c(P):
    P.sort()
    l,u=R(L,P,[]),R(L,P[::-1],[])
    return l.extend(u[i] for i in range(1,len(u)-1)) or l
C=c([[*map(int,input().split())]for _ in range(int(input()))])
l=len(C)
if l==1:
    exit(print(0))
if l==2:
    X,Y=C[0];x,y=C[1]
    exit(print((X-x)**2+(Y-y)**2))
if l==3:
    u=[]
    for i in range(3):
        X,Y=C[i-1];x,y=C[i]
        u.append((X-x)**2+(Y-y)**2)
    exit(print(max(u)))
xM,xm,yM,ym=-10000,10000,-10000,10000
for i in range(l):
    x,y=C[i]
    if x>xM:xM=x;p=i
    elif x<xm:xm=x;r=i
    if y>yM:yM=y;q=i
    elif y<ym:ym=y;s=i
m=min(p,q,r,s)
A=C[s:p+1] if m!=p else C[s:]+C[:p+1]
a=C[p:q+1] if m!=q else C[p:]+C[:q+1]
B=C[q:r+1] if m!=r else C[q:]+C[:r+1]
b=C[r:s+1] if m!=s else C[r:]+C[:s+1]
M=0
for i in A:
    X,Y=i
    for j in B:
        x,y=j
        d=(X-x)**2+(Y-y)**2
        if d>M:M=d
for i in a:
    X,Y=i
    for j in b:
        x,y=j
        d=(X-x)**2+(Y-y)**2
        if d>M:M=d
print(M)
