import sys
input=sys.stdin.readline
from math import *
l=[]
for _ in range(int(input())):
    x,y=map(int,input().split())
    l.append([x*x+y*y,atan2(y,x)])
m=max([i[0] for i in l])
v=sorted([i[1] for i in filter(lambda i:i[0]==m,l)])
M=0
for i in range(len(v)):
    d=(v[i]-v[i-1]-1e-8)%(2*pi)
    if d>M:M=d
print(M/pi*180)
