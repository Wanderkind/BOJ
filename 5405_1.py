def f(n,k):
 if n:t=2**n//2;u=t*t;p,q=f(n-1,k%u);return[(q,p),(p,t+q),(t+p,t+q),(2*t-1-q,t-1-p)][k//u]
 return 0,0
for _ in range(int(input())):n,h,o=map(int,input().split());p,q=f(n,h-1);r,s=f(n,o-1);print(round(((p-r)**2+(q-s)**2)**.5*10))
