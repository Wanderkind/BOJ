e=[0,[1,1],[-1,1],[-1,-1],[1,-1]]
U=lambda:map(int,input().split())
n,k=U()
x,y=U()
X=Y=0
for i in range(n):
    t=2**(n-1-i)
    p,q=e[int(str(k)[i])]
    X+=t*p
    Y+=t*q
X+=2*x
Y+=2*y
P=Q=0
z=''
for i in range(n):
    t=2**(n-1-i)
    a=X>P
    b=Y>Q
    if abs(X-P)>2*t or abs(Y-Q)>2*t:
        exit(print(-1))
    w=-2*a*b+a-b+3
    u,v=e[w]
    X-=t*u
    Y-=t*v
    z+=str(w)
print(z)
