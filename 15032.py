n,k=map(int,input().split())
l=[1]+[0 for _ in range(n)]
for _ in range(k):
    L=[0 for _ in range(n+1)]
    for j in range(n):
        w=l[j];L[j]+=w;L[j+1]+=w
    q=l[n];L[n]+=q;L[n-1]+=q;l=L[:]
print(sum(i*l[i] for i in range(n+1))/2**k)
