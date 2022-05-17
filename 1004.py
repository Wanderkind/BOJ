I=input
U=lambda:map(int,I().split())
for i in range(int(I())):
 a=0;b,c,d,e=U();n=int(I())
 for j in range(n):p,q,r=U();a+=((b-p)**2+(c-q)**2-r*r)*((d-p)**2+(e-q)**2-r*r)<0
 print(a)
