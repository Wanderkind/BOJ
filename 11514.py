from math import*
while 1:
    d,h,x,n1,n2=map(float,input().split())
    if d==0:exit()
    try:
        l,r=0,x
        for _ in range(40):
            p=(l+r)/2
            if (x-p)*hypot(d,p)/p/hypot(h,x-p)>n2/n1:l=p
            else:r=p
        print(f'{180*atan(d/p)/pi:.2f}')
    except ZeroDivisionError:print('90.00')
