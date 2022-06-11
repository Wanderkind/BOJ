E=[0,0,0,0]
z=[3,1,0]
y=[0,1,3]
Q=input().split()
S=[0]*6
k=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
for _ in range(6):
    a,b,w,d,l=input().split()
    A=Q.index(a)
    B=Q.index(b)
    for u in range(6):
        if set([A,B])==set(k[u]):
            if [A,B]==k[u]:
                S[u]=[*map(float,[w,d,l])]
            else:
                S[u]=[*map(float,[l,d,w])]
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                for e in range(3):
                    for f in range(3):
                        p=[z[a]+z[b]+z[c],y[a]+z[d]+z[e],y[b]+y[d]+z[f],y[c]+y[e]+y[f]]
                        t=[]
                        for i in p:
                            if i==max(p):
                                if p.count(i)==3:
                                    t.append(2/3)
                                elif p.count(i)==4:
                                    t.append(1/2)
                                else:
                                    t.append(1.0)
                            elif i==sorted(p)[2]:
                                t.append(1/p.count(i))
                            else:
                                t.append(0)
                        v=S[0][a]*S[1][b]*S[2][c]*S[3][d]*S[4][e]*S[5][f]
                        for m in range(4):
                            E[m]+=v*t[m]
for i in E:print(i)
