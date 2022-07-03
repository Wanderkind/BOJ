from math import sqrt
a,b,c,d=map(int,input().split())
def X(p,q,r,s):
    S=max(abs(p-q),abs(r-s))
    L=min(p+q,r+s)
    pp,qq,rr,ss=p*p,q*q,r*r,s*s
    def f(x):return sqrt(4*pp*qq-(pp+qq-x*x)**2)
    def g(x):return sqrt(4*rr*ss-(rr+ss-x*x)**2)
    def A(x):return (pp+qq)*g(x)+(rr+ss)*f(x)-(f(x)+g(x))*x*x
    l,R=S,L
    for _ in range(30):
        t=(l+R)/2
        if A(t)>0:
            l=t
        else:
            R=t
    return (f(t)+g(t))/4
print(max(X(a,b,c,d),X(a,c,b,d)))
