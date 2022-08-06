from math import*
n=int(input())
def P(a):
    for i in range(2,isqrt(a)+1):
        if a%i==0:return False
    return True
print(prod([i**int(log(n,i))for i in list(filter(P,[*range(2,n+1)]))])%987654321)
