import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *


isvar = lambda x: 64 < ord(x) < 91
binop = ['+', '-']
sapling = lambda x: [None, x, None, None]


def render(tree):
    val, prc, lft, rgt = tree
    if val in binop:
        if val == '-' and rgt[1] > prc + 1 and rgt[0] in binop:
            return f"{render(lft)}-({render(rgt)})"
        return f"{render(lft)}{val}{render(rgt)}"
    else:
        return val

for _ in range(int(input())):
    
    l = list(input())
    tree = []
    variables = sorted(set(filter(isvar, l)))
    prc = 1
    tree = sapling(1)
    
    while l:
        c = l[0]
        target = tree
        
        if isvar(c):
            while isinstance(target[3], list):
                target = target[3]
            target[0] = c
            neg = False
        
        elif c == '(':
            while isinstance(target[3], list):
                target = target[3]
            prc += 2
            target[1] = prc
        
        elif c == ')':
            prc -= 2
        
        elif c in binop:
            if c == '-':
                neg = True
            k = prc - 1
            def grow(t):
                if k <= t[1]:
                    return [c, k, t, sapling(prc)]
                else:
                    return t[:3] + [grow(t[3])]
            tree = grow(tree)
        
        del l[0]
    
    print(render(tree))
