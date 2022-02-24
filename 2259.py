n,k=map(int,input().split())
L=[*map(int,input().split())]
l=[0];s=0;M=0;N=-99*9
for i in L:
 s+=i;l+=[s]
for i in range(n-k+1):
 z=l[i+k]-l[i]
 if M<z:M=z
 if N<z:N=z
print(M if M>0 else N)
