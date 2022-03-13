from math import gcd as g

def z(i):
    n=len(i)-i.index('.')-1
    i=i.replace('.','')
    a=int(i)
    b=10**n
    G=g(a,b)
    a//=G
    b//=G
    return f'{a}/{b}'

i=input()
if '(' not in i:
    if '.' not in i:
        print(i+'/1')
    else:
        print(z(i))

else:
    v=i.index('.')
    e=int(i[:v])
    f=i.index('(')
    t=f-v-1
    w=i.index(')')-f-1
    b=int('9'*w)*10**t
    a=int(i[f+1:len(i)-1])
    G=g(a,b)
    a//=G
    b//=G
    c,d=map(int,z(i[:f]).split('/'))
    p=b*d
    q=a*d+b*c
    H=g(p,q)
    p//=H
    q//=H
    print(f'{q}/{p}')
