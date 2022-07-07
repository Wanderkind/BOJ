def I(a,b,c,d,p,q,r,s):
    if a==c or p==r:
        u=555/797;v=572/797
        a,b=u*a-v*b,v*a+u*b
        c,d=u*c-v*d,v*c+u*d
        p,q=u*p-v*q,v*p+u*q
        r,s=u*r-v*s,v*r+u*s
    u=[abs((b-q)*(r-a)-(a-p)*(s-b))<1e-4 and (p<=a<=r or r<=a<=p),abs((d-q)*(r-c)-(c-p)*(s-d))<1e-4 and (p<=c<=r or r<=c<=p),abs((b-q)*(c-p)-(a-p)*(d-q))<1e-4 and (a<=p<=c or c<=p<=a),abs((b-s)*(c-r)-(a-r)*(d-s))<1e-4 and (a<=r<=c or c<=r<=a)]
    w=any(u)
    if w:
        return 1
    try:
        x=((c-a)*(q*r-p*s)-(r-p)*(b*c-a*d))/((r-p)*(d-b)-(c-a)*(s-q))
        return 1-((a-x)*(c-x)>0 or(p-x)*(r-x)>0)
    except ZeroDivisionError:
        return w*(any([(p<=a<=r or r<=a<=p),(p<=c<=r or r<=c<=p),(a<=p<=c or c<=p<=a),(a<=r<=c or c<=r<=a)]))
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a,b,c,d,p,q,r,s=map(int,input().split())
    if I(a,b,c,d,p,q,p,s) or I(a,b,c,d,p,q,r,q) or I(a,b,c,d,r,q,r,s) or I(a,b,c,d,r,s,p,s):
        print('T')
    elif (p<a<r or r<a<p) and (p<c<r or r<c<p) and (q<b<s or s<b<q) and (q<d<s or s<d<q):
        print('T')
    else:
        print('F')
