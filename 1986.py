l,z,R,X=[],[],range,lambda:map(int,input().split())
def u(x,y):return(k[2*i+1]+x,k[2*i+2]+y)
def H(a,b,c,d,e,g,h,i,j):
 s,L=1,[]
 while(a*M+b*N+c*s<d)*(e*M+g*s<h)*((N+i*s,M+j*s)not in z)>0:L+=[(N+i*s,M+j*s)];s+=1
 return L
n,m=X();q,k,p=[*X()],[*X()],[*X()]
for i in R(p[0]):z+=[(p[2*i+1],p[2*i+2])]
for i in R(k[0]):z+=[u(0,0)];l+=[u(1,2),u(2,1),u(-1,2),u(2,-1),u(1,-2),u(-2,1),u(-1,-2),u(-2,-1)]
for i in R(q[0]):z+=[(q[2*i+1],q[2*i+2])]
for i in R(q[0]):N,M=q[2*i+1],q[2*i+2];l+=H(0,1,1,n+1,0,0,1,1,0)+H(0,0,1,N,0,0,1,-1,0)+H(1,0,1,m+1,0,0,1,0,1)+H(0,0,1,M,0,0,1,0,-1)+H(0,1,1,n+1,1,1,m+1,1,1)+H(0,1,1,n+1,0,1,M,1,-1)+H(0,0,1,N,0,1,M,-1,-1)+H(0,0,1,n,1,1,m+1,-1,1)
l+=z
for i in R(len(l)-1,-1,-1):
 if(0<l[i][0]<=n)+(0<l[i][1]<=m)<2:del l[i]
print(n*m-len(list(set(l))))
