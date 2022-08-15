N=int(input())
X=[*map(int,input().split())]
P=[0 for _ in range(N)]
M=[-1]+[0 for _ in range(N)]
L=0
for i in range(N):
    lo,hi=1,L+1
    while lo<hi:
        mid=(lo+hi)//2
        if X[M[mid]]>=X[i]:hi=mid
        else:lo=mid+1
    newL=lo
    P[i]=M[newL-1]
    M[newL]=i
    if newL>L:
        L=newL
S=[0 for _ in range(L)]
k=M[L]
for i in range(L-1,-1,-1):
    S[i]=X[k]
    k=P[k]
print(len(S))
