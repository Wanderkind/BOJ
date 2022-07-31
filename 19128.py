from math import hypot as h
A,a=map(int,input().split())
B,b=map(int,input().split())
C,c=map(int,input().split())
def f(x,y):return h(A-x,a-y)+2*h(B-x,b-y)+3*h(C-x,c-y)
x,y=(A+B+C)/3,(a+b+c)/3
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
print(m)
