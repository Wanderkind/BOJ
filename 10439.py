from math import*
for _ in range(int(input())):
    k,n,m=map(int,input().split())
    S,A=sin(pi/n),tan(pi/n)
    l,r=0,100
    for _ in range(40):
        t=(l+r)/2
        if t/(1/S+sqrt(2*t+1))<A:l=t
        else:r=t
    R=t**(m-1)*S/(1-S)
    print(k,f'{R:.3f}',f'{2*(pi+n)*R:.3f}')
