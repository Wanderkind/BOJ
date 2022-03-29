L1,L2=[],[]
n,m=map(int,input().split())
N=2*n*m

for i in range(n):
    l=[*map(int,input().split())]
    L1.append(l)

for i in range(m):
    l=[]
    for j in range(n):
        l.append(L1[j][i])
    L2.append(l)

for i in range(n):
    e=[0]
    v=L1[i]
    for j in range(m-1,0,-1):
        if v[j]==v[j-1]:
            del v[j]
    l=[0]+v+[0]
    for j in range(1,len(v)+1):
        if (l[j]-l[j-1])*(l[j+1]-l[j])<0:
            e.append(l[j])
    for j in range(1,len(e)):
        N+=abs(e[j]-e[j-1])
    N+=e[-1]
    
for i in range(m):
    e=[0]
    v=L2[i]
    for j in range(n-1,0,-1):
        if v[j]==v[j-1]:
            del v[j]
    l=[0]+v+[0]
    for j in range(1,len(v)+1):
        if (l[j]-l[j-1])*(l[j+1]-l[j])<0:
            e.append(l[j])
    for j in range(1,len(e)):
        N+=abs(e[j]-e[j-1])
    N+=e[-1]

print(N)
