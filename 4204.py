
import math

def sol(e):
        
    n = int(input())
    ls = [*map(float, input().split())]
    
    lst = []
    for i in range(2*n + 1):
        w = 0
        for j in range(i + 1):
            if j <= n and i - j <= n:
                w += ls[j]*ls[i - j]
        lst.append(w)
    
    def f(x):
        ans = 0
        for i in range(2*n + 1):
            ans += lst[i]/(i + 1)*x**(i + 1)
        return ans
    
    xl, xh, inc = map(float, input().split())
    v = lambda x: (f(x) - f(xl))*math.pi
    vol = v(xh)
    print(f"Case {e}: {vol:.2f}")
    
    if vol < inc:
        print("insufficient volume")
    
    else:
        k = min(8, int(vol/inc))
        
        def mark(z):
            vv = inc*z
            l = xl; r = xh
            while 1:
                t = (l + r)/2
                o = v(t)
                if o < vv - 0.00000001:
                    l = t
                elif vv + 0.00000001 < o:
                    r = t
                else:
                    return t - xl
        
        print(*[f"{mark(u + 1):.2f}" for u in range(k)], sep = ' ')

e = 0
while 1:
    try:
        e += 1
        sol(e)
    except EOFError:
        break
