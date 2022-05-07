from math import*
e,f,n,k=map(int,input().split())
a,b=sorted([e,f])
c=a*a+b*b
A,B,s,i=a*a/c,b*b/c,1,-1
while s<=k:i+=1;s+=comb(n,i)
print(log(a*b*A**i*B**(n-i)/2))
