from math import*
import sys
input=sys.stdin.readline

def val(x,y,r,t):
    a=(atan2(y,x)-t)%(2*pi)
    if pi/2<abs(a)<3*pi/2:
        return 0
    d=hypot(y,x)*sin(a)
    return sqrt(max(0,r*r-d*d))

while 1:
    n=int(input())
    if not n:break
    l=[[*map(int,input().split())]for _ in range(n)]
    V=2*max([sum(val(*i,pi/720*t)for i in l)for t in range(1440)])
    print(f'{V:.3f}')
