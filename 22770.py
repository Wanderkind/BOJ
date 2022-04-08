from math import*
def f(a,b,x):return b*(x/a*sqrt(a**2-x**2)+a*asin(x/a))/2
for _ in range(int(input())):
    A,B=map(int,input().split())
    a,b=map(int,input().split())
    if(A-a)*(B-b)<0:
        a,A=sorted([A,a])
        B,b=sorted([B,b])
        p=A*a*sqrt((B**2-b**2)/(a**2*B**2-A**2*b**2))
        q=B*b*sqrt((A**2-a**2)/(b**2*A**2-B**2*a**2))
        print(4*(f(A,B,p)+f(b,a,q)-p*q))
    else:
        print(min(A*B,a*b)*pi)
