from itertools import accumulate as A
import sys
input=sys.stdin.readline
U=lambda:map(int,input().split())
n,m=U()
l=[[0 for _ in range(n+1)]]
for _ in range(n):
    w=[0]+list(A([*U()]))
    for i in range(n):
        w[i+1]+=l[-1][i+1]
    l.append(w)
for _ in range(m):
    X,Y,x,y=U()
    A,B=l[X-1],l[x]
    print(B[y]-B[Y-1]-A[y]+A[Y-1])
