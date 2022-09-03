import sys
input=sys.stdin.readline
from math import hypot as h
for _ in range(int(input())):
    r,a,b,x,y,X,Y=map(float,input().split())
    print('The given circle and rectangle',['do not overlap.','overlap.'][(any(h(i[0]-a,i[1]-b)<r for i in [[x,y],[X,y],[x,Y],[X,Y]])) or (x<=a<=X and b-r<Y and y<b+r) or (y<=b<=Y and a-r<X and x<a+r)])
