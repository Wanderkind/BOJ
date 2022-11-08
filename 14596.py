def f(n,x):
    x-=1;L=[]
    for i in range(n):L+=[x//(4**(n-1-i))];x%=4**(n-1-i)
    N=[[0,0]]
    for i in range(n):
        if L[n-1-i]<1:N+=[[-1/4+N[i][1]/2,-1/4+N[i][0]/2]]
        elif L[n-1-i]<2:N+=[[-1/4+N[i][0]/2,1/4+N[i][1]/2]]
        elif L[n-1-i]<3:N+=[[1/4+N[i][0]/2,1/4+N[i][1]/2]]
        else:N+=[[1/4-N[i][1]/2,-1/4-N[i][0]/2]]
    return N[n]

def b(n):
    if n<2: return 1
    return 4*b(n-1)+2**(n-1)

def s(x,i):
    A=2**i
    return int((A*A*x+b(i))/A)+1

n,k=map(int,input().split())

i=-1
while n:
    i+=1
    n//=2
x,y=f(i,k)
print(s(x,i),s(y,i))
