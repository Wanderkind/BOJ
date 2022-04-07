def f(x):
 x-=1;L,N=[],[[0,0]]
 for i in range(n):e=4**(n-1-i);L+=[x//e];x%=e
 for i in range(n):a,b=N[i];N+=[[[-1/4+b/2,-1/4+a/2],[-1/4+a/2,1/4+b/2],[1/4+a/2,1/4+b/2],[1/4-b/2,-1/4-a/2]][L[n-1-i]]]
 return N[n]
for _ in range(int(input())):n,h,o=map(int,input().split());p,q=f(h);r,s=f(o);print(round(((p-r)**2+(q-s)**2)**.5*10*2**n))
