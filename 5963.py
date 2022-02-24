import math;N,z=map(int,input().split())
for _ in range(z):
 if input()=='P':
  n=int(input())-1;d=0;o=[];s=[]
  for i in range(N):o+=[i+1]
  while d<N:d+=1;k=math.factorial(N-d);p=o[n//k];s+=[str(p)];o.remove(p);n%=k
  print(' '.join(s))
 else:
  m=1;l=[*map(int,input().split())]
  for i in range(N-1):
   n=0
   for j in range(i+1,N):
    if l[i]>l[j]:n+=1
   m+=n*math.factorial(N-i-1)
  print(m)
