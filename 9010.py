for _ in range(int(input())):
    m,n=map(int,input().split())
    print(f'{(n/2+(m*m-1)/3/m):.1f}')
