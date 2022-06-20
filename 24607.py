from math import gcd
a,b,n=map(int,input().split())
s,t,k=0,1,0
for _ in range(n+1):
    if b*(t-s)<2*a*t:
        q=a*t
        p=b*(t-s)-q
        G=gcd(p,q)
        p//=G
        q//=G
        s,t=p,q
        k+=1
        a,b=b,a
    elif -b*(t+s)<2*a*t:
        s,t=s*b+2*a*t,t*b
        G=gcd(s,t)
        s//=G
        t//=G
        s=-s
        k+=2
        a=-a
    else:
        q=a*t
        p=-b*(t+s)-q
        G=gcd(p,q)
        p//=G
        q//=G
        s,t=-p,q
        k+=3
        a,b=b,a
        if b<0:
            a,b=-a,-b
    if s==0:
        t=1
    if t<0:
        s,t=-s,-t
    if b<0:
        a,b=-a,-b
print([f'-1 1 {s} {t}',f'{s} {t} 1 1',f'1 1 {-s} {t}',f'{-s} {t} -1 1'][k%4])
