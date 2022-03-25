L=[]
n=0
while 1:
    A,B=input().split()
    if A==B=='0':
        break
    else:
        n+=1
        L.append('Problem '+str(n))
        a=int(A)
        b=B[::-1]
        l=[]
        z=0
        for i in range(len(b)):
            v=int(b[i])
            if v!=0:
                l.append(str(a*v*10**z)+' '*(i-z))
                z=0
            else:
                z+=1
        f=str(a*int(B))
        N=len(f)
        L.append(' '*(N-len(A))+A)
        L.append(' '*(N-len(B))+B)
        if len(l)>1:
            L.append('-'*N)
            for i in l:
                L.append(' '*(N-len(i))+i)
        L.append('-'*N)
        L.append(f)
for i in L:
    print(i.rstrip())
