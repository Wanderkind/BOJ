import math

def f(x):
    X=x[::-1]
    n=len(X)
    s=0
    for i in range(n):
        s+=2**(n-1-i)*11**i*int(X[i])
    return s

def g(Q):
    n=int(math.log(Q,11))+1
    x=0
    while x<2**(n+1):
        N=Q
        X=list(bin(x)[2:].zfill(n))
        l=[]
        for i in range(n):
            k=2**i*11**(n-1-i)
            a=N//k-int(X[i])
            N-=a*k
            if a<0 or N<0:break
            l.append(str(a))
        if N==0:return ''.join(l)
        x+=1
    return 'NIE'

n=int(input())

for i in range(20):
    if n==11**i:
        exit(print(10**i))

G=g(n)
if G!='NIE':
    if f(G)!=n or G[0]=='0':
        print('NIE')
        exit()
print(G)
