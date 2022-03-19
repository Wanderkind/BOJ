from math import comb as c
n,m,k=map(int,input().split())
S=s=n+m
if k>c(S,m):exit(print(-1))
a,z,l,p=[],[],['']*S,m
while 1:
 while 1:
  C=c(p,m)
  if C<k:p+=1;continue
  elif C==k:
   for i in range(m):z.append(p-1-i)
   for i in range(S):l[i]='z'if i in z else'a'
   exit(print(''.join(l[::-1])))
  else:
   z.append(p-1)
   for i in range(p,s):a.append(i)
   s=S-len(a)-len(z);k-=c(p-1,m);m-=1;p=m;break
