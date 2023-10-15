import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *


isnum = lambda x: 47 < ord(x) < 58
binop = ['*', '/', '+', '-']
sapling = lambda x: [None, x, None, None]


def f(tree):
    try:
        val, prc, lft, rgt = tree
        if val in binop:
            if val == '/':
                val = "//"
            return eval(f"{f(lft)}{val}{f(rgt)}")
        return int(val)
    except(ZeroDivisionError, TypeError):
        print("ROCK")
        exit()


l = list(input())
prc = 2
tree = sapling(2)

while l:
    c = l[0]
    target = tree
    
    if isnum(c):
        while len(l) > 1 and isnum(l[1]):
            c += l[1]
            del l[0]
        while isinstance(target[3], list):
            target = target[3]
        if target[0] == None:
            target[0] = c
        else:
            print("ROCK")
            exit()
    
    elif c == '(':
        if len(l) > 1 and l[1] == ')':
            print("ROCK")
            exit()
        while isinstance(target[3], list):
            target = target[3]
        prc += 3
        target[1] = prc
    
    elif c == ')':
        prc -= 3
        if prc < 0:
            print("ROCK")
            exit()
    
    elif c in binop:
        k = prc - binop.index(c)//2 - 1
        def grow(t):
            if k <= t[1]:
                return [c, k, t, sapling(prc)]
            else:
                return t[:3] + [grow(t[3])]
        tree = grow(tree)
    
    del l[0]

if prc != 2:
    print("ROCK")
else:
    print(f(tree))
