from math import*
import sys
input=sys.stdin.readline

def g(x):
    if x>=0: return x-pi
    else: return x+pi

def h(x,y): return max(x)-min(x)>pi and max(y)-min(y)>pi

def sol(AA, BB):
    X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3 = AA
    x1,y1,z1,x2,y2,z2,x3,y3,z3 = BB
    a,b,c=(Y2-Y1)*(Z3-Z1)-(Y3-Y1)*(Z2-Z1),(Z2-Z1)*(X3-X1)-(Z3-Z1)*(X2-X1),(X2-X1)*(Y3-Y1)-(X3-X1)*(Y2-Y1)
    d=a*X1+b*Y1+c*Z1
    def f(x,y,z):
        return (a*x+b*y+c*z-d)/hypot(a,b,c)
    U=[[X1,Y1,Z1],[X2,Y2,Z2],[X3,Y3,Z3]]
    V=[[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
    l=[f(*i) for i in V]
    if all(i>=0 for i in l) or all(i<=0 for i in l):
        return False
    elif any(i==0 for i in l):
        I=l.index(0)
        P=V[I]
        del V[I]
        s,t=[abs(f(*i)) for i in V]
        R=[(V[0][i]*t+V[1][i]*s)/(s+t) for i in range(3)]
        if c!=0:
            u=[[i[0], i[1]] for i in U]
            r=[R[0], R[1]]
            p=[P[0], P[1]]
        elif a!=0:
            u=[[i[1], i[2]] for i in U]
            r=[R[1], R[2]]
            p=[P[1], P[2]]
        else:
            u=[[i[0], i[2]] for i in U]
            r=[R[0], R[2]]
            p=[P[0], P[2]]
        A1=[atan2(r[1]-u[i][1],r[0]-u[i][0]) for i in range(3)]
        A2=[g(i) for i in A1]
        B1=[atan2(p[1]-u[i][1],p[0]-u[i][0]) for i in range(3)]
        B2=[g(i) for i in B1]
        return h(A1,A2) ^ h(B1,B2)
    else:
        w=(prod(l)>0)-.5
        At=[V[i] for i in range(3) if l[i]*w>0]
        B=[V[i] for i in range(3) if l[i]*w<0]
        A=At[0]
        k=abs(f(*A))
        C=[abs(f(*i)) for i in B]
        R=[[(A[i]*C[j]+B[j][i]*k)/(C[j]+k) for i in range(3)]for j in range(2)]
        if c!=0:
            u=[i[0:2] for i in U]
            R1,R2=[i[0:2] for i in R]
        elif a!=0:
            u=[i[1:3] for i in U]
            R1,R2=[i[1:3] for i in R]
        else:
            u=[[i[0]]+[i[2]] for i in U]
            R1,R2=[[i[0]]+[i[2]] for i in R]
        A1=[atan2(R1[1]-u[i][1],R1[0]-u[i][0]) for i in range(3)]
        A2=[g(i) for i in A1]
        B1=[atan2(R2[1]-u[i][1],R2[0]-u[i][0]) for i in range(3)]
        B2=[g(i) for i in B1]
        return h(A1,A2) ^ h(B1,B2)

L = [[*map(float, input().split())] for _ in range(6)]
sat = []

for i in range(1, 5):
    for j in range(i + 1, 6):
        AA = L[0] + L[i] + L[j]
        BB = []
        for k in range(1, 6):
            if k != i and k != j:
                BB += L[k]
        if sol(AA, BB):
            sat.append([i + 1, j + 1])

print(len(sat))
for i in sat:
    print(*i, sep = ' ')
