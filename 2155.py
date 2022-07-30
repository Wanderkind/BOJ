from math import isqrt
a,b=sorted(map(int,input().split()))
A=isqrt(a-1)
B=isqrt(b-1)
p=a-A*A
q=b-B*B
D=B-A
if p%2:
    l,r=p,p+2*D
    if l<=q<=r:
        z=2*D-1+q%2
    elif q<l:
        z=2*D+l-q
    else:
        z=2*D+q-r
else:
    l,r=p-1,p+2*D-1
    if l<=q<=r:
        z=2*D+q%2
    elif q<l:
        z=2*D+l-q+1
    else:
        z=2*D+q-r+1
print(z)
