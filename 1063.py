a,b,c=input().split()
K=[ord(a[0])-64,int(a[1])];S=[ord(b[0])-64,int(b[1])]
for _ in range(int(c)):
 o=input();q=r=1;k=K[:];s=S[:]
 for i in range(len(o)):
   if o[i]=='R':k[0]+=1;s[0]+=1
   elif o[i]=='L':k[0]-=1;s[0]-=1
   elif o[i]=='B':k[1]-=1;s[1]-=1
   else:k[1]+=1;s[1]+=1
 for z in k:
  if not 0<z<9:q*=0
 for z in s:
  if not 0<z<9:r*=0
 if q>0:
  if k==S:
   if r>0:K=k;S=s
  else:K=k
for z in [K,S]:z[0]=chr(64+z[0]);z[1]=str(z[1]);print(''.join(z))
