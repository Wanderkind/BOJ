from math import hypot as H
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    h,a,b,c,A,B,C=map(int,input().split())
    def f(u,v):return H(a,h*u)/A+H(b,h*(1-u-v))/B+H(c,h*v)/C
    x,y=1/3,1/3
    for i in range(4):
        t=3**(-i-2)
        while 1:
            p=[[0,0],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
            q=[f(x+w[0]*t,y+w[1]*t)for w in p]
            m=min(q)
            if m!=q[0]:
                X,Y=p[q.index(m)]
                x+=X*t
                y+=Y*t
            else:
                break
    print(f(x,y))
