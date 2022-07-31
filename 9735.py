from math import sqrt
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    def f(x):return x*(x*(a*x+b)+c)+d
    p,q=-b/3/a,sqrt(b**2-3*a*c)/3/a
    D=b**2*c**2-4*a*c**3-4*b**3*d-27*a**2*d**2+18*a*b*c*d
    if D<0:
        l,r=-10**6,10**6
        for _ in range(100):
            t=(l+r)/2
            l,r=[[l,t],[t,r]][(a>0)^(f(t)>0)]
        L=[f'{t:.4f}']
    elif D>0:
        l,r=sorted([p-q,p+q])
        for _ in range(100):
            k=(l+r)/2
            l,r=[[k,r],[l,k]][(a>0)^(f(k)>0)]
        l,r=-10**6,k
        for _ in range(100):
            w=(l+r)/2
            l,r=[[l,w],[w,r]][(a>0)^(f(w)>0)]
        l,r=k,10**6
        for _ in range(100):
            e=(l+r)/2
            l,r=[[l,e],[e,r]][(a>0)^(f(e)>0)]
        L=[f'{w:.4f}',f'{k:.4f}',f'{e:.4f}']
    elif b**2==3*a*c:
        l,r=-10**6,10**6
        for _ in range(100):
            t=(l+r)/2
            l,r=[[l,t],[t,r]][(a>0)^(f(t)>0)]
        L=[f'{t:.4f}']
    else:
        if a>0:
            w,e=p-q,p+q
            if f(w)>0:
                l,r=-10**6,w
                for _ in range(100):
                    k=(l+r)/2
                    l,r=[[l,k],[k,r]][f(k)<0]
                L=[f'{k:.4f}',f'{e:.4f}']
            else:
                l,r=e,10**6
                for _ in range(100):
                    k=(l+r)/2
                    l,r=[[l,k],[k,r]][f(k)<0]
                L=[f'{w:.4f}',f'{k:.4f}']
        else:
            w,e=p+q,p-q
            if f(w)<0:
                l,r=-10**6,w
                for _ in range(100):
                    k=(l+r)/2
                    l,r=[[l,k],[k,r]][f(k)>0]
                L=[f'{k:.4f}',f'{e:.4f}']
            else:
                l,r=e,10**6
                for _ in range(100):
                    k=(l+r)/2
                    l,r=[[l,k],[k,r]][f(k)>0]
                L=[f'{w:.4f}',f'{k:.4f}']
    for i in range(len(L)):
        if L[i]=='-0.0000':
            L[i]='0.0000'
    print(*L,sep=' ')
