m=1000000007
import sys,math
input=sys.stdin.readline
p,q=0,1
for _ in range(int(input())):
    n,s=map(int,input().split())
    p,q=n*p+s*q,n*q
    G=math.gcd(p,q)
    p//=G;q//=G
print((p*pow(q,-1,m))%m)
