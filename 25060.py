from math import*
H=hypot
d=lambda x,y:H(x[0]-y[0],x[1]-y[1])
s=lambda A,B,C:(d(B,C),d(C,A),d(A,B))
j=lambda a,b,c:acos(max(-1,min((b*b+c*c-a*a)/(2*b*c),1)))
t=lambda a,b,c:1/cos(j(a,b,c)-pi/6)
b=lambda A,B,C,p,q,r:[(p*A[i]+q*B[i]+r*C[i])/(p+q+r)for i in[0,1]] 
f=lambda A,B,C:A if j(*s(A,B,C))>=2*pi/3 else B if j(*s(B,C,A))>=2*pi/3 else C if j(*s(C,A,B))>=2*pi/3 else b(A,B,C,d(B,C)*t(*s(A,B,C)),d(C,A)*t(*s(B,C,A)),d(A,B)*t(*s(C,A,B)))
U=lambda:map(int,input().split())
x1,y1=U();x2,y2=U();x3,y3=U()
x,y=(x1+x2+x3)/3,(y1+y2+y3)/3
try:
    for i in range(40):
        T=2**(10-i)
        while 1:
            def F(p,q):
                x0,y0=x+p,y+q
                X1,Y1=f([x0,y0],[x1,y1],[x2,y2])
                X2,Y2=f([x0,y0],[x2,y2],[x3,y3])
                X3,Y3=f([x0,y0],[x3,y3],[x1,y1])
                d1=H(X1-x0,Y1-y0)+H(X1-x1,Y1-y1)+H(X1-x2,Y1-y2)
                d2=H(X2-x0,Y2-y0)+H(X2-x2,Y2-y2)+H(X2-x3,Y2-y3)
                d3=H(X3-x0,Y3-y0)+H(X3-x3,Y3-y3)+H(X3-x1,Y3-y1)
                return max(d1,d2,d3)
            P=[[0,0],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
            Q=[F(w[0]*T,w[1]*T)for w in P]
            m=min(Q)
            if m!=Q[0]:
                X,Y=P[Q.index(m)]
                x+=X*T
                y+=Y*T
            else:
                break
    X1,Y1=f([x,y],[x1,y1],[x2,y2])
    X2,Y2=f([x,y],[x2,y2],[x3,y3])
    X3,Y3=f([x,y],[x3,y3],[x1,y1])
    d1=H(X1-x,Y1-y)+H(X1-x1,Y1-y1)+H(X1-x2,Y1-y2)
    d2=H(X2-x,Y2-y)+H(X2-x2,Y2-y2)+H(X2-x3,Y2-y3)
    d3=H(X3-x,Y3-y)+H(X3-x3,Y3-y3)+H(X3-x1,Y3-y1)
    print(max(d1,d2,d3))
except(ZeroDivisionError,ValueError):print(max(H(x1-x2,y1-y2),H(x2-x3,y2-y3),H(x3-x1,y3-y1)))
