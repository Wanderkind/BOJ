import math,sys
input=sys.stdin.readline
n=int(input())
l=[]
for _ in range(int(input())):
    l.append([*map(int,input().split())])
l.sort()
z=1
R,C=0,0
try:
    for i in l:
        r,c=i
        p,q=r-R,c-C
        z*=math.comb(p,q)
        R,C=r,c
    print(z*2**(n-r-1))
except ValueError:
    print(0)
