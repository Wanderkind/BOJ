from math import*
L,n,l,R=[],int(input()),sorted([*map(int,input().split())]),range
a=[l[i]for i in R(0,n,2)]+[l[i]for i in R(1,n,2)][::-1]
print('{:.3f}'.format(round(sum(a[i-1]*a[i]for i in R(n))*sin(2*pi/n)/2,3)))
