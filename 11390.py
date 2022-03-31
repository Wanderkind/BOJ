from math import*
e,f,n,k=map(int,input().split())
a,b=sorted([e,f])
c=a**2+b**2
A,B,s,i=a**2/c,b**2/c,1,-1
while s<=k:i+=1;s+=comb(n,i)
print(log(a*b*A**i*B**(n-i)/2))
