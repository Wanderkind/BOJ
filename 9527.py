def f(n):
 a=1
 while n>1:a+=n%2;n//=2
 return a if n>0 else 0
N=[*map(int,input().split())];A=0
for s in range(2):
 n=N[s];n+=s-1;l=[];a=k=1
 if n>0:
  while n>1:
   l+=[n%2];n//=2
  for i in range(len(l)-1,-1,-1):
   if l[i]==1:a=2*a+k+1;k=2*k+1
   else:a+=a-f(k)+k;k*=2
 else:a=0
 A-=a*(-1)**s
print(A)
