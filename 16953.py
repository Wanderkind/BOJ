U=lambda:map(int,input().split())
a,b=U()
L=[a]
z=1
while b not in L:
    z+=1
    l=[]
    for i in L:
        p,q=2*i,10*i+1
        if p<=3*b:l.append(p)
        if q<=3*b:l.append(q)
    if l[0]>b:
        exit(print(-1))
    L=l
print(z)
