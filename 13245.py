n=int(input())

def f(j):
    x=0
    for k in range(0,len(str(n))):
        w=10**k
        d=(n//w)%10;s=(n//(10*w))*w+n%w
        if d>j:a=(s//w+1)*w
        elif d==j:a=s+1
        else:a=(s//w)*w
        x+=a
    return x

print(sum(j*f(j) for j in range(10)))
