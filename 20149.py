def I(a,b,c,d,p,q,r,s):
    T=0
    if a==c or p==r:
        T=1
        u=555/797;v=572/797
        a,b=u*a-v*b,v*a+u*b
        c,d=u*c-v*d,v*c+u*d
        p,q=u*p-v*q,v*p+u*q
        r,s=u*r-v*s,v*r+u*s
    U=[abs((b-q)*(r-a)-(a-p)*(s-b))<1e-4 and (p<=a<=r or r<=a<=p),abs((d-q)*(r-c)-(c-p)*(s-d))<1e-4 and (p<=c<=r or r<=c<=p),abs((b-q)*(c-p)-(a-p)*(d-q))<1e-4 and (a<=p<=c or c<=p<=a),abs((b-s)*(c-r)-(a-r)*(d-s))<1e-4 and (a<=r<=c or c<=r<=a)]
    w=any(U)
    if w:
        X,Y=[[a,b],[c,d],[p,q],[r,s]][U.index(True)]
        if T:
            X,Y=u*X+v*Y,-v*X+u*Y
        return 1 if (U and abs((d-b)/(c-a)-(s-q)/(r-p))<1e-4 and len(set([(a,b),(c,d),(p,q),(r,s)]))!=3) or (abs((d-b)/(c-a)-(s-q)/(r-p))<1e-4 and sum([(p<=a<=r or r<=a<=p),(p<=c<=r or r<=c<=p),(a<=p<=c or c<=p<=a),(a<=r<=c or c<=r<=a)])>2) else f'1\n{X} {Y}'
    try:
        x=((c-a)*(q*r-p*s)-(r-p)*(b*c-a*d))/((r-p)*(d-b)-(c-a)*(s-q))
        m=1-((a-x)*(c-x)>0 or(p-x)*(r-x)>0)
        if m:
            X=(q-b+a*(d-b)/(c-a)-p*(s-q)/(r-p))/((d-b)/(c-a)-(s-q)/(r-p))
            Y=(d-b)/(c-a)*(X-a)+b
            if T:
                X,Y=u*X+v*Y,-v*X+u*Y
            return f'1\n{X} {Y}'
        else:
            return 0
    except ZeroDivisionError:
        return w*(any([(p<=a<=r or r<=a<=p),(p<=c<=r or r<=c<=p),(a<=p<=c or c<=p<=a),(a<=r<=c or c<=r<=a)]))

a,b,c,d=map(int,input().split())
p,q,r,s=map(int,input().split())
print(I(a,b,c,d,p,q,r,s))
