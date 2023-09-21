import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *


n = int(input())

def bad(b, new):
    if new in b:
        return True
    l = len(b)
    for i in range(l):
        d = l - i
        if abs(b[i] - new) == d:
            return True
    return False

stack = [([], n - 1)]
start = 0
cnt = 0

while 1:
    bb, s = stack[-1]
    b = bb[:]
    #print(b)
    advance = False
    for i in range(start, n):
        if not bad(b, i):
            advance = True
            break
    if advance:
        start = 0
        b.append(i)
        if len(b) == n:
            cnt += 1
        stack.append((b, start))
        continue
    else:
        start = b[-1] + 1
        if start == n:
            del stack[-1]
            try:
                start = stack[-1][0][-1] + 1
            except:
                break
        del stack[-1]

print(cnt)
