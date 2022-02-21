n,k=map(int,input().split());L=[1]*(n+1);L[0]=0;x=1;a=[];A='<'
for i in range(n-1):
 c=1;t=(k-1)%(n-i)+1;l=len(a)
 while len(a)==l:
  if L[x]>0:
   if c==t:L[x]=0;a+=[x];A+=str(x)+', '
   c+=1
  x+=1
  if x==n+1:x=1
print(A+str(L.index(1))+'>')
