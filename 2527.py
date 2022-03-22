def f(p,rect):
    x,y=p
    x1,y1,x2,y2=rect
    return int(p in [[x1,y1],[x1,y2],[x2,y2],[x2,y1]])+2*int((x in [x1,x2] and (y1<y<y2 or y2<y<y1))^(y in [y1,y2] and (x1<x<x2 or x2<x<x1)))+3*int((x1<x<x2 or x2<x<x1) and (y1<y<y2 or y2<y<y1))

for _ in range(4):
    
    X1,Y1,X2,Y2,x1,y1,x2,y2=map(int,input().split())

    A=[[X1,Y1],[X1,Y2],[X2,Y2],[X2,Y1]]
    B=[[x1,y1],[x1,y2],[x2,y2],[x2,y1]]
    rA=[X1,Y1,X2,Y2]
    rB=[x1,y1,x2,y2]
    
    a,b=[],[]
    for i in A:
        a.append(f(i,rB))
    for i in B:
        b.append(f(i,rA))
    
    S=sum(a)+sum(b)
    if S>5:
        print('a')
    elif S==4:
        print('b')
    elif S==2:
        print('c')
    else:
        if max(X1,X2)<min(x1,x2) or max(x1,x2)<min(X1,X2) or max(Y1,Y2)<min(y1,y2) or max(y1,y2)<min(Y1,Y2):
            print('d')
        else:
            print('a')
