F=lambda w:f'{abs(w):.3f}'
G=lambda w:'-+'[w<0]
import sys,math
for i in sys.stdin:
    A,a,B,b,C,c=map(float,i.split())
    P=(A+B)/2;p=(a+b)/2;Q=(C+B)/2;q=(c+b)/2
    t=((A-B)*(P-Q)/(a-b)+p-q)/((A-B)*(b-c)/(a-b)+C-B)
    h,k=Q+t*(b-c),q+t*(C-B)
    r=math.hypot(A-h,a-k)
    v=r*r-h*h-k*k
    print(f'(x {G(h)} {F(h)})^2 + (y {G(k)} {F(k)})^2 = {F(r)}^2')
    print(f'x^2 + y^2 {G(h)} {F(2*h)}x {G(k)} {F(2*k)}y {G(v)} {F(v)} = 0\n')
