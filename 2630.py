import math
N=int(input())
n,W,L,a=round(math.log2(N)),[],[[0]*N*N],1
for _ in range(N):W+=[*input().split()]
for q in range(N*N):
 r,c=divmod(q,N);x=0
 for i in range(n):k=2**(n-i-1);x+=(2*(r//k)+c//k)*k**2;r%=k;c%=k
 L[0][x]=int(W[q])
while a>0:
 a=0
 for q in range(len(L)-1,-1,-1):
  l=L[q];t=len(l)//4
  if len(set(l))==2:
   for w in range(3):L.insert(q,l[t*w:-t*(3-w)])
   L.insert(q,l[t*3:]);del L[q+4];a+=1
for i in range(len(L)):L[i]=L[i][0]
print(L.count(0))
print(L.count(1))
