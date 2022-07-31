from math import hypot as h
import sys
input=sys.stdin.readline
while 1:
    l=[*map(int,input().split())]
    if all(i==0 for i in l):break
    xa,ya,xb,yb,xc,yc=l
    a=h(xb-xc,yb-yc)
    b=h(xc-xa,yc-ya)
    c=h(xa-xb,ya-yb)
    S=a+b+c
    xi,yi=((a*xa+b*xb+c*xc)/S,(a*ya+b*yb+c*yc)/S)
    d=h(xi-xa,yi-ya)
    e=h(xi-xb,yi-yb)
    f=h(xi-xc,yi-yc)
    r=abs(xa*yb+xb*yc+xc*ya-xa*yc-xc*yb-xb*ya)/S
    s=S/2
    r1=r*(s-r+d-e-f)/2/(s-a)
    r2=r*(s-r-d+e-f)/2/(s-b)
    r3=r*(s-r-d-e+f)/2/(s-c)
    print(r1,r2,r3)
