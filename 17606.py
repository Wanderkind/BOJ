def f(p,q):
    a,b=p;c,d=q
    return [a*c-b*d,a*d+b*c]

A=[[-117, 44],[-35, 120],[75, 100],[125, 0],[75, -100],[-35, -120],[-117, -44]]
B=[[-119, 120],[65, 156],[169, 0],[65, -156],[-119, -120]]
C=[[15, 8],[17, 0],[15, -8]]
D=[[21, 20],[29, 0],[21, -20]]

Z=[]
for a in A:
    for b in B:
        for c in C:
            for d in D:
                x,y=f(a,f(b,f(c,d)))
                Z.append([x,y])
                Z.append([-y,x])
                Z.append([-x,-y])
                Z.append([y,-x])

n=int(input())
print(10414625)
for i in range(n):
    x,y=Z[i]
    print(x,y)
