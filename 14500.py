import sys
L,Z=[],[]
n,m=map(int,input().split())
for _ in range(n):L+=[*map(int,sys.stdin.readline().split())]
S=[[[1,m,m+1],[0,1],1],[[1,2,3],[0,3],0],[[m,2*m,3*m],[0,0],3],[[1,2,m+1],[0,2],1],[[m-1,m,m+1],[1,1],1],[[m-1,m,2*m],[1,0],2],[[m,m+1,2*m],[0,1],2],[[m,m+1,2*m+1],[0,1],2],[[1,m-1,m],[1,1],1],[[m-1,m,2*m-1],[1,0],2],[[1,m+1,m+2],[0,2],1],[[m,2*m,2*m+1],[0,1],2],[[1,2,m],[0,2],1],[[1,m+1,2*m+1],[0,1],2],[[m-2,m-1,m],[2,0],1],[[m,2*m,2*m-1],[1,0],2],[[m,m+1,m+2],[0,2],1],[[1,m,2*m],[0,1],2],[[1,2,m+2],[0,2],1]]
for h in S:
 a,b,c=h;p,q,r=a;u,v=b
 for i in range(n*m):
  if u<=i%m<m-v and i//m<n-c:Z+=[L[i]+L[i+p]+L[i+q]+L[i+r]]
print(max(Z))
