import sys
input = lambda: sys.stdin.readline().strip()
U = lambda: map(int, input().split())
#def printflush(x): print(x); sys.stdout.flush()
#from math import *
#from itertools import *
#from random import *
#from functools import *

inf = 10.**10
sq2 = .5**.5

b, a, h = U()

def f(p, q):
    s1 = b*q
    s2 = h*p
    s3 = a*(h - q)
    s4 = h*(b - p) + q*(a - b)
    return max(s1, s2, s3, s4) - min(s1, s2, s3, s4)

def grad_desc(p, q):
    t = .2
    for _ in range(10):
        t /= 2
        while True:
            vals = ((p - t, q + t), (p, q + t), (p + t, q + t),
                    (p - t, q),                 (p + t, q),
                    (p - t, q - t), (p, q - t), (p + t, q - t))
            nine = []
            for pair in vals:
                P, Q = pair
                if P < 0 or Q < 0 or Q > h or (a - b)*Q < h*(P - b):
                    nine.append(inf)
                else:
                    nine.append(f(P, Q))
            nine.insert(4, inf)
            m = min(nine)
            if f(p, q) <= m:
                break
            else:
                u, v = divmod(nine.index(m), 3)
                k = 1 if u == 1 or v == 1 else sq2
                p += k*[-t, 0, t][v]
                q += k*[t, 0, -t][u]
    return f(p, q)/2

points = [
    (b*b/(3*b - a), b*h/(3*b - a)),
    ((a*a - a*b + b*b)/(a + b), a*h/(a + b)),
    (a*b/(a + b), a*h/(a + b)),
    ((a*a + b*b)/2/(a + b), a*h/(a + b))
]
if b < 2*a:
    points.append((a*a/(3*a - b), h*(2*a - b)/(3*a - b)))

print(min(grad_desc(*pair) for pair in points))
