w=10**9+7
n=int(input())
def mul(A,B):
    L=[]
    for i in range(2):
        a=A[i];l=[]
        for j in range(2):
            b=[B[i][j]for i in range(2)];s=0
            for k in range(2):
                s+=a[k]%w*b[k]%w
            l.append(s%w)
        L.append(l)
    return L
B=bin(n)[2:][::-1]
L=[[1,1],[1,0]]
LL=[[1,0],[0,1]]
l=L[:]
for i in range(len(B)):
    if i>0:
        l=mul(l,l)
    if int(B[i]):
        LL=mul(LL,l)
print(LL[0][1])
