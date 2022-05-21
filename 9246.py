import math
l=[*map(float,input().split())]
s=float(input())
def f(r):return 1-math.e**(-r*r/2/s/s)
L=[0,*map(f,l)]
print(sum([50,25,10.5,31.5,10.5,21][i]*(L[i+1]-L[i])for i in range(6)))
