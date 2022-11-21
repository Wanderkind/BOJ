import sys
input=sys.stdin.readline

p=(1+5**.5)/2

def f(a,b):
    a,b=sorted([a,b])
    n=0
    while 1:
        A=int(n*p)
        if A>=a:
            break
        n+=1
    print("Farmer John" if (A==a and int(n*p*p)==b) else "Bessie")

input()
for _ in range(int(input())):
    f(*map(int,input().split()))
