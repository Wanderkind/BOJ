import math;N=int(input());l=list(map(int,input().split()))
if l[0]<2:
 n=l[1]-1;d=0;o=[];s=[]
 for i in range(N):o+=[i+1]
 while d<N:d+=1;k=math.factorial(N-d);p=o[n//k];s+=[str(p)];o.remove(p);n%=k
 print(' '.join(s))
else:
 m=1
 for i in range(1,N):
  n=0
  for j in range(i+1,N+1):
   if l[i]>l[j]:n+=1
  m+=n*math.factorial(N-i)
 print(m)
