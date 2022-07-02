from math import*
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
z=0
e,f=0,1
n,m=U()
L=[[*U()]for _ in range(n)]
d={}
l=[]
h=0
for i in L:
    a,b=i
    r=b/a
    T=(r,a)
    if T not in d:
        d[T]=i
    else:
        h+=1
        T=(r,a,h)
        d[T]=i
    l.append(T)
l.sort()
while 1:
    w,v=d[l[-1]]
    if m>=w:
        z+=v
        del l[-1]
    else:
        e=v*m
        f=w
        G=gcd(e,f)
        e//=G
        f//=G
    m-=w
    if m<=0:
        break
e+=f*z
print(f'{e}/{f}')
