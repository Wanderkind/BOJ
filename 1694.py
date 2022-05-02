import math
import sys
def f(x,y):return(0<=x<8)*(0<=y<8)
for u in sys.stdin:
 L,l=[[''for _ in range(8)]for _ in range(8)],u.split('/')
 for i in range(8):
  I,z=l[i].strip(),0
  for j in I:
   if j in [str(i+1)for i in range(8)]:z+=int(j)
   else:L[i][z]=j;z+=1
 z=0
 for Q in [[i,j]for i in range(8)for j in range(8)]:
  i,j=Q
  def h(o,r):
   p,q=o//5-2,o%5-2
   if f(i+p,j+q):
    return L[i+p][j+q]not in r
   return 1
  def g(o,r):
   p,q,s,t=o//3-1,o%3-1,1,1
   while f(i+t*p,j+t*q):
    v=L[i+t*p][j+t*q]
    if v in r:s=0;break
    elif v=='':t+=1;continue
    else:break
   return s
  z+=h(6,['K','p','k'])*h(8,['K','p','k'])*h(16,['K','P','k'])*h(18,['K','P','k'])*math.prod([h(w,['K','k'])for w in[7,11,13,17]]+[h(w,['N','n'])for w in[1,3,5,9,15,19,21,23]]+[g(w,['R','Q','r','q'])for w in[1,3,5,7]]+[g(w,['B','Q','b','q'])for w in[0,2,6,8]])*(L[i][j]=='')
 print(z)
