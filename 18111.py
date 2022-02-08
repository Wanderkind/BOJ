n,m,b=map(int,input().split());L=[];T=[]
for _ in range(n):L+=list(map(int,input().split()))
for i in range(max(L),min(L)-1,-1):
 c=b;t=0
 for j in range(m*n):
  x=i-L[j];c-=x
  t+=x if 0<=x else -2*x
 if c<0:t=9**9
 T+=[t]
print(min(T),max(L)-T.index(min(T)))
