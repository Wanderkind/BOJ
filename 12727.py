from decimal import*
getcontext().prec=200
Z=Decimal((Decimal(5))**Decimal(.5))
for i in range(int(input())):
    n=int(input())
    a,b=3,1
    for _ in range(n-1):
        a,b=3*a+5*b,3*b+a
    k=str(a+Decimal(b*Decimal(Z)))
    A=k.index('.')
    print(f'Case #{i+1}: {k[max(A-3,0):A].zfill(3)}')
