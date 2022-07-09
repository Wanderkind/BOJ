import sys
input=sys.stdin.readline
from math import gcd,lcm
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    L=lcm(b,d)
    A=a*L//b
    C=c*L//d
    p=gcd(A,C)
    q=lcm(A,C)
    G1=gcd(p,L)
    p//=G1
    L1=L//G1
    G2=gcd(q,L)
    q//=G2
    L2=L//G2
    print(f'{p}/{L1}',f'{q}/{L2}')
