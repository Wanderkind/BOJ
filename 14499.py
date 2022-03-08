n,m,Y,X,p=map(int,input().split())
k,M='310542215043402351152304',[]
for i in range(n):M+=[input().split()]
C,D=[*map(int,input().split())],['0']*6
for i in range(p):
 c,T=C[i]-1,[X,Y];d=[D[int(k[6*c+v])]for v in range(6)];T[c//2]+=2*int(c%3<1)-1;x,y=T
 if 0<=y<n and 0<=x<m:
  s=M[y][x]
  if s=='0':M[y][x]=d[5]
  else:d[5]=s;M[y][x]='0'
  X,Y,D=x,y,d[:];print(D[0])
