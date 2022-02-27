a,b,c=map(int,input().split())
B,d,x=bin(b)[2:],[a%c],1;l=len(B)
for i in range(l-1):d+=[d[i]**2%c]
for i in range(l):
 if B[i]=='1':x*=d[l-1-i]
print(x%c)
