import sys
input=sys.stdin.readline
from math import*
U=lambda:map(int,input().split())

A,a=U()
B,b=U()
C,c=U()

def f(x,y):
    if [x,y] in [[A,a],[B,b],[C,c]]:return 1
    x0,y0=A-x,a-y
    x1,y1=B-x,b-y
    x2,y2=C-x,c-y
    t=-atan2(y0,x0)
    x1,y1=x1*cos(t)-y1*sin(t),x1*sin(t)+y1*cos(t)
    x2,y2=x2*cos(t)-y2*sin(t),x2*sin(t)+y2*cos(t)
    p,q=atan2(y1,x1),atan2(y2,x2)
    if -pi in [p,q] or pi in [p,q]:return 1
    return abs(p-q)>=pi

print(round(abs(A*(b-c)+B*(c-a)+C*(a-b))/2,1))
n=int(input())
print(sum([f(*U()) for _ in range(n)]))
