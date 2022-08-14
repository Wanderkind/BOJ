U=lambda:map(int,input().split())
n,b=U()
def mul(A,B):
    L=[]
    for i in range(n):
        a=A[i];l=[]
        for j in range(n):
            b=[B[i][j]for i in range(n)];s=0
            for k in range(n):
                s+=a[k]%1000*b[k]%1000
            l.append(s%1000)
        L.append(l)
    return L
B=bin(b)[2:][::-1]
L=[[*U()]for _ in range(n)]
LL=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    LL[i][i]=1
l=L[:]
for i in range(len(B)):
    if i>0:
        l=mul(l,l)
    if int(B[i]):
        LL=mul(LL,l)
for i in LL:
    print(*i,sep=' ')
