n,r,c=map(int,input().split());x=0
for i in range(n):k=2**(n-i-1);x+=(2*(r//k)+c//k)*k**2;r%=k;c%=k
print(x)
