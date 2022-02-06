n=int(input())
def f(n,j):
 x=0
 for k in range(0,len(str(n))):
  d=(n//(10**k))%10;s=(n//(10**(k+1)))*(10**k)+n%(10**k)
  if d>j:a=((s//(10**k))+1)*(10**k)
  elif d==j:a=s+1
  else:a=((s//(10**k)))*(10**k)
  x+=a
 return str(x)
x=0
for k in range(0,len(str(n))-1):
 d=(n//(10**k))%10
 a=10**k-1 if d>0 else n%(10**k)
 x+=(n//(10**(k+1)))*(10**k)+a+1-10**k
L=str(x)
for i in range(9):L+=' '+f(n,i+1)
print(L)
