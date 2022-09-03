eps=1e-9
import math,sys
input=sys.stdin.readline
def c(n):
    return str(n).count('9')
def v(a,b):
    return f'{str(a).zfill(2)}:{str(b).zfill(2)}'
while 1:
    m,s=map(int,input().split(':'))
    t=m*60+s
    if t==0:
        break
    p,q,e,x=0,'',10000,'99:99'
    for g in range(int(t*0.9+eps)+1,math.ceil(t*1.1-eps)):
        a,b=divmod(g,60)
        if b<40 and a:
            j=c(a)+c(b)
            k=c(a-1)+c(b+60)
            y=max(j,k)
            if j!=k:
                w=v(a,b) if j==y else v(a-1,b+60)
            else:
                w=v(a-1,b+60)
        else:
            y=c(a)+c(b)
            w=v(a,b)
        r=abs(g-t)
        if y>p:
            p=y;q=w;e=r;x=q
        elif y==p:
            if r<e:
                p=y;q=w;e=r;x=q
            elif r==e:
                if w<x:
                     p=y;q=w;e=r;x=q
    print(q)
