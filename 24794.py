from math import comb
n,c=map(int,input().split())
l=sorted([*map(int,input().split())])
if c==0:
    print(sum(l)/n)
else:
    z=comb(n-1,c-1)*sum(l[:-1])/(n-1)
    for i in range(c-1,n-1):
        t=n-i-1
        z+=comb(i,c-1)*sum(l[-t:])/t
    print(z/comb(n,c))
