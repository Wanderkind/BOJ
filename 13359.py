import math
n,p=map(int,input().split())
l,r=0,1000000
for _ in range(70):
    x=(l+r)/2
    if sum(1/(n+x+i)for i in range(p))>1/x:r=x
    else:l=x
w=int(x)
k=lambda x:math.prod((n-i)/(n+x-i)for i in range(p-1))
print(max(p*i*k(i)/(n+i-p+1)for i in range(max(w-1,0),w+1)))
