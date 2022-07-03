from math import*
import sys
input=sys.stdin.readline
t=sqrt(3)
while 1:
    n=int(input())
    if n==0:
        break
    if n%3==0:
        n//=3
    k=t*tan(pi/3/n)
    a=k/(1+k)
    print(a/t*n)
