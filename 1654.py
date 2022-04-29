import math
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
L=[int(input()) for _ in range(n)]
z=sum(L)//k+1
m=min(L)
h=int(m/(m//z+2))
def f(x):
    return sum(i//x for i in L)
l,r,y=h,z,-1
while 1:
    t=l+(r-l)//2
    if t==y:
        exit(print(t))
    else:
        y=t
    if f(t)<k:
        r=t
    elif f(t)>k:
        l=t
    else:
        break
while f(t)==k:
    t+=max(int(1/max(math.log(k/n),0.0001)),1)
while f(t)!=k:
    t-=1
print(t)
