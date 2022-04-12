from math import*
def f(x): return (1+abs(x)-abs(abs(x)-1))*((x>0)-.5)
ax,ay,az,bx,by,bz,cx,cy,cz=map(int,input().split())
AB=hypot(ax-bx,ay-by,az-bz)
CB=hypot(cx-bx,cy-by,cz-bz)
AC=hypot(ax-cx,ay-cy,az-cz)
A=acos(f(((cx-ax)*(bx-ax)+(cy-ay)*(by-ay)+(cz-az)*(bz-az))/AC/AB))
B=acos(f(((cx-bx)*(ax-bx)+(cy-by)*(ay-by)+(cz-bz)*(az-bz))/CB/AB))
if A<=pi/2 and B<=pi/2:
    t=((bx-ax)*(bx-cx)+(by-ay)*(by-cy)+(bz-az)*(bz-cz))/AB**2
    z=hypot(cx-bx+(bx-ax)*t,cy-by+(by-ay)*t,cz-bz+(bz-az)*t)
elif A>pi/2:
    z=AC
else:
    z=CB
print(z)
