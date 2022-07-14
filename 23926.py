def f(n):
    z=str(n)
    N=len(z)
    s=(5**N-5)//4
    for i in range(N):
        k=int(z[i])
        B=k%2==i%2
        s+=5**(N-1-i)*((k+i%2+B)//2)
        if B:break
    return s+(i==N-1)*(1-B)
for i in range(int(input())):
    l,r=map(int,input().split())
    print(f'Case #{i+1}: {f(r)-f(l-1)}')
