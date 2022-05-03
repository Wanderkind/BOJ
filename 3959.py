from math import*
g=9.81
for _ in range(int(input())):
    j,p,H,L=map(int,input().split())
    V=sqrt(2*g*j)
    def f(l):
        return H+p-g*(l/V)**2/2
    if j<L*L/(8*H+16*p):
        l=sqrt(p/((1/4/j)-(2*H/L/L)))
        A=abs(atan2(4*H*l/L,L)-atan2(g*l/V,V))
    elif j<L*L/4/(H+p):
        l=(4*H/L+sqrt(16*H*H/L/L+(p-H)*(8*H/L/L+1/j)))/(4*H/L/L+1/2/j)
        A=abs(atan2(4*H*(l/L-1),L)-atan2(-g*l/V,V))
    else:
        l=2*sqrt(j*(H+p))
        A=atan2(g*l/V,V)
    c=hypot(V,sqrt(2*g*(H+p-f(l))))
    print(l,c,A*180/pi)
