from math import *
import sys
input=lambda:sys.stdin.readline().strip()
#U=lambda:map(int,input().split())
from itertools import permutations as P

def NewCircleLocation(leftloc, leftrad, rightrad):
    return leftloc + 2*sqrt(leftrad*rightrad)

def Size(p, n):
    
    placement = [p[0]]
    
    for i in range(1, n):
        rightrad = p[i]
        rightmost = 0
        for j in range(i):
            newloc = max(NewCircleLocation(placement[j], p[j], rightrad), rightrad)
            if newloc > rightmost:
                rightmost = newloc
        placement.append(rightmost)
    
    return max((placement[i] + p[i]) for i in range(n))

def Sol():
    
    l = [*map(float,input().split())]
    n = int(l[0])
    del l[0]
    
    minimum = inf
    for p in P(l, n):
        size = Size(p, n)
        if size < minimum:
            minimum = size
    
    print(f"{minimum:.3f}")

for _ in range(int(input())):
    Sol()
