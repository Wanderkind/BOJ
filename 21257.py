import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m,P=map(int,input().split())
    p=1-P/10000
    def f(t): return (t*n+m)/(1-p**t)
    z=10**30
    t=1
    while 1:
        F=f(t)
        if F<z:
            z=F
            t+=100
        else:
            break
    print(min(f(t) for t in range(max(1,t-200),t)))
