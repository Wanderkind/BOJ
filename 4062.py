from math import log
import sys
input=sys.stdin.readline
l=[0,2,4,6,30,32,34,36,40,42,44,46,50,52,54,56,60,62,64,66]
while 1:
    n=int(input())
    if n==0:break
    s=0
    k=int(log(n,20))
    if n>=20**7:
        k-=1
        s=2*(n//(20**7))*10**27
        n-=20**7
    for i in range(k+1):
        a=k>6
        s+=l[n%20]*1000**(i+2*a)
        n//=20
    S=list(str(s))
    t=len(S)
    for i in range(t):
        if i%3==0 and i>0:
            S.insert(t-i,',')
    print(''.join(S))
