from math import*
while 1:
    try:
        r,h,D,A,d,a=map(float,input().split())
        R=hypot(r,h)
        c=pi*(a-A)*r/R/180
        t=2*pi*r/R
        print('{:.2f}'.format(round(min(hypot(D-d*cos(c),d*sin(c)),hypot(D-d*cos(t-c),d*sin(t-c))),2)))
    except EOFError:
        break
