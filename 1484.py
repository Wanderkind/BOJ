n=int(input())
if n==1 or n%4==2:exit(print(-1))
if n%4==0:
    n//=4
    z=1
else:
    z=2
l=list(filter(lambda i:n%i==0,[i for i in range(1,n+1)]))
L=len(l)
k=L//2
for i in range(k):
    print((l[k+i+L%2]+l[k-i-1])//z)
