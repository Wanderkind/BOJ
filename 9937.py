from math import comb as c
import sys
input=sys.stdin.readline
n=int(input())
N=c(n,3)
d={}
for _ in range(n):
    A,B,C=[*map(int,input().split())]
    t=A/B if B else ''
    if t not in d:
        d[t]=1
    else:
        d[t]+=1
l=[d[i] for i in d]
for i in l:
    N-=c(i,3)
a=[c(i,2) for i in l]
z=N+sum(a[i]*l[i]for i in range(len(l)))-sum(l)*sum(a)
print(z%1000000007)
