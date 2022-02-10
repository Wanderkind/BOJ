N=int(input())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
l=[];m=[];a=[];b=[];C=A[:];D=B[:];z=0
for i in range(N):
 M=-1
 for j in range(N):
  if C[j]>M:k=j;M=C[j]
 l+=[k];C[k]=-1
for i in range(N):
 M=101
 for j in range(N):
  if D[j]<M:k=j;M=D[j]
 m+=[k];D[k]=101
for i in range(N):z+=A[l[i]]*B[m[i]]
print(z)
