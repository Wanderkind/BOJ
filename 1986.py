l=[];z=[]
def u(x,y):return(k[2*i+1]+x,k[2*i+2]+y)
n,m=map(int,input().split())
q=list(map(int,input().split()))
k=list(map(int,input().split()))
p=list(map(int,input().split()))
for i in range(p[0]):z+=[(p[2*i+1],p[2*i+2])]
for i in range(k[0]):z+=[u(0,0)];l+=[u(1,2),u(2,1),u(-1,2),u(2,-1),u(1,-2),u(-2,1),u(-1,-2),u(-2,-1)]
for i in range(q[0]):z+=[(q[2*i+1],q[2*i+2])]
for i in range(q[0]):
 s=1;N=q[2*i+1];M=q[2*i+2]
 while N+s<=n:
  o=(N+s,M)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while s<N:
  o=(N-s,M)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while M+s<=m:
  o=(N,M+s)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while s<M:
  o=(N,M-s)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while N+s<=n and M+s<=m:
  o=(N+s,M+s)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while N+s<=n and s<M:
  o=(N+s,M-s)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while s<N and s<M:
  o=(N-s,M-s)
  if o not in z:l+=[o];s+=1
  else:break
 s=1
 while s<n and M+s<=m:
  o=(N-s,M+s)
  if o not in z:l+=[o];s+=1
  else:break
l+=z
for i in range(len(l)-1,-1,-1):
 if not(0<l[i][0]<=n and 0<l[i][1]<=m):del l[i]
print(n*m-len(list(set(l))))
