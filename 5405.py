def f(x):
 x-=1;L,N=[],[[0,0]]
 for i in range(n):e=4**(n-1-i);L+=[x//e];x%=e
 for i in range(n):
  a,b=N[i];v=L[n-1-i]
  if v<1:N+=[[-1/4+b/2,-1/4+a/2]]
  elif v<2:N+=[[-1/4+a/2,1/4+b/2]]
  elif v<3:N+=[[1/4+a/2,1/4+b/2]]
  else:N+=[[1/4-b/2,-1/4-a/2]]
 return N[n]
for _ in range(int(input())):n,h,o=map(int,input().split());p,q=f(h);r,s=f(o);d=((p-r)**2+(q-s)**2)**.5;print(round(d*10*2**n))
