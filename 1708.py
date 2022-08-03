from functools import reduce as R
import sys
input=sys.stdin.readline
Q=lambda a:(a>0)-(a<0)
T=lambda p,q,r:Q((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
def L(H,r):
    while len(H)>1 and T(H[-2],H[-1],r)==-1:H.pop()
    if not len(H) or H[-1]!=r:H.append(r)
    return H
def c(P):
    P.sort()
    l,u=R(L,P,[]),R(L,P[::-1],[])
    return l.extend(u[i] for i in range(1,len(u)-1)) or l
C=c([[*map(int,input().split())]for _ in range(int(input()))])
p,q=C[-1];r,s=C[-2]
for i in range(len(C)-3,-3,-1):
    x,y=C[i]
    if (x-r)*(s-q)==(r-p)*(y-s):r,s=x,y;del C[i+1]
    else:p,q,r,s=r,s,x,y
print(len(C))
