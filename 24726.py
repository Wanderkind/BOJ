import math
f,g,h,j,k,l=map(int,input().split())
def F(x,y,z):
    A,a=x;B,b=y;C,c=z
    P=(c-b)/(C-B)if C!=B else 10**9
    Q=(c-a)/(C-A)if C!=A else 10**9
    R=(b-a)/(B-A)if B!=A else 10**9
    return abs((((Q*Q-R*R)*(B-A)**3+(P*P-Q*Q)*(B-C)**3)/3+a*(Q-R)*(B-A)**2+c*(P-Q)*(B-C)**2)*math.pi)
print(F(*sorted([[f,g],[h,j],[k,l]])),F(*sorted([[g,f],[j,h],[l,k]])))
