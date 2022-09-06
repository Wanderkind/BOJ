from math import*
n,k=map(int,input().split())
q=3**n
p=(q-sum((2**i-2*sum(comb(i,j)for j in range(i-k+1)))*comb(n,i)for i in range(min(n+1,2*k-1))))//2
G=gcd(p,q)
print(p//G,q//G)
