c,P=[],[]
for i in range(16):c+=[input()]
for i in range(16):P+=[[*map(int,input().split())]]
def f(p,q):return P[p][q]/100
def v2(n):return 1+(n//2)*4-n
def v4(n):return 3+(n//4)*8-n
def v8(n):return 7+(n//8)*16-n
def v16(n):return 15-n
def r4(n):m,s=v2(n),v4(n);t=v2(s);return f(n,m)*(f(s,t)*f(n,s)+f(t,s)*f(n,t))
def r8(n):o=v8(n);p,q=v2(o),v4(o);r=v2(q);z=[o,p,q,r];return r4(n)*sum([r4(i)*f(n,i)for i in z])
def r16(n):A=v16(n);B,C,E=v2(A),v4(A),v8(A);D=v2(C);F,G=v2(E),v4(E);H=v2(G);z=[A,B,C,D,E,F,G,H];return r8(n)*sum([r8(i)*f(n,i)for i in z])
for i in range(16):w=c[i];r=str(round(r16(i)*100,2));print(w+' '*(10-len(w))+f" p={r+'0'*(3+r.index('.')-len(r))}%")
