def f(n,j):
 x=0
 for k in range(0,len(str(n))):
  d=(n//(10**k))%10;s=(n//(10**(k+1)))*(10**k)+n%(10**k)
  if d>j:a=((s//(10**k))+1)*(10**k)
  elif d==j:a=s+1
  else:a=((s//(10**k)))*(10**k)
  x+=a
 return x
X=0;l=list(map(int,input().split()))
for q in range(2):
 n=l[q];n+=q-1;L=0
 for i in range(1,10):L+=f(n,i)*i
 X-=L*(-1)**q
print(X)
