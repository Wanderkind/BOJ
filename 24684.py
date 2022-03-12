l=[[-1,0],[0,1],[0,-1],[1,0]]

C=[
[[2,1,2,1],[3,2,3,2],[3,2,2,1],[4,3,3,2]],
[[3,2,4,3],[4,3,5,4],[3,2,3,2],[4,3,4,3]],
[[5,4,6,5],[6,5,7,6],[4,3,5,4],[5,4,6,5]],
[[5,4,4,3],[6,5,5,4],[6,5,5,4],[7,6,6,5]],
[[0,1,1,2],[1,0,2,1],[1,2,0,1],[2,1,1,0]]]

for _ in range(int(input())):
    
    X,Y,x,y=map(int,input().split())
    
    p=(X-2*(Y%5))%5-1
    s=X+l[p][0]
    t=Y+l[p][1]
    
    q=(x-2*(y%5))%5-1
    u=x+l[q][0]
    v=y+l[q][1]
    
    if s>u:
        if t>v:
            s,t=-s,-t
            u,v=-u,-v
            p=[3,2,1,0][p]
            q=[3,2,1,0][q]
        else:
            s,t=t,-s
            u,v=v,-u
            p=[1,3,0,2][p]
            q=[1,3,0,2][q]
    else:
        if t>v:
            s,t=-t,s
            u,v=-v,u
            p=[2,0,3,1][p]
            q=[2,0,3,1][q]
    
    m,n=u-s,v-t
    if not m==n==0:
        if n>3*m:
            b=m
            c=(n-3*m)//5
            z=3*b+5*c
            M=C[1][p][q]-3
            N=C[2][p][q]-5
            if b>0 and c>0:
                z+=min(M,N)
            else:
                z+=M*int(b>0)+N*int(c>0)
        elif 2*n<m:
            a=n
            d=(m-2*n)//5
            z=2*a+5*d
            M=C[0][p][q]-2
            N=C[3][p][q]-5
            if a>0 and d>0:
                z+=min(M,N)
            else:
                z+=M*int(a>0)+N*int(d>0)
        else:
            a=(3*m-n)//5
            b=(n-a)//3
            z=2*a+3*b
            M=C[0][p][q]-2
            N=C[1][p][q]-3
            if a>0 and b>0:
                z+=min(M,N)
            else:
                z+=M*int(a>0)+N*int(b>0)
    else:
        z=C[4][p][q]
    
    print(z)
