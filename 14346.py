import sys
input = lambda: sys.stdin.readline().strip()
from math import *


for tc in range(int(input())):

    n, a, b = map(float, input().split())
    c = float(input())
    
    def total(xp, yp, xq, yq):
        dx, dy = xq - xp, yq - yp
        d = hypot(dx, dy)
        if not d:
            return 0
        h = abs(dx*(yp - c) - dy*xp)/d
        if not h:
            return inf
        S = sqrt(max(xp*xp + (c - yp)**2 - h*h, 0))
        return d + (atan2(d - S, h) + atan2(S, h))/h
    
    def val(eight):
        P1, Q1, P2, Q2, P3, Q3, P4, Q4 = eight
        t1 = total(-10.,  a,  P1, Q1)
        t2 = total(  P1, Q1,  P2, Q2)
        t3 = total(  P2, Q2,  P3, Q3)
        t4 = total(  P3, Q3,  P4, Q4)
        t5 = total(  P4, Q4,  10., b)
        return t1 + t2 + t3 + t4 + t5
    
    x1, y1 = -1.5, (23*a + 17*b)/40 + 0.1
    x2, y2 = -0.5, (21*a + 19*b)/40 + 0.1
    x3, y3 =  0.5, (19*a + 21*b)/40 + 0.1
    x4, y4 =  1.5, (17*a + 23*b)/40 + 0.1
        
    m = val((x1, y1, x2, y2, x3, y3, x4, y4))
    for i in range(3, 9):
        t = 4.**(-i)
        s2 = t/sqrt(2)
        while True:
            p1, q1 = x1, y1
            p2, q2 = x2, y2
            p3, q3 = x3, y3
            p4, q4 = x4, y4
            sxtn = (
                (p1 + t, q1, p2, q2, p3, q3, p4, q4),
                (p1 + s2, q1 + s2, p2, q2, p3, q3, p4, q4),
                (p1, q1 + t, p2, q2, p3, q3, p4, q4),
                (p1 - s2, q1 + s2, p2, q2, p3, q3, p4, q4),
                (p1 - t, q1, p2, q2, p3, q3, p4, q4),
                (p1 - s2, q1 - s2, p2, q2, p3, q3, p4, q4),
                (p1, q1 - t, p2, q2, p3, q3, p4, q4),
                (p1 + s2, q1 - s2, p2, q2, p3, q3, p4, q4),
                (p1, q1, p2 + t, q2, p3, q3, p4, q4),
                (p1, q1, p2 + s2, q2 + s2, p3, q3, p4, q4),
                (p1, q1, p2, q2 + t, p3, q3, p4, q4),
                (p1, q1, p2 - s2, q2 + s2, p3, q3, p4, q4),
                (p1, q1, p2 - t, q2, p3, q3, p4, q4),
                (p1, q1, p2 - s2, q2 - s2, p3, q3, p4, q4),
                (p1, q1, p2, q2 - t, p3, q3, p4, q4),
                (p1, q1, p2 + s2, q2 - s2, p3, q3, p4, q4),
                (p1, q1, p2, q2, p3 + t, q3, p4, q4),
                (p1, q1, p2, q2, p3 + s2, q3 + s2, p4, q4),
                (p1, q1, p2, q2, p3, q3 + t, p4, q4),
                (p1, q1, p2, q2, p3 - s2, q3 + s2, p4, q4),
                (p1, q1, p2, q2, p3 - t, q3, p4, q4),
                (p1, q1, p2, q2, p3 - s2, q3 - s2, p4, q4),
                (p1, q1, p2, q2, p3, q3 - t, p4, q4),
                (p1, q1, p2, q2, p3 + s2, q3 - s2, p4, q4),
                (p1, q1, p2, q2, p3, q3, p4 + t, q4),
                (p1, q1, p2, q2, p3, q3, p4 + s2, q4 + s2),
                (p1, q1, p2, q2, p3, q3, p4, q4 + t),
                (p1, q1, p2, q2, p3, q3, p4 - s2, q4 + s2),
                (p1, q1, p2, q2, p3, q3, p4 - t, q4),
                (p1, q1, p2, q2, p3, q3, p4 - s2, q4 - s2),
                (p1, q1, p2, q2, p3, q3, p4, q4 - t),
                (p1, q1, p2, q2, p3, q3, p4 + s2, q4 - s2)
            )
            mm = val((p1, q1, p2, q2, p3, q3, p4, q4))
            for eight in sxtn:
                v = val(eight)
                if v < mm:
                    neweight = eight
                    mm = v
            if m == mm:
                break
            if mm < m:
                m = mm
            x1, y1, x2, y2, x3, y3, x4, y4 = neweight
    
    assert(m != inf)
    print(f"Case #{tc + 1}: {m*0.9992}")
