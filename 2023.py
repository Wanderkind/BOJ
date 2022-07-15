import math
def P(a):
    for i in range(2,math.isqrt(a)+1):
        if a%i==0:
            return False
    return True

n=int(input())

l=[[2,3,5,7]]
for _ in range(n-1):
    w=[]
    for i in l[-1]:
        z=10*i
        for j in range(5):
            y=z+2*j+1
            if P(y):
                w.append(y)
    l.append(w)

for i in l[-1]:
    print(i)
