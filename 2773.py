u=555/797;v=572/797
import sys
input=sys.stdin.readline
U=lambda:map(float,input().split())
for _ in range(int(input())):
    xa,ya=U()
    xb,yb=U()
    xc,yc=U()
    xa,ya=u*xa-v*ya,v*xa+u*ya
    xb,yb=u*xb-v*yb,v*xb+u*yb
    xc,yc=u*xc-v*yc,v*xc+u*yc
    xba,yba=xb-xa,yb-ya
    xd,yd=xa-yba,ya+xba
    xe,ye=xb-yba,yb+xba
    xac,yac=xa-xc,ya-yc
    xg,yg=xa-yac,ya+xac
    xcb,ycb=xc-xb,yc-yb
    xj,yj=xb-ycb,yb+xcb
    xl,yl=(xg+xd)/2,(yg+yd)/2
    xm,ym=(xe+xj)/2,(ye+yj)/2
    xp,yp=xa-xl,ya-yl
    xq,yq=xb-xm,yb-ym
    Q=(yp*(xa-xb)+xp*(yb-ya))/(yp*xq-xp*yq)
    P=(xb-xa+Q*xq)/xp
    X,Y=xa+P*xp,ya+P*yp
    print(f'{u*X+v*Y+0.00001:.4f} {-v*X+u*Y+0.00001:.4f}')
