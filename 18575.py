import sys
input=sys.stdin.readline
from math import*

L,R=0,pi
for _ in range(60):
    t=(L+R)/2
    if sin(2*t)-t*(cos(2*t)+1/2)>0:
        L=t
    else:
        R=t

for _ in range(int(input())):
    k,l=map(int,input().split())
    r=l/t
    a=2*r*sin(t/2)
    if k>=a:
        s=r*r*(t/2-sin(t)*cos(t))/2.1863866825110
    else:
        L,R=0,pi/2
        for _ in range(60):
            p=(L+R)/2
            if sin(p)/(2*pi-2*p)>k/2/l:
                R=p
            else:
                L=p
        th=2*pi-2*p
        r=l/th
        s=r*r*(th/2+sin(p)*cos(p))
    print(s)
