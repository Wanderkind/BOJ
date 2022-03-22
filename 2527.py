def f(p,r):x,y=p;x1,y1,x2,y2=r;return int(p in[[x1,y1],[x1,y2],[x2,y2],[x2,y1]])+2*int((x in[x1,x2]and(y1<y<y2 or y2<y<y1))^(y in[y1,y2]and(x1<x<x2 or x2<x<x1)))+3*int((x1<x<x2 or x2<x<x1)and(y1<y<y2 or y2<y<y1))
for _ in range(4):
 X1,Y1,X2,Y2,x1,y1,x2,y2=map(int,input().split());a,b=[],[]
 for i in[[X1,Y1],[X1,Y2],[X2,Y2],[X2,Y1]]:a+=[f(i,[x1,y1,x2,y2])]
 for i in[[x1,y1],[x1,y2],[x2,y2],[x2,y1]]:b+=[f(i,[X1,Y1,X2,Y2])]
 S=sum(a+b)
 if S>0:print('zzczbzaaaaaaa'[S])
 else:print('d'if max(X1,X2)<min(x1,x2)or max(x1,x2)<min(X1,X2)or max(Y1,Y2)<min(y1,y2)or max(y1,y2)<min(Y1,Y2)else'a')
