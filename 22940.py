n=int(input())
L=[[*map(int,input().split())]for _ in range(n)]
for j in range(n-1):
    for i in range(n-1,j,-1):
        a,b=L[i][j],L[i-1][j]
        for k in range(n+1):
            L[i][k]*=b;L[i][k]-=L[i-1][k]*a
A=[]
for i in range(n-1,-1,-1):
    k=L[i][n]
    for j in range(n-i-1):
        k-=A[j]*L[i][n-j-1]
    A.append(k//L[i][i])
for i in A[::-1]:
    print(i,end=' ')
