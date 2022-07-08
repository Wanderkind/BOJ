from math import*
r=6371009
for _ in range(int(input())):
    V,U,v,u=[pi*i/180 for i in map(float,input().split())]
    A,B,C=r*cos(V)*cos(U),r*cos(V)*sin(U),r*sin(V)
    a,b,c=r*cos(v)*cos(u),r*cos(v)*sin(u),r*sin(v)
    d=hypot(A-a,B-b,C-c)
    print(round(2*r*asin(d/2/r)-d))
