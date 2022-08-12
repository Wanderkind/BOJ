from math import*
for _ in range(int(input())):
    A,B=map(int,input().split())
    a,b=map(int,input().split())
    if(A-a)*(B-b)<0:
        x=sqrt((B*B-b*b)/(1-(A*b/a/B)**2))
        t1=asin(x/B)
        S1=A*B*2*t1
        y=sqrt(B*B-x*x)*a/b
        t2=asin(y/a)
        S2=b*a*2*t2
        print(S1+S2)
    else:
        print(min(A*B,a*b)*pi)
