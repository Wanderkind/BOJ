from math import*
def T(v,a,r):return[v[0]-sin(a)*r,v[1]+cos(a)*r]
A=['N','NbE','NNE','NEbN','NE','NEbE','ENE','EbN','E','EbS','ESE','SEbE','SE','SEbS','SSE','SbE','S','SbW','SSW','SWbS','SW','SWbW','WSW','WbS','W','WbN','WNW','NWbW','NW','NWbN','NNW','NbW']
while 1:
    n=int(input())
    if n==0:exit()
    z,l,q=[0,0],[],[[0,0]]
    for _ in range(n):
        d,r=input().split()
        l.append([-A.index(d)*pi/16,int(r)])
    for i in l:
        z=T(z,*i)
        q.append(z)
    x,y=z
    f=-float(input())*pi/180
    z=[cos(f)*x-sin(f)*y,sin(f)*x+cos(f)*y]
    x,y=z
    d=[hypot(i[0]-x,i[1]-y)for i in q]
    for i in range(len(q)-1):
        P,Q=q[i],q[i+1]
        x1,y1=P;x2,y2=Q
        if abs(hypot(*P)**2-hypot(*Q)**2+2*x*(x2-x1)+2*y*(y2-y1))<(x1-x2)**2+(y1-y2)**2:
            d.append(abs(x*y1+x1*y2+x2*y-y*x1-y1*x2-y2*x)/(hypot(x1-x2,y1-y2)))
    print('{:.2f}'.format(round(min(d),2)))
